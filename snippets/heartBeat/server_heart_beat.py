#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python实现心跳机制

- 使用socket实现
- 固定时间的下客户端给服务的端发送消息，出现异常便会抛出异常

服务端代码
"""


import socket
import datetime


start_time = None
end_time = None


def server_heart_beat():
    """
    服务端接收心跳函数
    """
    global start_time, end_time
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9999))
    s.listen(2)  # 同时监听两个

    s.settimeout(None)
    conn, addr = s.accept()
    start_time = datetime.datetime.now()
    while True:
        try:
            s.settimeout(5)  # 超过这个时间就会包异常
            conn, addr = s.accept()
            print(f'client addr: {addr}')  # 打印客户端的地址

            client_msg = conn.recv(1024)  # 客户端发送过来的消息
            print(f'client msg: {str(client_msg)}')  # 'utf-8'
        except Exception as e:
            end_time = datetime.datetime.now()
            _seconds = (end_time - start_time).seconds
            print(f'连接已断开，本次连接持续 {_seconds} 秒')
            print(f'异常情况: {e}')
            break


def main():
    print('开始监听: 127.0.0.1:9999...')
    server_heart_beat()


if __name__ == '__main__':
    main()
