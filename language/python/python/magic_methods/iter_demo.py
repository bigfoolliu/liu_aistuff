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

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 1000000000000000000000000000000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值


if __name__ == "__main__":
    fib = Fib()

    n = 0
    for i in fib:  # 每遍历一次都会执行一次fib.__next__()方法
        if n == 10:
            break
        print(i)
        n += 1
