#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.

给定一个整数 n，返回 n! 结果尾数中零的数量。
"""

from functools import reduce


def trailing_zeros(n):
    """
    粗暴的方法
    :param n: int
    :return: int
    """
    ret = reduce(lambda x, y: x * y, range(1, n + 1))
    print("ret:", ret)
    count = 0
    for i in str(ret)[::-1]:
        if i == "0":
            count += 1
        else:
            break
    return count


def trailing_zeros2(n):
    """
    讨巧的方法，因为有几个5因子就有几个0
    :param n: int
    :return: int
    """
    total = 0
    while n >= 1:
        print("n:", n)
        n //= 5
        print("n:", n)
        total += n
    return total


if __name__ == "__main__":
    # print(trailing_zeros(3))
    # print(trailing_zeros(5))
    # print(trailing_zeros(6))
    # print(trailing_zeros(10))

    print(trailing_zeros2(3))
    print(trailing_zeros2(5))
    print(trailing_zeros2(10))
