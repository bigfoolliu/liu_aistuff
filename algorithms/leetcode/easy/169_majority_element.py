#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
"""


def majority_element(nums):
    """
    因为一定有众数，且其数量大于n/2，故将其排好序直接取中间位置的元素即可
    :param nums: list
    :return: int
    """
    return sorted(nums)[int(len(nums)/2)]


if __name__ == "__main__":
    nums = [3, 2, 3]
    print(majority_element(nums))
