#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python filter函数实例

用来过滤序列
"""


def basic_demo():
    """基础使用"""
    seq = [1, 2, 3, 5, 6, 4]
    ret = filter(lambda x: x > 3, seq)
    print(next(ret))
    print(ret)  # 返回一个filter对象，可迭代
    print(list(ret))


def is_not_empty(s):
    """判断字符是否为空字符串"""
    return s and len(s.strip()) > 0


def defined_func_demo():
    """使用自定义的函数进行过滤"""
    l = ["helo ", "  ", " s  ", "", None]
    ret = filter(is_not_empty, l)
    print(list(ret))


if __name__ == "__main__":
    # basic_demo()
    defined_func_demo()
