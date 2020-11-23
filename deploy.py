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
region = os.environ.get('AWS_REGION')
role_arn = 'arn:aws:iam::{}:role/cf-deployment-service'.format(region)
response = client.create_stack(
    StackName='throwaway-stack-{}'.format(stack_id),
    TemplateBody=template_str,
    RoleARN=role_arn
)
print(response)
