#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

给一个非空数组代表一个非负整数，将其加1为整数之后再转换为列表，注意的是每一个元素都是单个整数

思路：
"""


def plus_one(digits):
    """
    :param digits: list
    :return: list
    暴力解法
    """
    # 将数字列表转换为数字
    num = 0
    for i in range(len(digits)):
        num += digits[i] * 10 ** (len(digits) -1 - i)

    num = num + 1
    # 将数字转换为列表
    ret = []
    for i in str(num):
        ret.append(int(i))
    return ret


def plus_one2(digits):
    """
    :param digits: list
    :return: list
    优化版本
    """
    string = ""
    for num in digits:
        string += str(num)

    number = int(string) + 1
    st_ls = list(str(number))
    digits = [int(c) for c in st_ls]
    return digits


print(plus_one([1, 2, 3, 4]))
print(plus_one2([1, 2, 3, 4]))

print(plus_one([4, 3, 2, 1]))
print(plus_one2([4, 3, 2, 1]))
