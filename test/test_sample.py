# -*- coding:utf-8

import unittest
from moto import mock_ec2
from aws_profile import get_client
from ec2 import list_ec2_instances

class TestSample(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @mock_ec2
    def __moto_setup(self):
        ec2 = get_client()
        reservation = ec2.run_instances(ImageId='ami-f00ba4', MinCount=1, MaxCount=1)
        self.instance_id = reservation['Instances'][0]['InstanceId']

    @mock_ec2
    def test_get_client(self):
        ec2 = get_client()
        self.assertEqual(ec2._endpoint.host, 'https://ec2.ap-northeast-1.amazonaws.com')

    @mock_ec2
    def test_list_ec2_instances(self):
        self.__moto_setup()
        instances = [e for e in list_ec2_instances()]
        self.assertEqual(len(instances), 1)
        self.assertEqual([self.instance_id], instances)

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestSample))
    return suite
