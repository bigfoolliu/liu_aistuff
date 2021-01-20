#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python实现心跳机制

- 使用socket实现
- 固定时间的下客户端给服务的端发送消息，出现异常便会抛出异常

客户端代码
"""

import socket
import time


def client_heart_beat():
    a = 0
    while True:
        time.sleep(4)  # 最好要小于服务端你的超时时间，否则会报异常
        a += 1
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 9999))
        msg = "已连接" + str(a * 4) + "秒"
        print(f'连接成功，发送消息: {msg}')
        s.send(msg.encode('utf-8'))  # 如果报错就把 'UTF-8' 去掉


def main():
    print('准备开始连接...')
    client_heart_beat()


if __name__ == '__main__':
    main()
