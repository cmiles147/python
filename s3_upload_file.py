import boto3

#How to upload single file
s3_resource=boto3.client("s3")
s3_resource.upload_file(
   Filename="beach.png",
   Bucket="cmiles-luit",
   Key="uploadtest.png")
   
#How to upload multiple files
import os
import glob

cwd=os.getcwd()
cwd=cwd+"/upload/"
files=glob.glob(cwd+"*.png")

for file in files:
   s3_resource=boto3.client("s3")
   s3_resource.upload_file(
   Filename=file,
   Bucket="cmiles-luit",
   Key=file.split("/"))
