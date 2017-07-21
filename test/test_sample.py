# -*- coding:utf-8

import unittest
from moto import mock_ec2, mock_s3
from aws_profile import get_client
from ec2 import list_ec2_instances
from s3 import s3_upload

class TestSample(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @mock_ec2
    def __moto_list_ec2_instances_setup(self):
        ec2 = get_client('ec2')
        reservation = ec2.run_instances(ImageId='ami-f00ba4', MinCount=1, MaxCount=1)
        self.instance_id = reservation['Instances'][0]['InstanceId']

    @mock_s3
    def __moto_s3_upload(self, bucket, key):
        s3 = get_client('s3')
        s3.create_bucket(Bucket=bucket)
        s3.put_object(Bucket=bucket, Key=key)

    @mock_ec2
    def test_get_client(self):
        ec2 = get_client('ec2')
        self.assertEqual(ec2._endpoint.host, 'https://ec2.ap-northeast-1.amazonaws.com')

    @mock_ec2
    def test_list_ec2_instances(self):
        #  mockup
        self.__moto_list_ec2_instances_setup()
        
        # execute test
        instances = [e for e in list_ec2_instances()]

        # assert
        self.assertEqual(len(instances), 1)
        self.assertEqual([self.instance_id], instances)

    @mock_ec2
    def test_s3_upload(self):
        bucket = 'dummy_bucket'
        key = 'README.md'

        #  mockup
        self.__moto_s3_upload(bucket, key)

        # execute test
        s3_upload(bucket, key)

        # assert
        s3 = get_client('s3')
        body = s3.get_object(Bucket=bucket, Key=key)['Body'].read().decode('utf-8').encode('utf-8')
        with open(key, 'r') as r:
            self.assertEqual(body, r.read())

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestSample))
    return suite
