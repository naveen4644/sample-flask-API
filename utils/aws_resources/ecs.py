import boto3
from values import ECS_CLUSTER_NAME

client = boto3.client('ecs')

def create_cluster():
    try:
        response = client.create_cluster(
            clusterName=ECS_CLUSTER_NAME
        )
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return True
        else:
            return False
    except Exception as e:
        print(str(e))
        return False

def delete_cluster():
    try:
        response = client.delete_cluster(
            clusterName=ECS_CLUSTER_NAME
        )
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return True
        else:
            return False
    except Exception as e:
        print(str(e))
        return False
