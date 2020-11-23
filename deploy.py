import json
import boto3
import random
import os

stack_id = random.randint(0, 10000000000)

client = boto3.client('cloudformation')

template = {
    'Resources': {
        'S3Bucket': {
            'Type': 'AWS::S3::Bucket',
            'DeletionPolicy': 'Delete',
            'Properties': {
                'BucketName': 'throwaway-elasti-cd-{}'.format(stack_id)
            }
        }
    }
}

template_str = json.dumps(template)
account_id = boto3.client('sts').get_caller_identity().get('Account')
role_arn = 'arn:aws:iam::{}:role/cf-deployment-service'.format(account_id)
response = client.create_stack(
    StackName='throwaway-stack-{}'.format(stack_id),
    TemplateBody=template_str,
    RoleARN=role_arn
)
print(response)
