#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
工厂模式python实现
"""


class Person(object):

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight


class Male(Person):

    def __init__(self, name, height=None, weight=None, **kwargs):
        super(Person).__init__(height, weight)
        self.name = name
        self.__dict__.update(kwargs)


class Female(Person):

    def __init__(self, name, height=None, weight=None, **kwargs):
        super(Person).__init__(height, weight)
        self.name = name
        self.__dict__.update(kwargs)


class Factory(object):

    """实现工厂模式的类"""

    @staticmethod
    def get_person(name, gender):
        """只要根据gender参数就可以实现不同的对象构建"""
        if gender == 'M':
            return Male(name)
        if gender == 'F':
            return Female(name)


if __name__ == '__main__':
    factory = Factory()
    person = factory.get_person("ll", "F")
