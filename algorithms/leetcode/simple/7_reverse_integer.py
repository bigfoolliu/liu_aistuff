#!/usr/bin/env python
#!coding:utf-8


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
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

思路：转化为字符串然后反转
"""


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    # 转换为字符串，然后处理输出
    if x < 0:
        ret = -int(str(x)[::-1][:-1])  # [:-1]为去掉负号
    elif x >= 0:
        ret = int(str(x)[::-1])
    return ret if 0x7fffffff < ret < 0x7fffffff else 0


for x in range(-100, 100):
    ret = reverse(x)
    print("[info]x:{} ret:{}".format(x, ret))
