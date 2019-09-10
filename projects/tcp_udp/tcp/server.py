#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
import threading
import time
from socketserver import BaseRequestHandler, ThreadingTCPServer

BUF_SIZE=1024


class Handler(BaseRequestHandler):

    def setup(self):
        pass

    def handle(self):
        address, pid = self.client_address
        print('address: {} pid: {}!'.format(address, pid))
        try:
            data = self.request.recv(1024).decode("utf-8").split(":")
            worker_id, wokrer_ip = data[0], data[1]
            print("id ip", worker_id, wokrer_ip)
        except IndexError:
            print('disconnect from {}'.format(self.client_address))
            return

        while True:
            # 持续监听
            data = self.request.recv(BUF_SIZE)
            if len(data)>0:
                print('receive data: {}'.format(data.decode('utf-8')))
                self.request.sendall('response'.encode('utf-8'))
                print("id ip", worker_id, wokrer_ip)
            else:
                # 发送空数据来断开连接
                print('disconnect from {}'.format(self.client_address))
                print("id ip", worker_id, wokrer_ip)
                break

    def finish(self):
        pass


if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 8998
    ADDR = (HOST, PORT)
    server = ThreadingTCPServer(ADDR, Handler)  # 参数为监听地址和已建立连接的处理类
    print('listening')
    server.serve_forever()  # 监听，建立好TCP连接后，为该连接创建新的socket和线程，并由处理类中的handle方法处理
    print("--------------------------")
    print(server)
