ACCOUNT_ID='892933193600'
ECR_REPO_NAME='flask_app'
ECS_CLUSTER_NAME='bstech'
ECS_TASK_ROLE_NAME='ECSTaskRole'
ECS_TASK_ROLE_DESC='ECS Task Role'
ECS_TASK_POLICY_NAME='ECSTaskExceutionPolicy'
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