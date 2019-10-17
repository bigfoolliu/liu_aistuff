#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

将一个排好序的数组插入到另外一个排号序的数组中作为一个排好序的数组。
假设m，n分别为两个数组的元素个数，将2插入到1中

思路：
从后往前比较,并且从后往前插入
"""


def merge_sorted_array(array1, array2, m, n):
    """
    :param array1: list
    :param array2: list
    :param m: int
    :param n: int
    return list
    """
    while m > 0 and n > 0:
        if array1[m - 1] <= array2[n - 1]:  # 从后面往前面对比，找到大的元素
            array1[m + n - 1] = array2[n - 1]
            n -= 1
        else:
            array1[m + n - 1] = array1[m - 1]
            m -= 1
    if n > 0:  # 当array2还存在最小的数值时候
        array1[:n] = array2[:n]
    return array1


if __name__ == "__main__":
    array1 = [1, 2, 3, 0, 0, 0]
    array2 = [2, 5, 6]
    print(merge_sorted_array(array1, array2, 3, 3))
