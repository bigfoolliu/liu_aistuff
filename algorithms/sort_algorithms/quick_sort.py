#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


def quick_sort(array):
    """
    快速排序
    比较标准的方式
    """
    print("[INFO]Quick_sort begins for {}".format(array))
    if len(array) <= 1:
        return array

    def recursive(begin, end):
        if begin > end:
            return None
        
        l, r = begin, end

        # 选取一个标准值，可以选取其中的任意一个数
        basic = array[l]

        # 左右标记相遇为一个循环
        while l < r:
            while l < r and array[r] > basic:
                r -= 1
            while l < r and array[l] <= basic:
                l += 1
            # 当左边标记比基准值大，右边标记比基准值小时，交换左右标记的值
            array[l], array[r] = array[r], array[l]
        
        # 当左右标记相遇的时候，调换基准值和该相遇标记的值，该标记的位置值，左边数值都小于它，右边都大于它
        # 同时将该左侧的值和起始值替换为基准值和左侧值
        array[l], array[begin] = basic, array[l]

        # 此时l==r，对分割的区间进行分治
        recursive(begin, l-1)
        recursive(l+1, end)

    recursive(0, len(array)-1)
    return array


if __name__ == "__main__":
    array = [3, 2, 4, 6, 6, 5, 8, 1, 8]
    print(quick_sort(array))
