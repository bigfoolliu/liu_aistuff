#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
gc模块示例

- python gc模块介绍: https://blog.csdn.net/qq_38260497/article/details/87879064
- gc模块提供一个接口给开发者设置垃圾回收的选项

gc.enable()
gc.disable()
gc.isebabled()
gc.collec([generation])
gc.set_debug(flags)
gc.get_debug()
gc.get_objects()

gc.is_tracked(obj)
gc.get_count()
gc.get_threadshold()
"""


import gc


def basic_demo():
    pass


def collect_demo():
    """
    显式进行垃圾回收的示例
    """
    pass


if __name__ == "__main__":
    pass

