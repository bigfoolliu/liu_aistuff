#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
享元模式python实现
"""


from enum import Enum


TreeTypes = Enum('')


class Tree(object):

    pool = dict()

    def __new__(cls, tree_type):
        obj = cls.pool.get(tree_type, None)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj
