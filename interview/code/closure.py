#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
闭包的最基本实现
"""


def my_add(num1):
    def real_add(num2):
        # 内函数引用了外函数的临时变量
        return num1 + num2
    return real_add


p = my_add(1)  # p结果为real_add

print(p(2))  # 2传给了num2
assert p(2) == 3
