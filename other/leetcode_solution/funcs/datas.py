#!/usr/bin/env python
#!coding:utf-8


"""
To generate data for testing.
"""
import random
import string


def _generateList(length, start=0, end=9):
    """
    generate n-D list
    :param length: int
    :param start: int
    :param end: int
    :reurn: List(int)
    """
    ret = []
    for i in range(length):
        num = random.randint(start, end)
        ret.append(num)
    return ret


def _generateSortedList(length, start=0, end=9):
    """
    generate sorted list
    :param length: int
    :param start: int
    :param end: int
    :return: List(int)
    """
    ret = _generateList(length, start, end)
    ret.sort()
    return ret


def _generateStr(length):
    """
    generate str
    :param length: int
    :return: str
    """
    ret = ""
    i = 0
    while i < length:
        # 随机挑选出一个ascii码对应的字符然后加入
        ret += random.choice(string.printable)
        i += 1
    return ret


ret = _generateList(10, 0, 9)
print("ret:", ret)

sorted_ret = _generateSortedList(10, 0, 9)
print("sorted_ret:", sorted_ret)

str_ret = _generateStr(20)
print("str_ret:", str_ret)

