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
    for x in (26, ):
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
        str_command = "cat /etc/hosts"
        stdin, stdout, stderr = ssh.exec_command(str_command)
        result = stdout.read()
        print(result)
        # ssh.close()

        try:
            t = paramiko.Transport((cuHost, port))
            t.connect(username=username, password=password)
            sftp = paramiko.SFTPClient.from_transport(t)

            # # 上传文件
            # sftp.put("/home/application/user.db", "/data/user/user.db")
            # # 下载文件
            # sftp.get("/data/user/test.db", "/home/application/test.db")
            # # 创建目录
            # sftp.mkdir("/home/userdir", "0755")
            # # 删除目录
            # sftp.rmdir("/home/userdir")
            # # 文件重命名
            # sftp.rename("/home/test.sh", "/home/testfile.sh")
            # # 打印文件信息
            # print(sftp.stat("/home/testfile.sh"))
            # # 打印目录列表
            s = sftp.put("/Users/chengcheng/Downloads/jdk-8u172-linux-x64.tar", "/usr/local/jdk-8u172-linux-x64.tar")
            print(s)
            tarJdkCommand = "cd /usr/local/ && tar -xvf /usr/local/jdk-8u172-linux-x64.tar &&" \
                            " rm /usr/local/jdk-8u172-linux-x64.tar && mv jdk1.8.0_172 jdk8"
            stdin, stdout, stderr = ssh.exec_command(tarJdkCommand)
            result = stdout.read()
            # print(result)
            jdkProfileCommand = """ echo  '#java environment
            export JAVA_HOME=/usr/local/jdk8
            export CLASSPATH=.:${JAVA_HOME}/jre/lib/rt.jar:${JAVA_HOME}/lib/dt.jar:${JAVA_HOME}/lib/tools.jar
            export PATH=$PATH:${JAVA_HOME}/bin' >> /etc/profile"""
            stdin, stdout, stderr = ssh.exec_command(jdkProfileCommand)
            result = stdout.read()
            # print(result)
            testJavaCommand = "javac"
            stdin, stdout, stderr = ssh.exec_command(testJavaCommand)
            result = stdout.read()
            print(result)
            # print(sftp.listdir("/home"))
        except Exception as error:
            print(error)
            print("error ip : {0}".format(cuHost))
            continue
        finally:
            t.close()
            ssh.close()
            # print(123)

