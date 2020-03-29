#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.

计算一个非负整数的平方根，没有整数平方根的时候返回整数部分

思路：
"""


import math


def my_sqrt(x):
    """
    :param x: int
    :return: int
    """
    ret = int(str(math.sqrt(x)).split(".")[0])
    return ret


def my_sqrt2(x):
    """
    :param x: int
    :return: int
    """
    return int(x**0.5)


if __name__ == "__main__":
    print(my_sqrt(4))
    print(my_sqrt(8))
    print(my_sqrt2(4))
    print(my_sqrt2(8))
