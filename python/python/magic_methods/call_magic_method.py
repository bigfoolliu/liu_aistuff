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


if __name__ == "__main__":
    a = A(12)
    a(23)  # 直接调用实例
