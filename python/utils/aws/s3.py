#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.config import AWS_S3
from httplib import OK
import boto3
import os
import re
import requests


class S3():
    def __init__(self):
        self.url = AWS_S3["URL"]
        self.access_key = AWS_S3["ACCESS_KEY"]
        self.secret_key = AWS_S3["SECRET_KEY"]
        self.bucket = AWS_S3["BUCKET"]
        self.permissions = AWS_S3["PERMISSIONS"]

    def upload_file(self, file_path, file_name):
        s3 = boto3.resource('s3',
                            aws_access_key_id=self.access_key,
                            aws_secret_access_key=self.secret_key)

        result = s3.meta.client.upload_file(file_path,
                                            self.bucket,
                                            file_name,
                                            ExtraArgs=self.permissions)

        file_url = "{}/{}/{}".format(self.url, self.bucket, file_name)
        response = requests.head(file_url)

        if response.status_code != OK:
            return False

        return file_url
