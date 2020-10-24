#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


import socket

# 设置需要监听的ip和端口
target_host = 'www.baidu.com'
target_port = 443

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)  # ipv4, tcp
server.connect((target_host, target_port))

server.send(b'GET / HTTP1.1\r\nHost:www.baidu.com')
response = server.recv(1024)

print(f'response: {response}')
