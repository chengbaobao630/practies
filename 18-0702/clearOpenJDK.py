#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import pexpect
import paramiko
import re
username = "root"
host = "192.168.103."
port = 22
password = "Aa111111"
# prompt = ']#'
# sshNewKey = 'Are you sure you want to continue connecting'
removeCommand = "rpm -e --nodeps {0}"

if __name__ == '__main__':
    for x in (12, 42, 50):
        cuHost = host + str(x)
        print(cuHost)
        # child = pexpect.spawnu("ssh "+username+"@"+ip, maxread=2000)
        #
        # i = child.expect([prompt, 'assword:*', sshNewKey, pexpect.TIMEOUT,
        #             'key.*? failed'])
        # print(i)
        # child.send(password + "\r")
        #
        # # result = child.send("cat /etc/hosts" + "\r")
        #
        # result = child.send("hostnamectl set-hostname myCentos02.com" + "\r")
        #
        # print(result)

        # child.expect(prompt)
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(cuHost, port, username, password)

            # str_command = "hostnamectl set-hostname myCentos02.com"
            # stdin, stdout, stderr = ssh.exec_command(str_command)
            str_command = "rpm -qa|grep java"
            stdin, stdout, stderr = ssh.exec_command(str_command)
            result = stdout.read()
            print(str(result))
            openJDKs = re.findall(r"java-1.{0,10}-openjdk-.{0,30}_64", str(result))
            for openJDK in openJDKs:
                ssh.exec_command(removeCommand.format(openJDK))
        except Exception as error:
            print(error)
            print("error ip:{0}".format(cuHost))
            continue



