#!/usr/bin/env python
# -*- coding: utf-8 -*-
AWS_S3 = {
    "URL": "https://s3-us-west-1.amazonaws.com",
    "ACCESS_KEY": "A************************A",
    "SECRET_KEY": "j*******************************9",
    "BUCKET": "my_bucket",
    "PERMISSIONS": {"ACL": "public-read"}
}

# Confiure the SMTP server host & credentials
MAIL = {
    "SERVICE": "smtp",
    "SERVER": "localhost",
    "PORT": 25,
    "AUTH": False,
    "USERNAME": "",
    "PASSWORD": "",
    "FROM": "empresa@ejemplo.com.mx",
}

SLACK = {
    "URL": "https://hooks.slack.com/services/*****************************w"
}
