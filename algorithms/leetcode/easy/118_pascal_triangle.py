#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

生成指定行数的杨辉三角
"""


def pascal_triangle(num):
    """
    :param num: int
    :return: list
    """
    ret = []
    for i in range(num):
        num_row = []

        if i == 0:
            num_row = [1]
        elif i == 1:
            num_row = [1, 1]
        else:
            num_row = [None] * (i + 1)
            num_row[0], num_row[-1] = 1, 1
            for j in range(1, len(num_row) - 1):
                num_row[j] = ret[i - 1][j - 1] + ret[i - 1][j]
        ret.append(num_row)
    return ret


if __name__ == "__main__":
    ret = pascal_triangle(10)
    for row in ret:
        print(row)
