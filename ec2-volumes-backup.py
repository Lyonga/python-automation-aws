#creates snapshots of EC2 volumes in the "eu-west-3" region that are tagged with the name "prod". The schedule library is used to run the create_volume_snapshots function once a day. 

import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="eu-west-3")


def create_volume_snapshots():
    volumes = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['prod']
            }
        ]
    )
    for volume in volumes['Volumes']:
        new_snapshot = ec2_client.create_snapshot(
            VolumeId=volume['VolumeId']
        )
        print(new_snapshot)


schedule.every().day.do(create_volume_snapshots)

while True:
    schedule.run_pending()
