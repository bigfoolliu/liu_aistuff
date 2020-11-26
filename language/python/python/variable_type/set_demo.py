#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python 集合操作
"""


def basic_demo():
    # 集合的推导式
    a = {1, 3, 4, 5, 6, 7}
    print(a)
    a = {x for x in a if x % 2 == 0}
    print(a)


if __name__ == "__main__":
    basic_demo()
