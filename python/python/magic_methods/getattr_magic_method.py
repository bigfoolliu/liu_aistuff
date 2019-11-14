#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
- getattr函数获取实例的属性
- __getattr__，当调用的属性或者方法不存在的时候，该方法会被调用
"""


class A(object):

    def __init__(self, name):
        self.name = name
    
    def default_func(self):
        print("default func")
    
    def __getattr__(self, attr):
        return self.default_func


if __name__ == "__main__":
    a = A("jim")
    print(getattr(a, "name"))

    a.f1()  # 该方法不存在，调用默认方法
