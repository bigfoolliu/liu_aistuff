#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
原型设计模式python实现
"""


import copy


class Prototype(object):

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
        object.__dict__.update(kwargs)
        return obj
