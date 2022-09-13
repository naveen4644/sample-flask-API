ACCOUNT_ID='763021346403'
ECR_REPO_NAME='dev-orthos'
ECS_CLUSTER_NAME='orthos-cluster'
ECS_TASK_ROLE_NAME='orthos_project_ecs_performer'
ECS_TASK_ROLE_DESC='ECS Task Role'
ECS_TASK_POLICY_NAME='orthos_project_ecs_performer'
ECS_TASK_POLICY_DESC='ECS Task Execution Policy'
ECS_TASK_ROLE_JSON={
    "Version": "2012-10-17",
    "Statement": [{
            "Sid": "",
            "Effect": "Allow",
            "Principal": {
                "Service": "ecs-tasks.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
ECS_TASK_POLICY_JSON={
    "Version": "2012-10-17",
    "Statement": [{
            "Effect": "Allow",
            "Action": [
                "ecr:GetAuthorizationToken",
                "ecr:BatchCheckLayerAvailability",
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        }
    ]
}
ECS_TASK_POLICY_ARN=f'arn:aws:iam::{ACCOUNT_ID}:policy/{ECS_TASK_POLICY_NAME}'
ECS_TASK_ROLE_ARN=f'arn:aws:iam::{ACCOUNT_ID}:role/{ECS_TASK_ROLE_NAME}'
ECS_CONTAINER_NAME='test-orthos'
ECS_TASK_DEFINITION_NAME='test-orthos'
ECS_TASK_DEFINITION_ARN=f'arn:aws:ecs:us-east-1:{ACCOUNT_ID}:task-definition/{ECS_TASK_DEFINITION_NAME}'
DOCKER_IMAGE_URI=f'{ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/{ECR_REPO_NAME}'
