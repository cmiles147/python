import boto3

client=boto3.client('ec2')

response = client.delete_vpc(
    VpcId='vpc-066329595805d09b9',)
    
print(response)