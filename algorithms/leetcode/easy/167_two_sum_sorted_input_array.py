#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
"""


def two_sum(numbers, target):
    """
    因为是有序的数组，可以根据其特点来进行选择
    :param numbers: list,有序的整数数组
    :param target: int
    :return: tuple, (int, int)
    """
    start, end = 0, len(numbers) - 1
    while start < end:
        ret = numbers[start] + numbers[end]
        if ret < target:
            start += 1
        elif ret > target:
            end -= 1
        else:
            # 按照规定，下标值不是从0开始，而是从1开始
            return (start+1, end+1)


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    # target = 100
    print(two_sum(numbers, target))
