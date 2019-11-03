#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python zi函数实例

zip(iterable, ...)

- 接收多个可迭代对象作为参数
- 返回一个zip对象
"""


def simple_demo():
    """zip简单实例"""
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    ret = zip(l1, l2)
    for i in ret:
        print(i)
    print(ret, list(ret), tuple(ret))


def multi_params():
    """zip多个参数"""
    l1 = [1, 2, 3]
    l2 = [4, 5, 6, 7]
    l3 = [7, 8, 9, 10, 11]  # 多个参数以及长度不一致的时候，取最短的参数
    ret = zip(l1, l2, l3)
    print(ret, list(ret))


if __name__ == '__main__':
    simple_demo()
    multi_params()
