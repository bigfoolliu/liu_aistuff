#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
vars内置函数

返回对象的属性和属性值的字典对象
"""


class Demo(object):
    """doc"""
    name = "demo class"


def basic_demo():
    print(vars())
    print(type(vars()))

    print(vars(Demo))
    print(vars(Demo()))


if __name__ == "__main__":
    basic_demo()
