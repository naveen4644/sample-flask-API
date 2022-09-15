import boto3
from values import (
    ECS_CLUSTER_NAME, DOCKER_IMAGE_URI, ECS_CONTAINER_NAME, 
    ECS_TASK_DEFINITION_NAME, ECS_TASK_ROLE_ARN, ECS_TASK_DEFINITION_ARN
)

client = boto3.client('ecs')

def create_task_definition():
    try:
        response = client.register_task_definition(
            family=ECS_TASK_DEFINITION_NAME,
            taskRoleArn=ECS_TASK_ROLE_ARN,
            executionRoleArn=ECS_TASK_ROLE_ARN,
            networkMode='awsvpc',
            containerDefinitions=[
                {
                    'name': ECS_CONTAINER_NAME,
                    'image': f'{DOCKER_IMAGE_URI}:latest',
                    'portMappings': [
                        {
                            'containerPort': 5005,
                            'protocol': 'tcp'
                        },
                    ],
                    'essential': True,
                    'logConfiguration': {
                        'logDriver': 'awslogs',
                        'options': {                            
                            'awslogs-group': f'/ecs/{ECS_TASK_DEFINITION_NAME}',
                            'awslogs-region': 'us-east-1',
                            'awslogs-create-group': 'true',
                            'awslogs-stream-prefix': 'ecs'
                        }
                    }
                }
            ],
            requiresCompatibilities=[
                'FARGATE',
            ],
            cpu='256',
            memory='512',
            runtimePlatform={
                'cpuArchitecture': 'X86_64',
                'operatingSystemFamily': 'LINUX'
            }
        )
        return response['taskDefinition']
    except Exception as e:
        print(str(e))
        return False

def create_service():
    try:
        response = client.create_service(
    cluster=ECS_CLUSTER_NAME,
    serviceName=ECS_TASK_DEFINITION_NAME,
    taskDefinition=ECS_TASK_DEFINITION_ARN,
    loadBalancers=[
        {
            'targetGroupArn': 'arn:aws:elasticloadbalancing:us-east-1:763021346403:targetgroup/test-orthos-target-group/9ffa9282e5823e62',
            'containerName': ECS_CONTAINER_NAME,
            'containerPort': 5005
        },
    ],
    
    desiredCount=1,
   
    launchType='FARGATE',
    
    platformVersion='LATEST',
    deploymentConfiguration={
        'deploymentCircuitBreaker': {
            'enable': True,
            'rollback': True
        
        },
        'maximumPercent': 200,
        'minimumHealthyPercent': 100
    },
   
    networkConfiguration={
        'awsvpcConfiguration': {
            'subnets': [
                'subnet-054c4c9508bcf7e0e',
                'subnet-0eef3203f25475c0a',
                'subnet-0f706c8e478ddf6d3',
                'subnet-0dd46293c76fd15c6',
                'subnet-0826eed225ee08584',
                'subnet-0c2a4c881b34306f9'
            ],
            'securityGroups': [
                'sg-08acefac281992497',
            ],
            'assignPublicIp': 'ENABLED'
        }
    },
    healthCheckGracePeriodSeconds=0,
   
    propagateTags='TASK_DEFINITION',

)
        return response['service']
    except Exception as e:
        print(str(e))
        return False