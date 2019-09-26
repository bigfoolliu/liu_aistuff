#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
little tips about python
"""

import os
import sys
from collections import Counter
from math import ceil


def all_unique(lst):
    """判断列表的所有元素是否唯一"""
    return len(lst) == len(set(lst))


def is_str_element_same(str1, str2):
    """检查两个字符串的组成元素是否一样"""
    return Counter(str1) == Counter(str2)


def size_of(var):
    """获取变量所占空间"""
    return sys.getsizeof(var) 


def byte_size_of(str1):
    """检查字符串占用的字节数"""
    return len(str1.encode("utf-8"))


def lst_chunk(lst, size):
    """将列表按照指定的长度进行分块切割列表"""
    return list(map(lambda x: lst[x * size: x * size + size], list(range(0, ceil(len(lst) / size)))))


if __name__ == "__main__":
    str1 = "sfsd34"
    str2 = "sdfsdfsd"

    # print(is_str_element_same(str1, str2))
    # print(size_of(str1))

    print(byte_size_of(str1))

    lst = ["12", "34", 4, 6, "6", 8, 12, 34, 5]
    print(lst_chunk(lst, 2))
