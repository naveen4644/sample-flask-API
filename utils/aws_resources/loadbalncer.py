import boto3
client = boto3.client('elbv2')

def create_target_group():
    try:
        response = client.create_target_group(
            name='test-orthos-target-group',
            Protocol='HTTP',
            ProtocolVersion='HTTP1',
            Port=5005,
            VpcId='vpc-062af964db13d2f63',
            HealthCheckProtocol='HTTP',
   
            HealthCheckEnabled=True,
            HealthCheckPath='/',
            HealthCheckIntervalSeconds=30,
            HealthCheckTimeoutSeconds=5,
            HealthyThresholdCount=5,
            UnhealthyThresholdCount=2,
            Matcher={
                'HttpCode': '302',
       
            },  
            TargetType='ip',
            Tags=[
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            IpAddressType='ipv4'
        )
        return response['targetgroup']
    except Exception as e:
        print(str(e))
        return False

def create_load_balancer():
    try:

        response = client.create_load_balancer(
            Name='test-othos-lb',
            Subnets=[
                'subnet-054c4c9508bcf7e0e',
                'subnet-0eef3203f25475c0a',
                'subnet-0f706c8e478ddf6d3',
                'subnet-0dd46293c76fd15c6',
                'subnet-0826eed225ee08584',
                'subnet-0c2a4c881b34306f9'
            ],
    
            SecurityGroups=[
                'sg-095f4e84a06cb3243'
            ],
            Scheme='internet-facing',
            Tags=[
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            Type='application',
            IpAddressType='ipv4',
        )
        return response['targetgroup']
    except Exception as e:
        print(str(e))
        return False
response1 = client.describe_target_groups(
     Names=[
        'test-orthos-target-group',
    
     ]
)


response2 = client.describe_load_balancers(
     Names=[
        'test-othos-lb',
    
     ]
)

response = client.create_listener(
    DefaultActions=[
        {
            'TargetGroupArn': response1['TargetGroups'][0]['TargetGroupArn'],
            'Type': 'forward',
        },
    ],
    LoadBalancerArn=response2['LoadBalancers'][0]['LoadBalancerArn'],
    Port=80,
    Protocol='HTTP',
)