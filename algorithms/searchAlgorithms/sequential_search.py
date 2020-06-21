#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
顺序查找python实现
"""


def sequential_search(array, target):
    """
    array: list
    return: int
    """
    if not array:
        return -1
    for index, item in enumerate(array):
        if item == target:
            return index
    return -1


if __name__ == '__main__':
    test_array = [0, 3, 4, 6, 12, 5, 66, 7]
    target1 = 12
    target2 = 123

    ret1 = sequential_search(test_array, target1)
    ret2 = sequential_search(test_array, target2)
    print(ret1)
    print(ret2)
