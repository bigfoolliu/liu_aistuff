#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

    Input: 123
    Output: 321
    Example 2:

    Input: -123
    Output: -321
    Example 3:

    Input: 120
    Output: 21
    Note:
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
    [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer
    overflows.

思路：转化为字符串然后反转
"""


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    # 转换为字符串，然后处理输出
    ret = 0
    if x < 0:
        ret = -int(str(x)[::-1][:-1])  # [:-1]为去掉负号,int转换可以去除首位的0
    elif x >= 0:
        ret = int(str(x)[::-1])
    return ret if -0x7fffffff < ret < 0x7fffffff else 0


if __name__ == "__main__":
    for i in range(-200, 100):
        reverse_ret = reverse(i)
        print("x:{} reverse_ret:{}".format(i, reverse_ret))
    reverse_ret = reverse(123123314214414124214214)
    print(reverse_ret)
