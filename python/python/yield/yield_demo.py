#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python yield的使用
"""


def generator1(n=3):
    """自定义生成器"""
    yield  # 类似于return None
    for i in range(n):
        yield i  # 类似于return i
        print("haha")
        yield n
    yield "over"


def yield_demo1():
    """yield使用1"""
    a = generator1()
    try:
        for m in range(100):  # 为了让迭代结束
            print(next(a))
    except StopIteration:
        print("iter is over")


if __name__ == "__main__":
    yield_demo1()
