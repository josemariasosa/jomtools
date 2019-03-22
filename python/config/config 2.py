#!/usr/bin/env python
# coding=utf-8

import os
import configparser
from pymongo import MongoClient

_parser = configparser.ConfigParser()
_parser.read_file(open(os.path.expanduser(os.environ['RIGS_SETTINGS'])))

_general = _parser["general"]

_database = _parser[("database %s" % _general["env"])]
_mongo_uri = "mongodb://%s:%s@%s:%s" % (_database["user"],
                                        _database["password"],
                                        _database["socket"],
                                        _database["port"])

_mongo_client = MongoClient(_mongo_uri)
db_rigs = _mongo_client["rigs"]

