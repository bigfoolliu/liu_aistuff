#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
为了让对象实例能够被直接调用，需要实现call方法
"""


class A(object):

    def __init__(self, a):
        """a:int"""
        self.__a = a

    def show(self):
        print("a:{}".format(self.__a))

    # def __call__(self, num):
    #     """num:int"""
    #     print("ret: {}".format(self.__a + num))


class B(object):

    def __init__(self, b):
        self.__b = b
    
    def __call__(self):
        print(f'b: {self.__b}')


if __name__ == "__main__":
    a = A(12)

    b = B(23)
    b()  # 直接调用实例, 和下面的方法等价
    b.__call__()
