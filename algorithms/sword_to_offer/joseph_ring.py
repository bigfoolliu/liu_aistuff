#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
0, 1, 2, n-1这n个数字排成一个圆环, 从数字0开始每次从这个圆圈里删除第m个数字
求这个圆圈中最后剩下的一个数字
"""


# -*- coding:utf-8 -*-
class Solution:

    @staticmethod
    def last_remaining_solution(n, m):
        if n < 1 or m < 1:
            return -1
        remain_index = 0
        for i in range(1, n + 1):
            remain_index = (remain_index + m) % i
            print(remain_index)
        return remain_index


s = Solution()
ret = s.last_remaining_solution(3, 1)
print("last remaining index:", ret)
