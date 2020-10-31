#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

示例:

输入: [2,1,5,6,2,3]
输出: 10

"""

import unittest


class Solution:

    def largestRectangleArea(self, heights):
        """
        暴力解法，以每个柱形为的高作为目标矩形的高，求出最大的底边，然后算出面积，最后得到最大面积
        :param heights: List(int]
        :return: int
        """
        if not heights:
            return 0
        if len(heights) == 1:
            return heights[0]
        ret = heights[0]

        index = 0
        while index < len(heights):
            # 终止条件，左右分别有比当前高度低时候
            left = right = index
            while left > 0 and heights[left - 1] >= heights[index]:
                left -= 1
            while right < len(heights) - 1 and heights[right + 1] >= heights[index]:
                right += 1
            ret = max(ret, (right - left + 1) * heights[index])
            index += 1

        return ret


class Solution2:

    def largestRectangleArea(self, heights):
        """
        每次求解每根柱子的左右边界时，都需要进行循环查找，因此在内层多了一个O(n)复杂度。
        如果使用栈根据高度由低到高的顺序将柱子的进行存储的话，此时会更容易找到当前柱子的左边界
        因此我们可以维护一个栈，栈中元素需要由小到大进行排序。
        :param heights: List(int]
        :return: int
        """
        return


class TestDemo(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()

    def test1(self):
        _heights = [2, 1, 5, 6, 2, 3]
        self.assertEqual(self.solution.largestRectangleArea(_heights), 10)

    def test2(self):
        _heights = [2, 1, 5, 6, 2, 3]
        self.assertEqual(self.solution2.largestRectangleArea(_heights), 10)


if __name__ == '__main__':
    unittest.main()
