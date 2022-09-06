# How to create S3 Bucket

import boto3
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("cmilesluit1")
response = bucket.create(
    ACL='public-read', 
    
)

print(response)