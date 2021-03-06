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
    for common_tuple in zip(*strs):  # ("f", "f") ("l", "w")
        if len(set(common_tuple)) > 1:  # 大于1说明该位置的元素有不同
            break
        prefix += common_tuple[0]
    return prefix


def longest_common_prefix2(strs):
    """
    :param: List(str)
    return: str
    寻找字符串的最长公共段2
    """
    pass
 

if __name__ == "__main__":
    assert longest_common_prefix(["flower", "flow", "flight"]) == 'fl'
    assert longest_common_prefix(["alower", "flow", "flight"]) == ''
    assert longest_common_prefix(["flower", "flow", "floight"]) == 'flo'

    print('pass')

