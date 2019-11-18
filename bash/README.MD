# Bash

[TOC]

## Shebangs

```bash
#!/usr/bin/env bash
```

## Basic and Fast Commands

### 1. Curl

Get the header of a curl request:

```bash
curl -I https://s3-us-west-1.amazonaws.com/rigs-images/multi0.jpg

# HTTP/1.1 200 OK
# x-amz-id-2: MqWfAIkhfLgvwM5wI6heCR60KhZFEKUNW2/tUaed4rtk5T0FpktwgyFWHuh0RpIFJwUReh0/4PU=
# x-amz-request-id: BAEC323D42C0B97E
# Date: Tue, 28 May 2019 15:02:08 GMT
# Last-Modified: Tue, 28 May 2019 14:51:38 GMT
# ETag: "28fa12a7b7e55c6049182c502589438a"
# Accept-Ranges: bytes
# Content-Type: image/jpeg
# Content-Length: 819961
# Server: AmazonS3
```

## How to Create and Use Symbolic Links

More on this topic, refer [this article](https://www.howtogeek.com/297721/how-to-create-and-use-symbolic-links-aka-symlinks-on-a-mac/).

Symbolic links, also known as symlinks, are special files that point to files or directories in other locations on your system. You can think of them like advanced aliases and here’s how to use them in MacOS.

Symbolic links are similar to aliases, except they work in every application on your Mac—including in the Terminal.

### Create Symbolic Links

Run the `ln` command in the following form. You can specify either a path to a directory or file:

```bash
ln -s /path/to/original /path/to/link
```

The -s here tells the ln command to create a symbolic link. If you want to create a hard link, you’d omit the -s. Most of the time symbolic links are the better choice, so don’t create a hard link unless you have a specific reason for doing so.

If your file path contains spaces or other special characters, you’ll need to enclose it in quotation marks. So, if you wanted to create a link on your desktop to a folder named “My Files” inside your user directory, you’d need something like the following command:

```bash
ln -s "/Users/name/My Files" "/Users/name/Desktop/My Link"
```

If you need to create a symbolic link in a system location your user account doesn’t have access to, you’ll need to prefix the ln command with the sudo command, like so:

```bash
sudo ln -s /path/to/original /path/to/link
```

### Delete Symbolic Links

You can delete symbolic links like you would any other type of file. For example, to delete a symbolic link in Finder, `Ctrl+click` or right-click it and select “Move to Trash”.

You can delete links from the command line using the `rm` command, which is the same command you’d use to remove other files. Run the command and specify the path to the link you want to delete:

```bash
rm /path/to/link
```

## Homebrew

### Install Homebrew

The missing package manager for macOS (or Linux) — [Homebrew](https://brew.sh/).

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

## Install the `tree` command for Mac

```bash
brew install tree
```

Print the folder and file structure with tree.

```bash
> tree .
.
├── README.md
├── aws
│   ├── README.md
│   └── lambda
│       └── lambda_function_1.py
├── bash
│   ├── README.MD
│   ├── template
│   │   ├── bash_profile.sh
│   │   └── credentials.txt
│   └── tools
│       ├── flask
│       │   └── create_app
│       │       └── app.sh
│       └── mirefaccion
│           └── import_export_mongo
│               ├── README.md
│               ├── db
│               └── docs
│                   └── db
│                       ├── export.txt
│                       └── import.txt
├── git
│   ├── README.md
│   └── template
│       └── gitignore.txt
├── ide
│   └── sublime
│       └── README.md
├── javascript
│   └── README.MD
├── mongo
│   └── README.MD
└── python
    ├── README.md
    ├── exercises
    │   ├── 1-grocery-list-price.py
    │   └── 2-grocery-list-price-stock.py
    ├── pandas
    │   └── README.MD
    ├── utils
    │   ├── __init__.py
    │   ├── aws
    │   │   ├── __init__.py
    │   │   └── s3.py
    │   ├── config.py
    │   ├── mail.py
    │   └── slack.py
    └── xml
        └── xml2json.py

23 directories, 27 files
```

Removing a folder from a tree command. For example, avoiding the venv to be printed.

```bash
> tree -I venv
.
├── config
│   ├── __pycache__
│   │   └── selection.cpython-37.pyc
│   └── selection.py
├── core
│   ├── __pycache__
│   │   ├── calculus.cpython-37.pyc
│   │   ├── generator.cpython-37.pyc
│   │   └── runners.cpython-37.pyc
│   ├── calculus.py
│   ├── generator.py
│   └── runners.py
├── db
│   ├── __pycache__
│   │   ├── businessunit.cpython-37.pyc
│   │   ├── connection.cpython-37.pyc
│   │   ├── organization.cpython-37.pyc
│   │   ├── revs.cpython-37.pyc
│   │   └── site.cpython-37.pyc
│   ├── businessunit.py
│   ├── connection.py
│   ├── organization.py
│   ├── revs.py
│   └── site.py
├── helper
│   ├── __pycache__
│   │   ├── counter.cpython-37.pyc
│   │   └── z.cpython-37.pyc
│   ├── counter.py
│   └── z.py
└── main.py

8 directories, 23 files
```

## Generate some alias

```bash
export LSCOLORS=ExFxBxDxCxegedabagacad
alias ls='ls -GFh'
alias random_music='cd /Users/josemaria/Dropbox/albums_to_have && ls > all_files && sort -R all_files | head -n 10 && rm all_files && cd -'
```

## Config file in a server

It is useful to have in any server a centralized file with all the credentials. For example, in the dataserv the credentials file was located in `~/.rigs/credentials`. The contend of the file looks as follows:

```text
[general]
env = staging
test = True
notification = True
s3_key_id = A***********************
s3_secret = A***********************
s3_bucket = elasticbeanstalk-us-west-1-687111944639

[database local]
socket = localhost
port = 27017
user = master
password = A***********************
auth = True

[database development]
socket = localhost
port = 27017
user = master
password = A***********************
auth = True

[database staging]
socket = ec2-54-193-83-156.us-west-1.compute.amazonaws.com
port = 33033
user = master
password = A***********************
auth = True
```

## Cron job in a server

The software utility cron is a time-based job scheduler in Unix-like computer operating systems. People who set up and maintain software environments use cron to schedule jobs to run periodically at fixed times, dates, or intervals.

To open the current cron jobs in a server use:

```bash
crontab -e
```

**Warning:** Be careful not to run the later command without the `-e`. This action would delete all your current commands.

For some examples on the cron job scheduling, visit [crontab.guru](https://crontab.guru/).

### Crontab examples:

```bash
0 17 * * 4  cd /root/nps_gen; bash main.sh; cd -
0 4 * * *  cd /root/strong_arm/_multi_tools/4_discounts && bash main.sh && cd -
```

## Moving files from a local machine to a remote server

`scp` allows files to be copied to, from, or between different hosts. It uses ssh for data transfer and provides the same authentication and same level of security as ssh. One application of this command is to move files from a Digital Ocean Droplet to my local machine.

```bash
scp username@droplet_ip:/path/to/file /path/to/destination
```

Running a command on your local computer to upload files to your server is pretty easy on macOS or Linux where you can use scp:

```bash
scp -r /path/to/my/files root@:0.0.0.0:/path/on/my/server
```

### SCP examples:

```bash
scp root@192.241.193.129:/root/strong_arm/_insert_products/dataPool/type_1/gates_2018_10_03.json ./gates_2018_10_03.json 
```

## Basic file and directory processing

### 1. Remove all directories with an specific name.

In this first example, the requirement was to eliminate all the files within multiple directories having the same name `venv`, within a root directory.

```bash
sudo find . -name "*venv*" -type d > temp; for line in $(cat temp); do rm -rf $line; done
```

### 2. Check if a directory exists

To check if a directory exists in a shell script you can use the following:

```bash
if [ -d "$DIRECTORY" ]; then
  # Control will enter here if $DIRECTORY exists.
fi
```

Or to check if a directory doesn't exist:

```bash
if [ ! -d "$DIRECTORY" ]; then
  # Control will enter here if $DIRECTORY doesn't exist.
fi
```

### Epoch & Unix Timestamp Conversion Tools
 
The current Unix epoch time is: `1574113549`.

For more info, check: https://www.epochconverter.com/.


#### How to get the current epoch time

**Python:**

```py
    import time; time.time()
```

**Unix/Linux Shell:**

```bash
date +%s
```

#### Convert from human-readable date to epoch

**Python:**

```py
import calendar, time
calendar.timegm(time.strptime('2000-01-01 12:34:00', '%Y-%m-%d %H:%M:%S'))
```

**Unix/Linux Shell:**

```bash
date -d @1520000000
```

Replace 1520000000 with your epoch, needs recent version of 'date'. Replace '-d' with '-ud' for GMT/UTC time.

#### Convert from epoch to human-readable date

**Python:**

```py
import time
time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(epoch))
```

Replace `time.localtime` with `time.gmtime` for GMT time.

Or using `datetime`:

```py
import datetime
datetime.datetime.utcfromtimestamp(epoch).replace(tzinfo=datetime.timezone.utc)
```

**Unix/Linux Shell:**

```sh
date +%s -d"Jan 1, 1980 00:00:01"
```

Replace `-d` with `-ud` to input in GMT/UTC time.

### Grep

When you want to avoid all python files in the tree notation.

```bash
tree -I venv . | grep --invert-match -E "__|cpython"
```