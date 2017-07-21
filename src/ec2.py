# -*- coding:utf-8

import boto3
from aws_profile import get_client

def list_ec2_instances():
    response = get_client().describe_instances()
    if response:
        for res in response.get('Reservations', []):
            for instance in res.get('Instances', []):
                yield instance['InstanceId']
