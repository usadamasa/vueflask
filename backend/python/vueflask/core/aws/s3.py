import boto3
from boto3.session import Session


class S3Client(object):
    def __init__(self, profile: str, bucket: str):
        self._profile = 'vueflasksample'
        self._session = Session(profile_name=self._profile)
        self._client = self._session.client('s3')
        self._bucket_name = bucket


    def getList(self, prefix:str):
        response = self._client.list_objects(
            Bucket= self._bucket_name,
            Prefix = prefix)
        if 'Contents' in response:  # 該当する key がないと response に 'Contents' が含まれない
            keys = [content['Key'] for content in response['Contents']]
            return keys
