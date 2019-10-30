#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

求连续最大的子序列和。
"""
import time



def maxinum_sum_subarray1(array):
    """
    暴力求解
    :param array: list, 整数数组
    :return int
    """
    start_time = time.perf_counter()
    sums = []
    for i in range(0, len(array)):
        a = 0
        for j in range(i, len(array)):
            a += array[j]
            sums.append(a)
    end_time = time.perf_counter()
    print("cost time:%.8f" % (end_time - start_time))
    return max(sums)


def maxinum_sum_subarray2(array):
    """
    使用前缀和,优化
    :param array: list, 整数数组
    :return int
    """
    start_time = time.perf_counter()
    min_sum = 0  # 前n项和的最小值
    max_sum = array[0]  # 最大子序列和
    pre_sum = 0  # 前缀和
    for i in range(len(array)):
        pre_sum += array[i]
        max_sum = max(max_sum, pre_sum - min_sum)
        min_sum = min(min_sum, pre_sum)
    return max_sum


def maxinum_sum_subarray3(array):
    """
    使用动态规划进行求解

    1.建立状态转移方程的模型
        状态转移方程：
        dp[i] = max(dp[i-1] + nums[i], nums[i])
        dp[i]：当前位置i的最大子序列和
        nums[i]: 数组的第i个元素

        初始化:
        dp[0] = nums[0]
    
    2. 将模型与当前的问题进行对应
        curr_max_sum = max(curr_max_sum + nums[i], numx[i])
        max_sum = max(curr_max_sum, max_sum)

        初始化：
        curr_max_sum = nums[0]

    :param array: list, 整数数组
    :return int
    """
    curr_max_sum = max_sum = array[0]
    for i in range(1, len(array)):
        curr_max_sum = max(curr_max_sum + array[i], array[i])
        max_sum = max(curr_max_sum, max_sum)
    return max_sum


if __name__ == "__main__":
    array = [-2,1,-3,4,-1,2,1,-5,4]
    # array = [2, -3, 4, -5, 1]
    print(maxinum_sum_subarray1(array))
    print(maxinum_sum_subarray2(array))
    print(maxinum_sum_subarray3(array))
