#!/usr/bin/env python
# coding=utf-8

import os
import configparser
from pymongo import MongoClient

_env = 'api-prod-env'

_parser = configparser.ConfigParser()
_parser.read_file(open(os.path.expanduser(os.environ['REVER_SETTINGS'])))

_general = _parser['general']

db_connection = {}
for _env in ['api-prod-env', 'log-prod-env']:
    _database = _parser[('database {}'.format(_general[_env]))]
    _mongo_uri = 'mongodb://{}:{}@{}:{}/{}'.format(_database['user'],
                                                _database['pass'],
                                                _database['socket'],
                                                _database['port'],
                                                _database['database'])
    _mongo_client = MongoClient(_mongo_uri)

    db_connection.update({
        _env: _mongo_client[_database['database']]
    })