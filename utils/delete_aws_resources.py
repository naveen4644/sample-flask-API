from aws_resources import ecr
from aws_resources import ecs

ecr.delete_repo()
ecs.delete_cluster()
