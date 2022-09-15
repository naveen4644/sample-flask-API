from http import client
import boto3
client = boto3.client('route53')

response = client.change_resource_record_sets(
    HostedZoneId='Z096818425BO6XYDPHPY9',
    ChangeBatch={
        'Comment': 'string',
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'Name': 'test.orthos.cloud.',
                    'Type': 'CNAME',
                    'TTL': 300,
                    'ResourceRecords': [
                        {
                            'Value': 'test-othos-lb-905887803.us-east-1.elb.amazonaws.com'
                        },
                    ],
                    
                }
            },
        ]
    }
)