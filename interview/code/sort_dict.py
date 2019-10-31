#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
给列表中的字典排序
"""
import operator
l = [{"name": "a", "age": 10}, {"name": "b", "age": 12}, {"name": "c", "age": 8}]

print(l)

# 使用内置模块
ret = sorted(l, key=operator.itemgetter("age"))
print(ret)

# 使用匿名函数
ret2 = sorted(l, key=lambda x:x["age"])
print(ret2)
