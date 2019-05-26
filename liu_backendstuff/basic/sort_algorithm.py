#!/usr/bin/env python
#!coding:utf-8


"""
几个常见的排序算法
"""
import time


def count_time(func):
    """计算耗时装饰器"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs)
        end_time = time.time()
        print("[INFO]Cost time:{}".format(end_time - start_time))
        return ret  # 注意此处将函数的返回值返回
    return wrapper


@count_time
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


@count_time
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


@count_time
def quick_sort(array):
    """快速排序"""
    print("[INFO]Quick_sort begins for {}".format(array))
    if len(array) <= 1:
        return array

    def recursive(begin, end):
        if begin > end:
            return None
        l, r = begin, end
        pivot = array[l]  # 以左侧的数作为基准数
        while l < r:
            while l < r and array[r] > pivot:
                r -= 1
            while l < r and array[l] <= pivot:
                l += 1
            array[l], array[r] = array[r], array[l]
        array[l], array[begin] = pivot, array[l]

        recursive(begin, l-1)  # 对左侧的元素进行排序
        recursive(r+1, end)  # 对右侧的元素进行排序

    recursive(0, len(array)-1)
    return array


print(bubble_sort([1, 2, 5, 7, 12, 4, 2, 8]))
print(insert_sort([12, 2, 4, 1, 6, 2, 7, 8]))
print(quick_sort([12, 34, 5, 6, 2, 4, 1, 9]))

