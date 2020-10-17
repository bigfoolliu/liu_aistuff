#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
itertools模块

迭代工具模块
"""

import itertools

# 产生ABCD的全排列
a = itertools.permutations('ABCD')
print(list(a))

# 产生ABCD的四选三组合
b = itertools.combinations('ABCD', 3)
print(list(b))

# 产生ABCD和123的笛卡尔积
c = itertools.product('ABCD', '123')
print(list(c))

# 产生ABC的无限循环序列
d = itertools.cycle(('A', 'B', 'C'))
# print(list(d))
