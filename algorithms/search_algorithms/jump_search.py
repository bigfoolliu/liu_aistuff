#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python实现跳转搜索
"""


import math


def jump_search(array, target):
    """跳转搜索"""
    n = len(array)
    step = int(math.floor(math.sqrt(n)))  # 跳转的间隔
    prev = 0  # 跳转间隔的前面一个下标
    while array[min(step, n)-1] < target:
        prev = step
        step += int(math.floor(math.sqrt(n)))
        if prev >= n:
            return -1

    while array[prev] < target:
        prev = prev + 1
        if prev == min(step, n):
            return -1
    if array[prev] == target:
        return prev
    return -1


if __name__ == "__main__":
    array = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    target = 55
    index = jump_search(array, target)
    print("Number " + str(target) + " is at index " + str(index))
