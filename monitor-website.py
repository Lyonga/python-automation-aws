#This script monitors the status of an application hosted on a Linode server. It uses the requests library to send an HTTP GET request to the application and check the response status code. 
#If the response status code is not 200 (OK), it means the application is down.

#The script then sends an email notification about the down status of the application using the smtplib library and the email login credentials stored as environment variables.

#If the connection to the application results in an error, the script restarts the container running the application. 
#If the container restart doesn't fix the issue, the script restarts the whole Linode server and then the container.

#The script runs the monitor_application() function every 5 minutes using the schedule library.


import requests
import smtplib
import os
import paramiko
import linode_api4
import time
import schedule

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
LINODE_TOKEN = os.environ.get('LINODE_TOKEN')


def restart_server_and_container():
    # restart linode server
    print('Rebooting the server...')
    client = linode_api4.LinodeClient(LINODE_TOKEN)
    nginx_server = client.load(linode_api4.Instance, 24920590)
    nginx_server.reboot()

    # restart the application
    while True:
        nginx_server = client.load(linode_api4.Instance, 24920590)
        if nginx_server.status == 'running':
            time.sleep(5)
            restart_container()
            break


def send_notification(email_msg):
    print('Sending an email...')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"Subject: SITE DOWN\n{email_msg}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)


def restart_container():
    print('Restarting the application...')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='139.162.130.236', username='root', key_filename='/Users/nanajanashia/.ssh/id_rsa')
    stdin, stdout, stderr = ssh.exec_command('docker start c3e706bc905e')
    print(stdout.readlines())
    ssh.close()


def monitor_application():
    try:
        response = requests.get('http://li1388-236.members.linode.com:8080/')
        if response.status_code == 200:
            print('Application is running successfully!')
        else:
            print('Application Down. Fix it!')
            msg = f'Application returned {response.status_code}'
            send_notification(msg)
            restart_container()
    except Exception as ex:
        print(f'Connection error happened: {ex}')
        msg = 'Application not accessible at all'
        send_notification(msg)
        restart_server_and_container()


schedule.every(5).minutes.do(monitor_application)

while True:
    schedule.run_pending()
