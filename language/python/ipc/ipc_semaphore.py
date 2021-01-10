#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
进程间通信：信号量

特点：

- 不传输数据，用于多进程的同步
"""


import multiprocessing
from multiprocessing import Semaphore
import time


def consumer(s: Semaphore):
    """消费者"""
    s.acquire()
    print(multiprocessing.current_process().name + '正在执行')
    time.sleep(2)
    s.release()
    print(multiprocessing.current_process().name + 'release')


def main():
    s = multiprocessing.Semaphore(5)
    for i in range(5):
        p = multiprocessing.Process(target=consumer, args=(s,))
        p.daemon = True  # 跟随主进程死亡
        p.start()

    time.sleep(3)
    print(f'main end')


if __name__ == "__main__":
    main()
