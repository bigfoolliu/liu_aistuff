#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
"""


def single_number(nums):
    """
    利用异或位操作的性质
    :param nums: list
    :return: int
    """
    for i in range(1, len(nums)):
        nums[0] ^= nums[i]

    return nums[0]


if __name__ == "__main__":
    print(single_number([2, 2, 1]))
    print(single_number([4, 1, 2, 1, 2]))
