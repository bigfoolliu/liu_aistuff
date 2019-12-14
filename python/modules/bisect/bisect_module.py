#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
bisect库使用

该库主要用来排序,主要是二分查找
"""


import bisect


def bisect_left_demo():
    array = [12, 22, 23, 25, 30, 33]  # 有序列表
    value_insert_point = bisect.bisect_left(array, 12)  # 查找元素，存在则返回其左侧的位置，不存在则返回应该插入的位置
    print(value_insert_point)


def bisect_right_demo():
    array = [12, 22, 23, 25, 30, 33]  # 有序列表
    value_insert_point = bisect.bisect_right(array, 12)  # 查找元素，存在则返回其右侧的位置，不存在则返回应该插入的位置
    print(value_insert_point)


def insort_left_demo():
    array = [12, 22, 23, 25, 30, 33]  # 有序列表
    value_insort_left = bisect.insort_left(array, 31)  # 插入元素，存在时插入在左侧
    print(value_insort_left, array)


def insort_right_demo():
    array = [12, 22, 23, 25, 30, 33]  # 有序列表
    value_insort_right = bisect.insort_right(array, 31)  # 插入元素，存在时插入在右侧
    print(value_insort_right, array)


if __name__ == "__main__":
    # bisect_left_demo()
    # bisect_right_demo()
    insort_left_demo()
    insort_right_demo()
