#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
合并两个列表为一个无重复元素的列表
"""


def merge_list(*args):
    s = set()
    for arg in args:
        s = s.union(arg)
    return list(s)


l1 = [12, 2, 4, 2, 56, 2]
l2 = [2, 4, 5, 77, 8]
print(merge_list(l1, l2))

