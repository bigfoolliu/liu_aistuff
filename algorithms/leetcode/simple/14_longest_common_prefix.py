#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

思路：利用充分利用Python zip函数，以及元组，集合的特性
"""


def longest_common_prefix(strs):
    """
    :param: List(str)
    return: str
    寻找字符串的最长公共段
    """
    prefix = ""
    # zip打包列表的时候会打包成元组，且只会打包到最短的元素
    for cmbn in zip(*strs):
        if len(set(cmbn)) > 1:
            break
        prefix += cmbn[0]
    return prefix


print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["alower", "flow", "flight"]))
print(longest_common_prefix(["flower", "flow", "floight"]))
