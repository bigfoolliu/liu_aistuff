#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu

"""
二维数组，从左到右递增，从上到下递增，给出一个数，判断是否在数组中

0   1   3   5
2   3   4   7
5   7   8   9
"""

import time


# 计算时间的装饰器
def count_time(func):

    def wrapper(*args, **kwargs):
        start_time = time.clock()
        ret = func(*args, **kwargs)
        end_time = time.clock()
        print("spend_time:  %.40f s" % (end_time - start_time))
        return ret

    return wrapper


# 方法一：简单粗暴的方法
@count_time
def find_integer(array, target):
    """
    :params array: [[]]
    :params target: int
    :return bool
    """
    if not array:
        return False
    for i in array:
        if i[0] <= target <= i[len(i)-1]:
            if target in i:
                return True
        else:
            if i[0] > target:
                break
    return False


# 方法2：从左下角开始比较，查找速度更快
@count_time
def find_integer1(array, target):
    """
    :params array: [[]]
    :params target: int
    :return bool
    """
    if not array:
        return False
    rows = len(array)
    cols = len(array[0])

    row = rows - 1
    col = 0
    while row >= 0 and col <= cols - 1:
        if array[row][col] == target:
            return True
        elif array[row][col] > target:
            row -= 1
        else:
            col += 1
    return False


# 方法3：从右上角开始比较，查找速度和2相当
@count_time
def find_integer2(array, target):
    """
    :params array: [[]]
    :params target: int
    :return bool
    """
    if not array:
        return False
    rows = len(array)
    cols = len(array[0])

    row = 0
    col = cols - 1
    while row <= rows - 1 and col >= 0:
        if array[row][col] == target:
            return True
        elif array[row][col] > target:
            col -= 1
        else:
            row += 1
    return False


if __name__ == "__main__":
    array = [[0, 1, 3, 5], [2, 3, 4, 7], [5, 7, 8, 9]]
    print(find_integer(array, 4))
    print(find_integer(array, 6))

    print(find_integer1(array, 4))
    print(find_integer1(array, 6))

    print(find_integer2(array, 4))
    print(find_integer2(array, 6))
