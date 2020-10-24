#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


import socket
import threading

# 设置需要监听的ip和端口
bind_ip = '0.0.0.0'
bind_port = 9999

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)  # ipv4, tcp
server.bind((bind_ip, bind_port))

# 设置最大连接为3
server.listen(3)

print(f'listening on {bind_ip}:{bind_port}')


def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f'receive {request}')
    client_socket.send(b'ACK')

    client_socket.close()


while True:
    # 启动监听，当一个客户端连接成功的时候将客户端套接字对象保存到client
    client, addr = server.accept()
    print(f'accept connection from {addr[0]},{addr[1]}')
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
