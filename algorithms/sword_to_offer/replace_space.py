#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
替换空格，将字符串中的空格替换为 20%
"""

import time


# 计算时间的装饰器
def count_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.clock()
        ret = func(*args, **kwargs)
        end_time = time.clock()
        print("spend_time:  %.40f ms" % ((end_time - start_time) * 1000))
        return ret

    return wrapper


# 方法一：直接使用内置方法
@count_time
def replace_space(target_str):
    """
    :params target_str: str
    return: str
    """
    new_str = target_str.replace(" ", "20%")
    return new_str


if __name__ == "__main__":
    test_str = "i love china,  haha"
    print(replace_space(test_str))
