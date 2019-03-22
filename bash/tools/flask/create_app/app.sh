#!/bin/bash
printf "
 WSGI & Flask API Creator
"

if [[ $# -eq 0 ]]; then
printf "Help: set of utilities to perform operations on RIGS Business system
Options:
  -a, --app        Python application name, ex: open_search
  -n, --name       Name of the application, ex: Open Search
  -d, --database   Mongo database name
"
exit
fi

while [[ $# -gt 0 ]]
do
key="$1"
case $key in
  -a|--app) application=$2; shift;;
  -n|--name) app_name=$2; shift;;
  -d|--database) database=$2; shift;;
esac
shift
done 

SECRET_KEY="wqe2e2wsq"
ROOT_PATH="/Users/josemaria/data_projects"
APP_NAME="$(echo "$application" | awk '{print toupper($0)}')"
PYTHON_APP_PATH=$application/app
CONFIG_PATH=$PYTHON_APP_PATH/conf
MODULE_PATH=$PYTHON_APP_PATH/modules
ENVAR="ENVIRONMENT"
ENVAR_LOCAL="${APP_NAME}_LOCAL"
ENVAR_STAGING="${APP_NAME}_STG"
ENVAR_PRODUCTION="${APP_NAME}_PROD"
HOME_MODULE="home"

printf "Application settings:

ROOT_PATH        = ${ROOT_PATH}
APP_NAME         = ${APP_NAME}
PYTHON_APP_PATH  = ${PYTHON_APP_PATH}
CONFIG_PATH      = ${CONFIG_PATH}
MODULE_PATH      = ${MODULE_PATH}
ENVAR            = ${ENVAR}
ENVAR_LOCAL      = ${ENVAR_LOCAL}
ENVAR_STAGING    = ${ENVAR_STAGING}
ENVAR_PRODUCTION = ${ENVAR_PRODUCTION}
HOME_MODULE      = ${HOME_MODULE}

-------------------------------------------

Application Architecture

- app.wsgi
- app/__init__.py
- app/application.py
- app/modules/__init__.py
- app/modules/home.py


-------------------------------------------

Virtual Env

-------------------------------------------

Git Configuration

A inital commit is performed and the following branches are created:
- master
- staging
- develop
"

# Create app wsgi
cd $ROOT_PATH && pwd;
mkdir -p $application;
touch $application/app.wsgi &&
printf "#!/usr/bin/python
import sys
import logging
import os


activate_this = '/var/www/${PYTHON_APP_PATH}/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

logging.basicConfig(stream=sys.stderr)

path = '/var/www/${application}/'
if path not in sys.path:
    sys.path.append(path)

path = '/var/www/${PYTHON_APP_PATH}'
if path not in sys.path:
    sys.path.append(path)

from app import application
application.secret_key = '${SECRET_KEY}'" >> $application/app.wsgi;

# # Setup python application 
# mkdir -p $PYTHON_APP_PATH &&
# touch $PYTHON_APP_PATH/application.py && touch $PYTHON_APP_PATH/__init__.py;
# printf "# -*- encoding: utf-8 -*-
# import os
# from flask import Flask
# from flask_cors import CORS
# from modules.${HOME_MODULE} import ${HOME_MODULE}


# application = Flask(__name__)

# CORS(application, origins=application.config['CORS_ORIGINS'])

# application.register_blueprint(${HOME_MODULE}, url_prefix='/${HOME_MODULE}')

# if __name__ == '__main__':
#     application.run(port=application.config['PORT'])
# " >> $PYTHON_APP_PATH/application.py &&

# printf "from application import application


# if __name__ == '__main__':
#     application.run(port=application.config['PORT'])
# " >> $PYTHON_APP_PATH/__init__.py

# # Create home module
# # - expose GET /home enpoint
# touch $MODULE_PATH/${HOME_MODULE}.py
# printf "# -*- encoding: utf-8 -*-
# from flask import Blueprint
# from httplib import OK
# import json

# ${HOME_MODULE} = Blueprint('${HOME_MODULE}', __name__)


# @${HOME_MODULE}.route('/', methods=['GET'])
# def get():
#     return json.dumps({'message': 'hello world!'}), OK
# " >> $MODULE_PATH/${HOME_MODULE}.py;


# # Setup virtual environment
# {
#   cd $PYTHON_APP_PATH && pwd && 
#   /usr/local/bin/virtualenv venv && eval "source venv/bin/activate" &&
#   curl "https://bootstrap.pypa.io/get-pip.py" | python &&
#   pip install flask &&
#   pip install flask_cors &&
#   pip install flask_pymongo &&
#   pip freeze >> requirements.txt &&
#   # python __init__.py
#   deactivate;
# } || {
#   echo "Virtual env creation fail"
# }

# # Init git repo and commit the basic files tree
# git init &&
# git config --local user.name "${app_name}"
# echo "venv" >> .gitignore &&
# git add . &&
# git commit -m "Added: basic files tree" &&
# git checkout -b staging &&
# git checkout master &&
# git checkout -b develop
