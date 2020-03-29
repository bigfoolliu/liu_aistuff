#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

爬楼梯

思路：dp问题，从后往前看,类斐波那契问题
"""


def climbing_stairs(n):
    """
    :param n: int
    :return: int
    """
    if n == 0:
        return 1
    dp = [None] * (n+1)
    dp[0] = 1
    dp[1] = 1
    # 注意当2 > n+1时候，不会返回数据
    for i in range(2, n+1):
        # 核心点，最后一步可以是1步或者2步,所以可能性是其和
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


if __name__ == "__main__":
    print(climbing_stairs(0))
    print(climbing_stairs(1))
    print(climbing_stairs(2))
    print(climbing_stairs(3))
    print(climbing_stairs(4))
    print(climbing_stairs(5))
    print(climbing_stairs(6))
    print(climbing_stairs(7))
    print(climbing_stairs(10))
