import boto3

s3_resource=boto3.client('s3') 

#delete single object
s3_resource.delete_object(Bucket="cmiles-luit",
    key='uploadtest.png')
    
    
#delete multiple objects
import os
import glob

#find all objects from bucket
objects=s3_resource.list_objects(Bucket="cmiles-luit")["contents"]
len(objects)
for object in objects:
    print(object['key'])