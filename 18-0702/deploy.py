#!/usr/bin/python
# -*- coding: UTF-8 -*-
import paramiko
import sys
import os

username = "root"
host = "192.168.115.15"
port = 22
password = "Aa111111"
server = {
    "center": "192.168.115.2"
}

if __name__ == '__main__':
    application = sys.argv[1]
    applicationPath = sys.argv[2]
    realFile = "{0}/{1}/build/libs/*.jar".format(application, applicationPath)
    print(application)
    print(applicationPath)
    print(realFile)
    try:
        t = paramiko.Transport((cuHost, port))
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)

        s = sftp.put(realFile, "/application/java/")

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)
        str_command = "/application/java/bootSh.sh stop finance"
        stdin, stdout, stderr = ssh.exec_command(str_command)
        result = stdout.read()
        print(str(result))
    except Exception as error:
        print(error)
        print("error ip:{0}".format(host))
    finally:
        sys.exit("finished")




