#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


"""
回调函数的原理
"""
import threading
import time


def callback(ret):
    print("callback run, ret: {}".format(ret))


def long_io(callback):
    def func(callback):
        print("start long io")
        time.sleep(5)
        ret = "longio ret"
        print("end long io")
        callback(ret)
    a = threading.Thread(target=func, args=(callback,))
    a.start()


def missionA():
    print("start a")
    long_io(callback)
    print("end a")


def missionB():
    print("start b")
    time.sleep(2)
    print("end b")


if __name__ == "__main__":
    start_time = int(time.time())
    missionA()
    missionB()
    print("cost_time: {}".format(int(time.time()) - start_time))
    while True:
        time.sleep(1)
