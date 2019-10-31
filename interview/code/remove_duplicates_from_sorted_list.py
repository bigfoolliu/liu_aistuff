#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
移除排序好的重复数字，返回不重复的数字个数
使用快慢指针法
[0, 0, 1, 2, 2, 5] ---> [0, 1, 2, 5] 4
"""


def remove(array):
    if len(array) <= 1:
        return array

    pre = 0
    for cur in range(1, len(array)):
        if array[pre] != array[cur]:
            pre += 1
            array[pre] = array[cur]
    return array[:pre+1], pre+1


print(remove([0, 0, 1, 2, 2, 5]))
