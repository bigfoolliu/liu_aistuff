#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python实现单例
"""


class SingleItem(object):
    """通过重写__new__方法"""

    _instance = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__new__(cls)
        return cls._instance[cls]


def single_item(cls, *args, **kwargs):
    """通过闭包的方式"""
    isinstances = {}

    def get_instance():
        if cls not in isinstances:
            isinstances[cls] = cls(*args, **kwargs)
        return isinstances[cls]

    return get_instance


class A(SingleItem):

    def __init__(self, name, age=10):
        self.name = name
        self.age = age


a = A("jim")
b = A("tom")  # 第二次实例化会被忽略

print(a.name, a.age, b.name, b.age)
