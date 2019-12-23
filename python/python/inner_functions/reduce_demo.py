#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python reduce函数实例

reduce(function, sequence, initial)

- reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])：计算的就是((((1+2)+3)+4)+5)
- python2是内置函数
- python3是functools模块中的函数

返回的是一个具体的值
"""


from functools import reduce


def simle_demo():
    """reduce最简单的展示"""
    l = [1, 2, 3, 4, 5]
    ret = reduce(lambda x,y: x*y, l)  # 进行阶乘
    print(ret)


def demo2():
    """reduce将一个整数列表转换为一个整数"""
    l = [1, 2, 3, 4, 5]
    ret = reduce(lambda x,y:x*10+y, l)
    print(ret)


def demo3():
    """reduce函数初始值"""
    l = [1, 2, 3, 4, 5]
    ret = reduce(lambda x,y: x*10+y, l, 666)  # 设置初始值，作为第一个元素执行
    print(ret)


if __name__ == "__main__":
    simle_demo()
    demo2()
    demo3()
