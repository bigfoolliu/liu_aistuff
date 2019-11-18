#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
用来简单模糊搜索的模块
"""


from fuzzywuzzy import fuzz
from fuzzywuzzy import process


ret = fuzz.ratio("this is a test", "this is also a test")

print(ret)

choices = ["china", "usa", "japan", "russian"]

ret2 = process.extract("ch", choices, limit=2)
print(ret2)

ret3 = process.extractOne("boys", choices)

print(ret3)
