#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""进程池中的队列Queue"""
import os
import multiprocessing
import time


def write(q):
    print("write {} start, father process is {}".format(os.getpid(), os.getppid()))
    for i in "python":
        q.put(i)


def read(q):
    print("read {} start, father process is {}".format(os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print("read msg from Queue: {}".format(q.get(True)))


if __name__ == "__main__":
    print("process {} start".format(os.getpid()))
    q = multiprocessing.Manager().Queue()
    po = multiprocessing.Pool()
    po.apply_async(write, args=(q,))
    time.sleep(2)
    po.apply_async(read, args=(q,))
    po.close()
    po.join()

    print("process {} ends".format(os.getpid()))
