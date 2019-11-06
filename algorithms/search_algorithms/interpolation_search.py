#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python实现差值搜索算法
"""


import bisect


def interpolation_search(sorted_array, target):
    """
    差值搜索基本实现
    return: int
    """
    left = 0
    right = len(sorted_array) - 1

    while left <= right:
        # 核心
        index = left + int((target - sorted_array[left]) * (right - left) / (sorted_array[right] - sorted_array[left]))
        print("index: {}".format(index))

        # out of range check
        if index < 0 or index >= len(sorted_array):
            return -1
        
        if sorted_array[index] == target:
            return index
        else:
            if target < sorted_array[index]:
                right = index - 1
            else:
                left = index + 1
    return -1


if __name__ == '__main__':
    sorted_array = [0, 12, 23, 45, 56, 66, 77, 345, 556, 2345]
    target1 = 345
    target2 = 111

    ret1 = interpolation_search(sorted_array, target1)
    ret2 = interpolation_search(sorted_array, target2)
    print(ret1, ret2)
