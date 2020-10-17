#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python multiprocessing模块使用的示例

官方文档：
https://docs.python.org/zh-cn/3/library/multiprocessing.html
"""


import multiprocessing
import time
from multiprocessing import Pipe, Pool, Process, Queue


def time_counter(f):
    """计算耗时装饰器"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        ret = f(*args, **kwargs)
        print("cost time:{} s".format(time.time()-start_time))
        return ret
    return wrapper


def func_square(x):
    """
    计算平方任务
    :param x: int
    :return: int
    """
    time.sleep(2)
    return x*x


def func_hello(name):
    """
    say hello任务
    :param name: str
    :return:
    """
    time.sleep(2)
    print("hello, {}".format(name))


def func_use_queue(q):
    """
    将数据存入队列，便于进程通信
    :param q: Queue
    :return:
    """
    q.put([1, "a", None])


def basic_demo():
    """
    简单示例
    """
    # 计算当前计算机的cpu核心数量
    print("cpu number:", multiprocessing.cpu_count())  # 8


@time_counter
def pool_demo():
    """
    使用进程池进行并行计算
    """
    pool = Pool()
    print(pool.map(func_square, [1, 3, 4]))


@time_counter
def process_demo():
    """产生一个单独的进程进行运算"""
    process = Process(target=func_hello, args=["tony",])
    process.start()
    # join之后会阻塞至该任务完成之后再执行后面的任务,没有该句则会直接执行后面的
    process.join()
    print("end")


@time_counter
def queue_demo():
    """
    使用multiprocessing中的Queue进行数据共享示例
    """
    # 队列是进程和线程安全的
    queue = Queue()
    process = Process(target=func_use_queue, args=[queue,])
    process.start()
    print("get from queue:{}".format(queue.get(timeout=2)))
    process.join()


def pipe_demo():
    """
    使用multiprocessing中的Pipe进行数据共享示例
    """
    pass


if __name__ == "__main__":
    basic_demo()
    # pool_demo()
    # process_demo()
    # queue_demo()
    # TODO:
    pass
