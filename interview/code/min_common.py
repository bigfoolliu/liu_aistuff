#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
求最小公倍数
"""


def min_common(a, b):
    c = a*b
    while b:
        a, b = b, a%b
    print(a)
    return c//a  # c整除a,a是a和b的最大公约数


print(min_common(1, 3))
print(min_common(2, 9))
print(min_common(6, 24))

