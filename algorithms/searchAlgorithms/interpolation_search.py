#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python实现差值搜索算法
"""


# import bisect


def interpolation_search(array, target):
    """
    差值搜索基本实现
    return: int
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        # 核心
        index = left + int((target - array[left]) * (right - left) / (array[right] - array[left]))
        print("index: {}".format(index))

        # out of range check
        if index < 0 or index >= len(array):
            return -1
        
        if array[index] == target:
            return index
        else:
            if target < array[index]:
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
