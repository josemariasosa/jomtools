# Bash

[TOC]

## Shebangs

```
#!/usr/bin/env bash
```

## Basic and Fast Commands

### 1. Curl

Get the header of a curl request:

```
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

## Config file in a server

It is useful to have in any server a centralized file with all the credentials. For example, in the dataserv the credentials file was located in `~/.rigs/credentials`. The contend of the file looks as follows:

```
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

[database production]
socket = ec2-54-193-14-48.us-west-1.compute.amazonaws.com
port = 27017
user = master
password = A***********************
auth = True

[hooks]
general = https://hooks.slack.com/services/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
business = https://hooks.slack.com/services/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
developers = https://hooks.slack.com/services/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

[aws]
default_region = us-west-1
ses_region = us-east-1
aws_access_key_id = A***********************
aws_secret_access_key = A***********************
```

## Cron job in a server

The software utility cron is a time-based job scheduler in Unix-like computer operating systems. People who set up and maintain software environments use cron to schedule jobs to run periodically at fixed times, dates, or intervals.

To open the current cron jobs in a server use:

```
crontab -e
```

**Warning:** Be careful not to run the later command without the `-e`. This action would delete all your current commands.

For some examples on the cron job scheduling, visit [crontab.guru](https://crontab.guru/).

### Crontab examples:

```
0 17 * * 4  cd /root/nps_gen; bash main.sh; cd -
0 4 * * *  cd /root/strong_arm/_multi_tools/4_discounts && bash main.sh && cd -
```

## Moving files from a local machine to a remote server

`scp` allows files to be copied to, from, or between different hosts. It uses ssh for data transfer and provides the same authentication and same level of security as ssh. One application of this command is to move files from a Digital Ocean Droplet to my local machine.

```
scp username@droplet_ip:/path/to/file /path/to/destination
```

Running a command on your local computer to upload files to your server is pretty easy on macOS or Linux where you can use scp:

```
scp -r /path/to/my/files root@:0.0.0.0:/path/on/my/server
```

### SCP examples:

```
scp root@192.241.193.129:/root/strong_arm/_insert_products/dataPool/type_1/gates_2018_10_03.json ./gates_2018_10_03.json 
```

## Basic file and directory processing

### 1. Remove all directories with an specific name.

In this first example, the requirement was to eliminate all the files within multiple directories having the same name `venv`, within a root directory.

```
sudo find . -name "*venv*" -type d > temp; for line in $(cat temp); do rm -rf $line; done
```

