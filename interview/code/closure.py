#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
闭包的最基本实现
"""

def my_add(num1):
    def real_add(num2):
        return num1 + num2
    return real_add


p = my_add(1)

print(p(2))
assert p(2) == 3

