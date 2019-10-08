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
            while l < r and array[r] > pivot:  # 右侧的数大于基准数则不必移动
                r -= 1
            while l < r and array[l] <= pivot:  # 左侧的数小于基准数则不必移动
                l += 1
            array[l], array[r] = array[r], array[l]
        array[l], array[begin] = pivot, array[l]  # 完成一轮，找到基准元素应该放置的位置

        recursive(begin, l-1)
        recursive(r+1, end)

    recursive(0, len(array)-1)
    return array


def quick_sort2(array, begin, end):
    """
    快速排序清晰版本形式
    begin作为该区间的最小下标
    end作为该区间的最大下标
    """
    l, r = begin, end
    # 如果左右下标重合则一轮结束
    if l >= r:
        return
    # 取该区间的第一个元素作为基准元素
    pivot = array[begin]
    while l < r:
        while l < r and array[r] >= pivot:
            r -= 1
        # 找到右边第一个小于基准的数，赋值给左边的l，而此时左边的元素记录在pivot基准中
        array[l] = array[r]
        while l < r and array[l] <= pivot:
            l += 1
        # 找到左边第一个大于基准的数，赋值给右边的r，而此时右边的r值和左边的l值相同
        array[r] = array[l]
    # 一轮循环结束，将基准值放到正确的位置，即l处
    array[l] = pivot

    # 在除去l之外的两段继续递归
    quick_sort2(array, begin, l-1)
    quick_sort2(array, l+1, end)

    return array


print(bubble_sort([1, 2, 5, 7, 12, 4, 2, 8]))
print(insert_sort([12, 2, 4, 1, 6, 2, 7, 8]))
print(quick_sort([8, 4, 6, 10, 7]))

array = [8, 4, 6, 10, 7]
print(quick_sort2(array, 0, len(array)-1))
