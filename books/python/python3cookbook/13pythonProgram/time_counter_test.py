#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
调用一次 perf_counter()，从计算机系统里随机选一个时间点A，
计算其距离当前时间点B1有多少秒。当第二次调用该函数时，
默认从第一次调用的时间点A算起，距离当前时间点B2有多少秒。
两个函数取差，即实现从时间点B1到B2的计时功能。

一般来说， 使用 time.time()
或 time.clock() 计 算 的 时 间 精 度 因 操 作 系 统 的 不 同 会 有 所 不 同。 而 使 用
time.perf_counter() 函数可以确保使用系统上面最精确的计时器。
"""

import time

class Timer(object):

    def __init__(self, func=time.perf_counter):
        self.cost_time = 0.0
        self._start = None  # running flag
        self._func = func
    
    def start(self):
        if self._start is not None:
            raise RuntimeError("Already started")
        self._start = self._func()  # 记录当前时间

    def stop(self):
        if self._start is None:
            raise RuntimeError("Timer has not started")
        end = self._func()
        self.cost_time = end - self._start
        self._start = None
    
    @property
    def running(self):
        return self._start is not None

    def reset(self):
        self.cost_time = 0.0
    
    def __enter__(self):
        self.start()
        return self
    
    def __exit__(self, *args):
        self.stop()


def main():
    t = Timer()

    t.start()
    for i in range(1000000):
        i = i + 1
    t.stop()
    print(t.cost_time)


    # 使用__enter__和__exit__定义了该类在上下文中的行为
    t = Timer(time.process_time)
    with t:
        for i in range(1000000):
            i = i + 1
    print(t.cost_time)


if __name__ == "__main__":
    main()
