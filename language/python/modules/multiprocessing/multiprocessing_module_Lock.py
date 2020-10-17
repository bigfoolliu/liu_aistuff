#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Lock对象

- 可以使用锁来确保一次只有一个进程操作资源
- 不使用锁的时候，多进程的的输出容易混淆
"""

import time
from multiprocessing import Process, Lock
from pudb import set_trace


def f(lock, i):
    set_trace()
    time.sleep(1)
    lock.acquire()
    try:
        print('hello world', i)
    finally:
        lock.release()


if __name__ == '__main__':
    _l = Lock()
    for num in range(5):
        Process(target=f, args=(_l, num)).start()
