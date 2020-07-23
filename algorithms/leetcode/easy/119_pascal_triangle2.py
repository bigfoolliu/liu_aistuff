#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?


给定一个非负整数索引，返回杨辉三角的第n行所有数字
"""


def pascal_triangle_get_row(row):
    """
    :param row: int,非负整数
    :return: list
    """
    fact = [1] * (row + 1)
    ret = [1] * (row + 1)
    for i in range(1, row + 1):
        fact[i] = fact[i - 1] * i

    print("fact:", fact)

    for i in range(1, row + 1):
        ret[i] = int(fact[-1] / (fact[i] * fact[row - i]))
    return ret


if __name__ == "__main__":
    print(pascal_triangle_get_row(0))
    print(pascal_triangle_get_row(3))
    print(pascal_triangle_get_row(5))
