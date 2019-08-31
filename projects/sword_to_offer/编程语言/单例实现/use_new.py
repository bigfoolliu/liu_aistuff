#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
使用__new__方法实现单例模式
"""


class SingleTon(object):

    """继承该父类的类都是单例类,即重写类的new方法"""

    _instance = {}  # 用来保存自己类的实例

    def __new__(cls, *args, **kwargs):
        # 如果没有创建过该实例则创建一个自身的实例
        if cls not in cls._instance:
            cls._instance[cls] = super().__new__(cls)
        return cls._instance[cls]


class Tony(SingleTon):

    class_val = "class_method"

    def __init__(self, name):
        self.name = "tony"
    
    def print_name(self):
        print(self.name)
    
    @staticmethod
    def print_staic():
        print("static method")
    
    @classmethod
    def print_classmethod(cls):
        print(cls.class_val)


if __name__ == '__main__':
    tony = Tony("tony")
    jim = Tony("jim")
    print(tony is jim)
    print(tony.name)
    print(jim.name)

    tony.print_name()
    jim.print_name()

    tony.print_staic()
    jim.print_staic()

    tony.print_classmethod()
    jim.print_classmethod()
