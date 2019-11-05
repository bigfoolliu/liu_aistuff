#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python3 添加进度条效果

参考：https://blog.csdn.net/qq_33472765/article/details/82940843
"""


import time
from tqdm import tqdm


def demo1():
    """
    最基本的进度条效果
    """
    for i in tqdm(range(100)):
        time.sleep(0.01)
    return


def demo2():
    """
    添加描述和不同的样式
    """
    for i in tqdm(range(100), ascii=True, desc="Progress bar"):
        time.sleep(0.01)
    return


def demo3():
    """
    """
    text = ""
    for char in tqdm(["a", "b", "c", "d"]):
        time.sleep(0.25)
        text += char


def demo4():
    """
    为每一个进度条添加描述
    """
    pbar = tqdm(["a", "b", "c", "d"])
    for char in pbar:
        time.sleep(0.1)
        pbar.set_description("progress %s" % char)


if __name__ == "__main__":
    print("------------demo1--------------")
    demo1()
    print("------------demo2--------------")
    demo2()
    print("------------demo3--------------")
    demo3()
    print("------------demo4--------------")
    demo4()
