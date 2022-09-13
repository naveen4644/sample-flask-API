
import boto3 
import json 

client = boto3.client('secretsmanager')

response = client.put_secret_value(
    SecretId='test',
    SecretString='{"db": "prod", "password": "hello-world-updated2"}'
)

print(response)