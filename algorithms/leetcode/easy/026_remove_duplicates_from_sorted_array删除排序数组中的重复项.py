#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length. Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length. Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

去除有序数组中的重复数字并返回其去重后的长度，且时间复杂度为O(1)

双指针
"""


import unittest


def remove_duplicates_from_sorted_array(sorted_array):
    """
    :param sorted_array: list,有序数组
    :return int，去重后的数组的长度
    """
    if not sorted_array:
        return 0
    if len(sorted_array) == 1:
        return 1
    slow = 0  # fast为快指针,slow为慢指针
    for fast in range(1, len(sorted_array)):
        # 快指针始终前进
        # 如果快慢指针指向的数字不同，则慢指针前进一步，同时将当前的慢指针指向的数字赋值
        if sorted_array[fast] != sorted_array[slow]:
            slow += 1
            sorted_array[slow] = sorted_array[fast]  # 同时将慢指针对应元素修改
    return slow + 1


class TestRemoveDuplicates(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_1(self):
        self.assertEqual(2, remove_duplicates_from_sorted_array([1, 1, 2]))

    def test_2(self):
        self.assertEqual(1, remove_duplicates_from_sorted_array([1, 1]))

    def test_3(self):
        self.assertEqual(4, remove_duplicates_from_sorted_array([0, 0, 1, 1, 2, 3]))


if __name__ == '__main__':
    unittest.main()
