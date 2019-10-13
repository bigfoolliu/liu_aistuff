#!/usr/bin/env python
#!coding:utf-8


"""
python3的环境

添加进度条效果
"""


from tqdm import tqdm
import time


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


demo1()
demo2()
demo3()
demo4()

