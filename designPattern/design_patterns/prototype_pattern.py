#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
原型设计模式python实现
"""


import copy


class Prototype(object):

    """实现原型设计模式的类"""

    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        """注册方法,用来追踪已经创建的对象"""
        self.objects[identifier] = obj
    
    def un_register(self, identifier):
        del self.objects[identifier]
    
    def clone(self, identifier, **kwargs):
        """核心方法，用来克隆已经存储的对象"""
        is_found = self.objects.get(identifier)
        if not is_found:
            raise ValueError(f'{identifier} not correct')
        obj = copy.deepcopy(self.objects[identifier])
        obj.__dict__.update(kwargs)
        return obj


class Book(object):

    def __init__(self, name, author, **kwargs):
        self.name = name
        self.author = author
        self.__dict__.update(kwargs)
    
    def __str__(self):
        _list = []
        for i in self.__dict__.keys():
            _list.append(f'{i}:{self.__dict__[i]}')
        return ' '.join(_list)


if __name__ == "__main__":
    book1 = Book('book1', 'tony', price=100)

    prototype = Prototype()
    cid = 'id1'
    prototype.register(cid, book1)

    book2 = prototype.clone(cid, price=120)

    for i in (book1, book2):
        print(i)
