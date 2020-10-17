#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Process使用

- 生成进程
"""

import os
from multiprocessing import Process


def info(title):
    print(title)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    print()


def f(name):
    info('function f')
    print('hello', name)


if __name__ == '__main__':
    f('anna')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
