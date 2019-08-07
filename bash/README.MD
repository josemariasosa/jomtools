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

