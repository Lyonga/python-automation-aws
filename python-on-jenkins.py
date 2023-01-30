# Install Python inside Jenkins server
apt-get install python3
apt-get install pip
pip install boto3
pip install paramiko
pip install requests

# Create credentials in Jenkins 
"jenkins_aws_access_key_id" - Secret Text
"jenkins_aws_secret_access_key" - Secret Text
"ssh-creds" - SSH Username with private key
"ecr-repo-pwd" - Secret Text

# NOTE: you will have to approve usage of "split" function in script. You will see the link to approval inside the build console logs






# In jenkins folder, you will find the Jenkinsfile that executes 3 python scripts for different stages:
- get-images.py
- deploy.py
- validate.py

# Before executing the Jenkins pipeline, set the following environment variable values inside Jenkinsfile
- ECR_REPO_NAME
- EC2_SERVER
- ECR_REGISTRY
- CONTAINER_PORT
- HOST_PORT
- AWS_DEFAULT_REGION


