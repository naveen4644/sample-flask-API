from aws_resources import ecr
from aws_resources import ecs

ecr.create_repo()
ecs.create_cluster()
