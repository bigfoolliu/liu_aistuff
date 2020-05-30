#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
算法学习
"""

from pygorithm.sorting import selection_sort
from pygorithm.sorting import quick_sort
from pygorithm.fibonacci import generator
from pygorithm.dynamic_programming import binary_knapsack


def sort_demo():
    """排序算法使用"""
    l = [12, 3, 3, 4, 55, 55, 6, 34, 56]
    sorted_l = selection_sort.sort(l)
    print(sorted_l)

    sorted_l2 = quick_sort.sort(l)
    print(sorted_l2)


def fib_demo():
    """使用生成器的方式生成斐波那契数列"""
    ret = generator.get_sequence(20)
    print(ret)


def get_code_demo():
    """获取展示的代码"""
    ret = binary_knapsack.get_code()
    print(ret)


if __name__ == "__main__":
    sort_demo()
    fib_demo()
    get_code_demo()
