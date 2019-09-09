#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket

BUF_SIZE = 1024
host = 'localhost'
port = 8083
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)  # 接收的连接数
client, address = server.accept()  # 因为设置了接收连接数为1，所以不需要放在循环中接收

# 循环收发数据包，长连接
while True:
    data = client.recv(BUF_SIZE)
    print(data.decode())
