#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
随机从扑克牌中抽出了5张牌,判断是不是顺子,
决定大小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
"""


class Solution:

    @staticmethod
    def is_continuous(numbers):

        print(numbers)

        if numbers is None or len(numbers) <= 0:
            return False
        # 把A、J、Q、K转化一下
        trans_dict = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
        for i in range(len(numbers)):
            if numbers[i] in trans_dict.keys():
                numbers[i] = trans_dict[numbers[i]]

        numbers = sorted(numbers)

        print(numbers)

        num_of_zero = 0
        num_of_gap = 0

        # 统计0的个数
        i = 0
        while i < len(numbers) and numbers[i] == 0:
            num_of_zero += 1
            i += 1

        # 统计间隔的数目
        small = num_of_zero
        big = small + 1
        print(small, big)
        # 从左至右两两比较数字
        while big < len(numbers):
            # 出现对子, 不可能是顺子
            if numbers[small] == numbers[big]:
                return False

            num_of_gap += numbers[big] - numbers[small] - 1  # 获取相邻两个数字的间隔
            small = big
            big += 1

            print(small, big)

        print(num_of_gap)
        return False if num_of_gap > num_of_zero else True


test = ['A', 3, 2, 5, 0]
test2 = [0, 3, 1, 6, 4]
s = Solution()
print(s.is_continuous(test))
print(s.is_continuous(test2))
