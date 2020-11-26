#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
829. 连续整数求和
给定一个正整数 N，试求有多少组连续正整数满足所有数字之和为 N?

示例 1:

输入: 5
输出: 2
解释: 5 = 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。
示例 2:

输入: 9
输出: 3
解释: 9 = 9 = 4 + 5 = 2 + 3 + 4
示例 3:

输入: 15
输出: 4
解释: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

middle_ret肯定为有理数，否则不存在
N   middle(数字个数) middle_ret(差不多为中间数字或者大1或者小1)
15  1       15  必须有
15  3       5   整除,中间数字为5, 5 >= (3-1)/2, 可以
15  5       3   整除,中间数字为3, 3 >= (5-1)/2, 可以
15  7       2.1xx  非整除,肯定不可以

15  2       7.5  可以 7 + 8
15  4       3.75, 3或者4,
15  6       2.5，2或者3


说明: 1 <= N <= 10 ^ 9

"""


import unittest


class Solution:

    def consecutiveNumbersSum(self, N):
        """
        :param N: int
        :return:
        """
        ret = 1
        # 1.从1开始整除，如果可以有连续的结果，那么肯定为奇数或者偶数个整数相加得到
        # 2.如果最终结果为奇数个数相加，则中间的整数middle能被整除，且整除结果middle_ret肯定不小于 (middle-1)/2
        # 3.如果最终结果为偶数个数相加，则
        for i in range(0, ):
            pass
        return ret


class TestDemo(unittest.TestCase):

    def setUp(self):
        self.solution = Solution().consecutiveNumbersSum

    def test1(self):
        self.assertEqual(2, self.solution(5))

    def test2(self):
        self.assertEqual(3, self.solution(9))

    def test3(self):
        self.assertEqual(4, self.solution(15))


if __name__ == '__main__':
    unittest.main()
