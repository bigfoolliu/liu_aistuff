#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python map函数实例

map(function, iterable)

- python2返回一个列表
- python3返回一个map可迭代对象
"""


def simple_demo():
    """map最基础的展示"""
    l = [1, 2, 3, 4, 5]
    ret = map(lambda x: x * 2, l)  # 对可迭代对象中的每一个元素进行操作
    print(ret, list(ret))


def multi_params():
    """map传入多个可迭代对象作为参数"""
    l1 = ["a", "b"]
    l2 = ["c", "d", "e", "f"]
    ret = map(lambda x, y: x + y, l1, l2)  # 当内部的元素数量不同的时候，python3中按最短的处理
    print(ret, list(ret))


def use_own_func():
    """使用自定义的函数，而不是匿名函数"""

    def add(x):
        return x + 1

    l = [1, 2, 3]
    ret = map(add, l)
    print(ret, list(ret))


if __name__ == "__main__":
    simple_demo()
    multi_params()
    use_own_func()
