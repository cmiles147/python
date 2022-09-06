# How to get Creation Date for S3 Bucket

import boto3
s3_resource=boto3.client("s3")
s3_resource.list_buckets()["Buckets"][1]["Name"]
creation_date=s3_resource.list_buckets()["Buckets"][1]["CreationDate"]
creation_date.strftime("%m%d%y_%H:%M:%S")
for bucket in s3_resource.list_buckets()["Buckets"]:
    print(bucket["Name"])
    print(bucket["CreationDate"])
    