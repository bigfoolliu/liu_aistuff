#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶


爬楼梯

思路：dp问题，从后往前看,类斐波那契问题
"""

import unittest



class Solution:

    def climbStairs(self, n):
        """
        :param n: int
        :return: int
        """
        if n == 0:
            return 1
        dp = [None] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        # 注意当2 > n+1时候，不会返回数据
        for i in range(2, n + 1):
            # 核心点，最后一步可以是1步或者2步,所以可能性是其和
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.climbStairs = Solution().climbStairs

    def test1(self):
        _n = 2
        _ans = 2
        self.assertEqual(self.climbStairs(_n), _ans)

    def test2(self):
        _n = 3
        _ans = 3
        self.assertEqual(self.climbStairs(_n), _ans)


if __name__ == "__main__":
    unittest.main()
