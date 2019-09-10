#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket,sys
HOST = 'localhost'
PORT = 8998
ADDR =(HOST,PORT)
BUFSIZE = 1024

sock = socket.socket()
try:
    sock.connect(ADDR)
    print('have connected with server')

    while True:
        data = input("input:")
        if len(data)>0:
            print('send:',data)
            sock.sendall(data.encode('utf-8')) #不要用send()
            recv_data = sock.recv(BUFSIZE)
            print('receive: {}'.format(recv_data.decode('utf-8')))
        else:
            sock.close()
            break
except Exception as e:
    print("error: {}".format(e))
    sock.close()
    sys.exit()
