#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
使用Python的魔术方法来求解斐波那契数列
"""


class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 1000000000000000000000000000000:  # 退出循环的条件
            raise StopIteration();
        return self.a  # 返回下一个值


i = 0
fib = Fib()
while i < 100:
    print(fib.next())
    i += 1
