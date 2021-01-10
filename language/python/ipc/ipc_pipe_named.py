#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
使用FIFO（命名管道）来实现任意两个进程间的通信

特点：

1. 和无名管道一样，半双工
2. 每个FIFO管道都与一个路径名相关联，类似一个文件
3. 进程间通过读写FIFO来通信
4. 这种方式对子进程的生命周期管理并不方便，不建议在python中使用
"""


import os
import time


PIPE_NAME = 'pipe'


def child_process():
    """子进程, 负责写"""
    pipe_out = os.open(PIPE_NAME, os.O_WRONLY)  # 只写模式
    count = 0
    while count < 10:
        print(f'write {count}')
        os.write(pipe_out, f'number:{count}'.encode('utf-8'))  # 非阻塞的
        count += 1
        time.sleep(1)


def parent_process():
    """父进程，负责读"""
    # pipe_in = os.open(PIPE_NAME, 'r')

    fd = os.open(PIPE_NAME, os.O_RDONLY)  # 只写模式, 获取一个file descriptor

    while True:
        line = os.read(fd, 20)  # 每次读20个字节，读出后FIFO管道中会马上清楚数据
        parent_id = os.getpid()
        cur_time = time.time()

        if line:
            print(f'parent {parent_id} get line {line} at {cur_time}')
        else:
            print(f'parent {parent_id} get None')

        time.sleep(1)


def main():
    if not os.path.exists(PIPE_NAME):
        os.mkfifo(PIPE_NAME)

    p_id = os.fork()

    if p_id:
        parent_process()
    else:
        child_process()


if __name__ == "__main__":
    main()
