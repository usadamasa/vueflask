import boto3
from boto3.session import Session


class S3Client(object):
    def __init__(self, profile: str, bucket: str):
        self._profile = 'vueflasksample'
        self._session = Session(profile_name=self._profile)
        self._resource = self._session.resource('s3')
        self._bucket = self._resource.Bucket(bucket)


    def getList(self, path:str):
        obj = self._bucket.Object('sample.txt').get()
        print(obj['LastModified'])
        return obj['LastModified']
