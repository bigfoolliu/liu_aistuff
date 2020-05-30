#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
两个整数的最大公约数
"""


def max_common(a, b):
    while b:
        a, b = b, a % b
    return a


print(max_common(12, 24))
print(max_common(3, 8))
print(max_common(35, 7))
