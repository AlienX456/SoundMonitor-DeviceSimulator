import os
import boto3
from botocore.exceptions import ClientError


class AwsS3Resource:
    def __init__(self):
        session = boto3.Session()
        s3 = session.resource('s3')
        self.bucket = s3.Bucket(os.environ['S3_BUCKET'])

    def uploadData(self, file_name, object_s3_name, metadata):
        try:
            self.bucket.upload_file(file_name, object_s3_name,
                                    ExtraArgs=metadata)
        except ClientError as e:
            return False
