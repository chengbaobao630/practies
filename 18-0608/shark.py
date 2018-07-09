#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

while True:
    print(1)
    print(s.recvfrom(8090))
