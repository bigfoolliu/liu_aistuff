#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
print函数展示
"""
import time


def end_demo():
    """print结尾控制，加flush强制刷新"""
    for i in range(100):
        print("#", end="", flush=True)
        time.sleep(0.01)
    print()


def progress_demo():
    """使用\r展示进度"""
    days = 365
    for i in range(days):
        print("\r", "progress:{}%".format(round((i+1)*100/days)), end="", flush=True)
        time.sleep(0.01)
    print()


def sep_demo():
    """使用sep参数将结果使用指定分隔符分割"""
    print("name", "age", "score", sep=" | ")


def sysout_demo():
    """将print的默认输出改到指定文件，而不是默认的屏幕"""
    f = open("print_demo.log", "w")
    print("hello, this is print demo.", file=f)
    print("hello, this is print demo again.", file=f)
    f.close()


if __name__ == "__main__":
    # end_demo()
    # progress_demo()
    sep_demo()
    sysout_demo()
