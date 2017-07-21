# -*- coding:utf-8

from boto3.session import Session

def get_client(_type):
    return Session().client(_type)
    #return Session(profile_name='<profile_name_here>').client(_type)
