#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
实现__call__方法让类可调用并实现一个类装饰器
"""


# class Hello(object):
# 
#     def __call__(self):
#         print("hello, __call__")
# 
# 
# # 使用callable()函数可以知道对象是否可以被调用
# print(callable(Hello))
# # 实例化并调用类
# hello = Hello()
# hello()


import time
import functools


class DelayFunc(object):

    """延迟函数装饰器，使用其装饰后的函数每次执行前都会等待额外的时间"""

    def __init__(self, duration, func):
        """
        duration: 延时的秒数
        func: 待装饰的函数
        """
        self.duration = duration
        self.func = func
    
    def __call__(self, *args, **kwargs):
        """每次调用就会延时的接口"""
        print("will wait for {} seconds..".format(self.duration))
        time.sleep(self.duration)
        return self.func(*args, **kwargs)
    
    def eager_all(self, *args, **kwargs):
        """直接执行不等待的接口"""
        print("no delay")
        return self.func(*args, **kwargs)


def delay(duration):
    """具体要使用时候的装饰器"""
    return functools.partial(DelayFunc, duration)


@delay(duration=2)
def add(a, b):
    return a + b


# 这次调用将会延迟
print(add(1, 2))
# 这次执行将会立即执行
print(add.eager_all(1, 2))

