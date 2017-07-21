# -*- coding:utf-8

from boto3.session import Session

def get_client():
    return Session().client('ec2')
    #return Session(profile_name='<profile_name_here>').client('ec2')
