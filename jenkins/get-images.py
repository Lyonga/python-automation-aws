#The script starts by importing the required modules (boto3 and os) and setting the repository name as an environment variable.
# The ECR client is then initialized with the boto3 client, and the describe_images method is used to retrieve the list of images in the repository.

#The image details are looped through and the first image tag of each image is appended to the image_tags list. 
#Finally, the script loops through the image tags list and prints each tag to the console.

import boto3
import os

repo_name = os.environ['ECR_REPO_NAME']

ecr_client = boto3.client('ecr')

# Fetch all 3 images from ECR repo
images = ecr_client.describe_images(repositoryName=repo_name)

image_tags = []
for image in images['imageDetails']:
    image_tags.append(image['imageTags'][0])

for tag in image_tags:
    print(tag)
