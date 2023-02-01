#This is a Python script to validate the deployment of a containerized application on an EC2 instance. 
#The script sets the EC2 server hostname and host port from the environment variables and waits for 15 seconds to allow the application to start up. 
#Then it sends a GET request to the application URL (hostname:host port) and checks if the status code of the response is 200 (success). 
#If the status code is 200, it prints "Application is running successfully!"; otherwise, it prints "Application deployment was not successful". 
#If any connection error occurs, it prints "Connection error happened" followed by the error message, and "Application not accessible at all".

from wsgiref.util import request_uri
import requests
import time
import os

ssh_host = os.environ['EC2_SERVER']
host_port = os.environ['HOST_PORT']

# Validate the application started successfully
try:
    # give the app some time to start up
    time.sleep(15)
    
    response = requests.get(f"http://{ssh_host}:{host_port}")
    if response.status_code == 200:
        print('Application is running successfully!')
    else:
        print('Application deployment was not successful')
except Exception as ex:
    print(f'Connection error happened: {ex}')
    print('Application not accessible at all')
