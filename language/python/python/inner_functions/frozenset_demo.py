#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
返回一个冻结的集合，冻结后的集合不能增加或者删除任何元素
frozenset(iterable)
"""


def test1():
    a = frozenset()  # 创建一个空的frozenset集合
    b = frozenset(range(10))
    print(type(a), a)
    print(type(b), b)

    print(b[2])


if __name__ == "__main__":
    test1()
