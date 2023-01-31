#connect to the Amazon EC2 service and retrieve a list of all subnets in your account. 
#Then, it will loop through the subnets and print the SubnetId of the subnet which is marked as the default subnet for its availability zone.

import boto3

ec2 = boto3.client('ec2')
subnets = ec2.describe_subnets()
for subnet in subnets["Subnets"]:
    if subnet["DefaultForAz"]:
        print(subnet["SubnetId"])

