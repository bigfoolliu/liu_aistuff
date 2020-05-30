#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
[2, 6, 7, 3, 12] 9=2+7, 9=3+6
"""


def two_sum(array, target):
    if not array:
        return None
    hash_map = {}
    for i in range(0, len(array)):
        num2 = target - array[i]
        if num2 in hash_map:
            return i, hash_map[num2]
        hash_map[array[i]] = i
    return None


print(two_sum([2, 7, 3, 8], 5))
