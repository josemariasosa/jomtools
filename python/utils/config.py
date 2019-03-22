#!/usr/bin/env python
# -*- coding: utf-8 -*-
AWS_S3 = {
    "URL": "https://s3-us-west-1.amazonaws.com",
    "ACCESS_KEY": "AKIAJBH3X7QANI37WWJA",
    "SECRET_KEY": "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",
    "BUCKET": "rigs-ebay-csv",
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
    "FROM": "empresa@rigs.com.mx",
}

SLACK = {
    "URL": "https://hooks.slack.com/services/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"
}
