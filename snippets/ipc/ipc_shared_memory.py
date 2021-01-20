#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
进程间通信之---共享内存

特点：

1. 最快的IPC方式
2. 因为多个进程可以同时操作，所以需要进行同步
3. 可通过与信号量或锁结合使用实现多个进程间同步

共享方案:
a. 消息队列
b. 文件映射（为了在进程间共享内存，内核专门留有一个内存区，主进程将需要共享的数据映射到这块内存中，其他进程访问这个共享内存）
"""


from typing import List
from multiprocessing import Process, Queue, Semaphore, current_process, Manager
import time


s = Semaphore(2)
global_list = list(range(5))  # 进程之间不共享内存，所以每个进程访问的是这个对象的副本，非同一个对象


def change_global_list(global_list: List, s: Semaphore):
    """子进程"""
    s.acquire()
    print(f'process_id: {current_process()} before change: {global_list}')

    global_list.pop()
    time.sleep(5)

    s.release()
    print(f'process_id: {current_process()} after change: {global_list}')


def main():
    manager = Manager()
    print(dir(manager))

    global_list = manager.list()
    global_list.extend(list(range(5)))

    for i in range(5):
        p = Process(target=change_global_list, args=(global_list, s,))
        p.daemon = True
        p.start()

    time.sleep(10)  # 等一下子进程
    print('process end')


if __name__ == "__main__":
    main()
