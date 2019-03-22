#!/usr/bin/env python
# coding=utf-8

import os
import configparser
from pymongo import MongoClient

_parser = configparser.ConfigParser()
_parser.read_file(open(os.path.expanduser(os.environ['RIGS_SETTINGS'])))

_general = _parser["general"]
_environment = _parser["facturbo"]["env"]

_database = _parser[("database %s" % _environment)]
_mongo_uri = "mongodb://%s:%s@%s:%s" % (_database["user"],
                                        _database["password"],
                                        _database["socket"],
                                        _database["port"])

_config = {
    "AWS_BUCKET_NAME": "rigs-business-invoices",
    "OFFICE_ZIP_CODE": "44160",
    "PAYMENT_FORM": "03",       # <---- Payment Form is a Default Value: Transferencia Electronica.
    "PAYMENT_METHOD": "pue",
    "FIXED_DECIMALS": "2",
    "FIXED_CURRENCY": "mxn",
    "TAX_RATE": 0.16,
    "TAX_NAME": "iva",
    "IS_RETENTION": "false",
    "UNIT": "pieza",
    "UNIT_CODE": "h87",
    "PRODUCT_CODE": "25174800",
    "DEFAULT_DISCOUNT": "0.0",
    "DEFAULT_NAME_ID": "1",
    "DEFAULT_CFDI_TYPE": "i",
    "DEFAULT_INVOICE_TYPE": "g01"
}

env_config = {
    "development": {
        "IS_SANDBOX": True,
        "API_URL": "https://apisandbox.facturama.mx/cfdi/{}/issued/{}",
        "API_URL_2": "https://apisandbox.facturama.mx/2/cfdis",
        "API_CLIENT": "https://apisandbox.facturama.mx/Client",
        "API_EMAIL": "https://apisandbox.facturama.mx/Cfdi?cfdiType=issued&cfdiId={}&email={}&subject={}&comments={}",
        "KEYS": ("josemariarigs", "XeNas9nmTO8V")
    },
    "production": {
        "IS_SANDBOX": False,
        "API_URL": "https://www.api.facturama.com.mx/cfdi/{}/issued/{}",
        "API_URL_2": "https://www.api.facturama.com.mx/2/cfdis",
        "API_CLIENT": "https://www.api.facturama.com.mx/Client",
        "API_EMAIL": "https://www.api.facturama.com.mx/Cfdi?cfdiType=issued&cfdiId={}&email={}&subject={}&comments={}",
        "KEYS": ("rigstechnology", "bM8#mw18bn1$fo*")
    }
}

_config.update(env_config[_environment])

_mongo_client = MongoClient(_mongo_uri)
db_rigs = _mongo_client["rigs"]
db_business = _mongo_client["business"]
db_ecommerce = _mongo_client["ecommerce"]
