#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

找到字符串中首次出现的子字符串的下标
思路：python列表的使用
"""


def strStr(haystack, needle):
    """
    :param hsystack: str
    :param needle: str
    :return int
    """
    for i in range(0, len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1


if __name__ == "__main__":
    print(strStr("hello", "ll"))
    print(strStr("aaaaa", "bba"))
