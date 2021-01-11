#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu



"""
threading模块基础使用
"""


import threading
from threading import Thread
import time


def target_func(n: int):
    """线程目标任务"""
    for i in range(n):
        time.sleep(0.5)
        cur_thread_name = threading.current_thread().name
        print(f'{cur_thread_name} {i}')


class ThreadFactory:
    """线程工厂"""
    @classmethod
    def create_thread(cls) -> Thread:
        t = Thread(target=target_func, args=(5,))
        return t


def single_thread_demo(is_daemon: bool=False, timeout: float=0):
    """
    单个子线程示例
    :param is_daemon: 是否设置线程为守护线程，设置为守护线程，则无论该子线程是否结束，主线程结束则该子线程结束
    :param timeout: 线程阻塞时间, 到达阻塞时间之后线程才向下执行, 设置为0则直至子线程结束才向下执行
    """
    print('主线程启动')

    t = ThreadFactory.create_thread()
    t.daemon = is_daemon
    t.start()

    t.join(timeout=timeout)  # 阻塞,阻塞时间为1秒，超过1秒，则向下执行，子线程执行结束，程序退出

    print('主线程结束')


def multi_thread_demo():
    """多子线程示例"""
    print('主线程启动')

    thread_list = []

    for i in range(3):
        t = ThreadFactory.create_thread()
        thread_list.append(t)

    for t in thread_list:
        t.start()

    print('主线程结束')


def main():
    # single_thread_demo()
    multi_thread_demo()


if __name__ == "__main__":
    main()
