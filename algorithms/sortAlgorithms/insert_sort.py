#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


def insert_sort(array):
    """插入排序"""
    print("[INFO]Insert_sort begins for {}".format(array))
    if len(array) <= 1:
        return array
    for i in range(len(array)):
        for j in range(i):
            if array[i] < array[j]:
                array.insert(j, array.pop(i))
    return array


if __name__ == '__main__':
    test_array = [0, 2, 8, 3, 6, 2, 9]
    print(insert_sort(test_array))
