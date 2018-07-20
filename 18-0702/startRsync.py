#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import pexpect
import paramiko


username = "root"
host = "192.168.115."
port = 22
password = "Aa111111"
# prompt = ']#'
# sshNewKey = 'Are you sure you want to continue connecting'


if __name__ == '__main__':
    for x in (4, 6, 7, 10, 11, 12, 13, 14, 15, 21, 22, 23, 25, ):
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

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(cuHost, port, username, password)

        # str_command = "hostnamectl set-hostname myCentos02.com"
        # stdin, stdout, stderr = ssh.exec_command(str_command)
        installRsync = """rsync --daemon --config=/usr/local/rsync/rsync.conf"""
        stdin, stdout, stderr = ssh.exec_command(installRsync)
        ssh.close()
