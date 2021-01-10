#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python进程间通信

队列实现
"""


from multiprocessing import Process, Queue
import time
from typing import NoReturn
from doctest import testmod



def process_read(q: Queue) -> NoReturn:
    """
    读进程

    >>> 
    """
    while True:
        time.sleep(0.5)
        v = q.get(True)
        if v:
            print(f'Get {v}')
        else:
            print('Get None')


def process_write(q: Queue) -> NoReturn:
    """
    写进程

    >>>
    """
    for i in range(5):
        q.put(i)
        print(f'Put {i}')


def main():
    q = Queue()
    p1 = Process(target=process_write, args=(q,))
    p2 = Process(target=process_read, args=(q,))

    p1.start()
    p2.start()

    p1.join()  # 等待队列创建完毕

    while not q.empty():
        time.sleep(1)

    p2.terminate()


if __name__ == "__main__":
    main()
