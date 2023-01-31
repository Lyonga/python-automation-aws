#The first line imports the boto3 library.
#The next line creates a client object for the IAM service.
#The list_users method is called on the IAM client object to retrieve a list of IAM users in the AWS account.
#A variable "last_active_user" is set to the first user in the list of IAM users.
#The code then iterates through each IAM user in the list and prints their username and the date/time they last used their password.
#The code also checks if the current IAM user's last password use is more recent than the previous user and updates the "last_active_user" variable if needed.
#Finally, the code prints the user ID, username, and last password use date/time of the last active user.

import boto3

iam = boto3.client('iam')
iam_users = iam.list_users()

last_active_user = iam_users["Users"][0]

for iam_user in iam_users["Users"]:
    print(iam_user["UserName"])
    print(iam_user["PasswordLastUsed"])
    print("---------------------------")
    
    if last_active_user["PasswordLastUsed"] < iam_user["PasswordLastUsed"]:
        last_active_user = iam_user

print("Last active user:")
print(last_active_user["UserId"])
print(last_active_user["UserName"])
print(last_active_user["PasswordLastUsed"])

