#!/usr/bin/env python3
# -*- coding:utf-8  -*-
# author: bigfoolliu


"""
sys模块
"""


import sys


def basic_demo():
    # 获取对象的引用计数
    a = "hahaha"
    print(sys.getrefcount(a))


if __name__ == "__main__":
    basic_demo()

