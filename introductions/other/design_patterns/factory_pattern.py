#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
工厂模式python实现
"""


class Person(object):

    def __init__(self,height,weight):
        self.height = height
        self.weight = weight

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight


class Male(Person):

    def __init__(self, name):
        print("Hello Mr." + name)


class Female(Person):

    def __init__(self, name):
        print("Hello Miss." + name)


class Factory(object):
    
    def getPerson(self, name, gender):
        if gender == 'M':
            return Male(name)
        if gender == 'F':
            return Female(name)


if __name__ == '__main__':
    factory = Factory()
    person = factory.getPerson("ll", "F")
