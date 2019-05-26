#!/usr/bin/env python
#!coding:utf-8


"""
使用装饰器给函数来记录log
"""


def log_decorator(func):
    """增加日志信息的装饰器"""
    def add_info(*args, **kargs):
        print("[INFO]Function {} running with args {} and kargs {}.".format(func.__name__, args, kargs))
        return func(*args, **kargs)

    return add_info


@log_decorator
def func1():
    print("func1 run")

@log_decorator
def func2(*args):
    print("func2 run")

@log_decorator
def func3(*args, **kargs):
    print("func3 run")


func1()
func2(1, 2)
func3("a", name="tony")

