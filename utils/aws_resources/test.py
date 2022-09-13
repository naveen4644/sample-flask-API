import boto3
client = boto3.client('elbv2')

response = client.describe_load_balancers(
     Names=[
        'test-othos-lb',
    
     ]
)
print(response['LoadBalancers'][0]['LoadBalancerArn'])