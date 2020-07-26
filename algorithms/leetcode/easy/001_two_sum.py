#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

思路：使用hash表,使用空间换时间
"""


import unittest


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hash_map = {}
    for index, num in enumerate(nums):
        # 查找另一个结果是否在hash中
        num2 = target - num
        if num2 in hash_map:
            return [index, hash_map[num2]]
        # 将这个暂时不需要的数字用其自身作为key，下标作为value存储
        hash_map[num] = index
    return None


class TestTwoSum(unittest.TestCase):

    def test_demo1(self):
        self.assertEqual([0, 1], twoSum([2, 7, 11, 15], 9))

    def test_demo2(self):
        self.assertEqual([1, 2], twoSum([2, 7, 11, 15], 18))


if __name__ == "__main__":
    unittest.main()
