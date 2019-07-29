"""
跳转搜索
"""
from __future__ import print_function

import math


def jump_search(arr, x):
    n = len(arr)
    step = int(math.floor(math.sqrt(n)))  # 跳转的间隔
    prev = 0  # 跳转间隔的前面一个下标
    while arr[min(step, n)-1] < x:
        prev = step
        step += int(math.floor(math.sqrt(n)))
        if prev >= n:
            return -1

    while arr[prev] < x:
        prev = prev + 1
        if prev == min(step, n):
            return -1
    if arr[prev] == x:
        return prev
    return -1



arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
x = 55
index = jump_search(arr, x)
print("Number " + str(x) +" is at index " + str(index))
