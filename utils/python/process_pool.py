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
        po.apply_async(task, (i,))  # apply_asyc使用非阻塞方式调用函数
    print("------start------")
    po.close()  # 关闭进程池，不再接受新的任务(po.terminate则是不管任务是否完成，立即终止)
    po.join()  # 主进程阻塞，等待子进程退出，必须在close和terminate之后使用
    print("------end--------")
