#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
反向迭代一个序列
"""

import copy

# 当序列为列表的时候
l1 = [1, 2, 3, 4, 5, 6]
l2 = copy.deepcopy(l1)
l2.reverse()
print(l1, l2)

# 当序列为字符串时候
s = "hello. pyhton"
print(s, s[::-1])
