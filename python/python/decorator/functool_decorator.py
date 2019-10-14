#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
使用functools.wraps()装饰函数，从而不影响函数

使用python -m pydoc functool_decorator查看该模块的帮助文档
"""
import time
import functools


def get_dura(wrapped):
    """获得函数的运行时间"""
    @functools.wraps(wrapped)
    def wrapper(*args, **kwargs):
        s_t = time.time()
        ret = wrapped(*args, **kwargs)
        print("spend time：{} s".format(time.time() - s_t))
        return ret
    return wrapper


@get_dura
def func():
    """睡眠时间"""
    time.sleep(3)


func()
