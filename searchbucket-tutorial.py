# How to search S3 Bucket

import boto3
resource=boto3.resource("s3")
for bucket in resource.buckets.all():
    print(bucket.name)
    
bucket_list = list(resource.buckets.all())
print(len(bucket_list))