#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""进程池"""
import multiprocessing
import time
import os
import random


def task(msg):
    t_start = time.time()
    print("begin task {}, id is {}".format(msg, os.getpid()))
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print("end task {}, spend time {}".format(msg, t_stop - t_start))


if __name__ == "__main__":
    po = multiprocessing.Pool(3)
    for i in range(0, 10):
        po.apply_async(task, (i,))
    print("------start------")
    po.close()
    po.join()
    print("------end--------")
