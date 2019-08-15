#!/usr/bin/env bash

PROJECT_NAME=$1;
PROJECT_LOC=$PWD"/"$PROJECT_NAME
CONFIG_FILE="/Users/josemaria/Maria/Rever/templates/config.py"
BASH_MAIN="/Users/josemaria/Maria/Rever/templates/main.sh"

if [ ! -d "$PROJECT_LOC" ]; then
    echo "Creating new python3 project in location:"
    echo "---> "$PROJECT_LOC

    # Create file structure
    mkdir $PROJECT_LOC
    mkdir $PROJECT_LOC"/pyFiles"
    mkdir $PROJECT_LOC"/data"
    cd $PROJECT_LOC
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install pymongo pandas configparser
    deactivate
    cp $BASH_MAIN ./main.sh
    
    cd ./pyFiles
    cp $CONFIG_FILE ./config.py
    curl https://raw.githubusercontent.com/josemariasosa/rubik/master/rubik/rubik.py > rubik.py
    touch main.py

    cd ../
    sublime .

    echo "Done!"

else
    echo "ERROR: The project name is already taken!"
fi
