#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
斐波那契查找Python实现

- 斐波那契数列递推公式：F(n)=F(n-1)+F(n-2)

基本原理：
1. 斐波那契数列前一个数和后一个数的比值逐渐接近黄金比例0.618
2. 查询有序数列，且长度为某斐波那契数-1，即len(k)-1
3. 分割点F[k-1], 前F[k-1]-1, 后F[k-2]-1，共F[k]-1
4. 确定查询点位置，在前半部分则k=k-1，后半部分则k=k-2
"""


def fibonacci_search(array, target):
    """
    斐波那契查找首选需要一个现成的斐波那契表,且其最大元素必须超过查找表中元素个数的数值
    """
    fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

    left = 0
    right = len(array) - 1
    print("right: {}".format(right))

    k = 0  # k为F表中首个元素值不小于查找表中的元素个数值的下标
    while right > fib[k] - 1:
        k += 1

    i = right
    while fib[k] - 1 > i:
        array.append(array[right])  # 查找表的末尾添加末位元素
        i += 1

    # 主逻辑
    while left <= right:
        if k < 2:
            mid = left
        else:
            mid = left + fib[k-1] - 1

        if target < array[mid]:
            right = mid - 1
            k -= 1
        elif target > array[mid]:
            left = mid + 1
            k -= 2
        else:  # target == array[mid]
            if mid <= right:
                return mid
            else:
                return right
    return -1


if __name__ == "__main__":
    sorted_array = [0, 1, 2, 4, 5, 6, 41, 56, 66, 77, 88, 91, 244, 1000, 2000, 5000, 10000, 20000]
    target1 = 10000
    target2 = 255

    ret1 = fibonacci_search(sorted_array, target1)
    ret2 = fibonacci_search(sorted_array, target2)
    print(ret1, ret2)
