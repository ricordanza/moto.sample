# -*- coding:utf-8

import boto3
import os.path
from aws_profile import get_client

def s3_upload(bucket, file):
	key = os.path.basename(file)
	get_client('s3').upload_file(file, bucket, key)

# if __name__ == '__main__':
#     s3_upload('<my_bucket>', '<my_file>')
