#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
最长没有重复的子字符串
"""


def longest_substring(s):
    start = 0
    ret = 0
    hash_map = {}
    for i in range(len(s)):
        start = max(start, hash_map.get(s[i], -1) + 1)
        ret = max(ret, i - start + 1)
        hash_map[s[i]] = i
    return ret, s[start:start + ret]


print(longest_substring("awadfg"))
print(longest_substring("awadedfg"))
