#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
使用多进程中的管道,它是半双工的，读写方向不固定

- 只允许具有亲缘关系的两个进程通信
"""


import time
from multiprocessing import Pipe, Process


def func(conn1, conn2):
    conn2.close()  # 子进程只需使用connection1,故关闭connection2
    while True:
        try:
            msg = conn1.recv()  # 无数据则阻塞
            print(msg)
        except EOFError as e:  # 对端关闭后，就无法继续接收了
            print(e)
            conn1.close()
            break


def main():
    conn1, conn2 = Pipe()  # 建立一个管道,管道返回两个connection
    print(f'conn1: {conn1}, conn2, {conn2}')

    p = Process(target=func, args=(conn1, conn2,))
    p.daemon = True  # 子进程必须和主进程一同退出，防止僵尸进程
    p.start()

    conn1.close()  # 主进程只需要一个connection,故关闭一个
    for i in range(20):
        time.sleep(0.2)
        conn2.send('main text')  # 主进程发送
    conn2.close()  # 主进程关闭connection2


if __name__ == '__main__':
    main()
