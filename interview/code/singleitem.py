#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
写一个单例父类
"""
class SingleItem(object):

    _instance = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__new__(cls)
        return cls._instance[cls]


class A(SingleItem):

    def __init__(self, name, age=10):
        self.name = name
        self.age = age


a = A("jim")
b = A("tom")  # 第二次实例化会被忽略

print(a.name, a.age, b.name, b.age)
