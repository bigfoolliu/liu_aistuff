#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


import socket

target_host = '127.0.0.1'
target_port = 111

client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # udp

client.sendto(b'hello', (target_host, target_port))
data, addr = client.recvfrom(4096)
print(data, addr)
