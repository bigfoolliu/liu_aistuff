#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


def bubble_sort(array):
    """冒泡排序"""
    print("[INFO]Bubble_sort begins for {}".format(array))
    if len(array) <= 1:
        return array
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


if __name__ == "__main__":
    array = [9, 2, 4, 8, 1, 6, 3]
    print(bubble_sort(array))
