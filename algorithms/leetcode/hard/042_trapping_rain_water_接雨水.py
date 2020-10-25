#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

雨水收集
给定n个代表海拔图的非负整数，其中每个条的宽度为1，计算下雨后它能捕获多少水。

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

解题思路：栈，双指针

https://leetcode-cn.com/problems/trapping-rain-water/
"""

import unittest


class Solution(object):
    """
    直观思路：遍历每一列，分别求每一列上方可以积水多少
    1.求每一列可以积水多少，根据左边最高的墙和右边最高的墙
    2.当前列装水多少根据木桶效应，应该根据左右两个最高墙中较矮的那个, 因此有三种情况
    3.当前列矮于较矮的列，当前列可以存水量为 较矮列高度 - 当前列高度
    4.当前列高于或等于较矮的列，水量为0
    """

    def trap(self, height):
        """
        :param height: list(int)
        :return: int
        """
        if not height or len(height) == 1 or not isinstance(height, list):
            return 0

        ret = 0
        for index, item in enumerate(height):
            if index != 0 and index != (len(height) - 1):
                # 找出左侧最大值
                left_max = max(height[0:index])
                # 找出右侧最大值
                if not index == len(height):
                    right_max = max(height[index:])
                else:
                    right_max = 0

                # 较小值
                min_height = min(left_max, right_max)

                # 分情况讨论
                if item < min_height:
                    ret += min_height - item
        return ret


class Solution2(object):
    """
    使用栈来保存每一个墙

    当遍历墙的高度的时候，如果当前高度小于栈顶的墙高度，说明这里会有积水，我们将墙的高度的下标入栈。
    如果当前高度大于栈顶的墙的高度，说明之前的积水到这里停下，我们可以计算下有多少积水了。计算完，就把当前的墙继续入栈，作为新的积水的墙。

    栈顶保存的高度始终是栈里最小的

    总体的原则就是:
    1.当前高度小于等于栈顶高度，入栈，指针后移。
    2.当前高度大于栈顶高度，出栈，计算出当前墙和新的栈顶的墙之间水的多少，然后计算当前的高度和新栈的高度的关系
    3.重复第 2 步。直到当前墙的高度不大于栈顶高度或者栈空，则把当前墙入栈，指针后移。
    """

    def trap(self, height):
        """
        :param height: list(int)
        :return: int
        """
        if not isinstance(height, list) or len(height) in [0, 1]:
            return 0
        stack = []
        ret = 0
        current = 0
        while current < len(height):
            # 栈不为空或者当前高度大于栈顶高度则一直循环
            while len(stack) != 0 and height[current] > height[stack[-1]]:
                # 获取栈顶高度并出栈
                top = height[stack[-1]]
                stack.pop()
                if not stack:
                    break
                # 计算新的栈顶高度下标和当前高度下标之间的距离
                distance = current - stack[-1] - 1
                min_height = min([height[stack[-1]], height[current]])
                ret += distance * (min_height - top)
            stack.append(current)
            current += 1
        return ret


class TestSolution(unittest.TestCase):

    def test_demo1(self):
        _height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        _ret = Solution().trap(_height)
        self.assertEqual(_ret, 6)

    def test_demo2(self):
        _height = [4, 2, 0, 3, 2, 5]
        _ret = Solution().trap(_height)
        self.assertEqual(_ret, 9)

    def test_demo3(self):
        _height = []
        _ret = Solution().trap(_height)
        self.assertEqual(_ret, 0)

    def test_demo4(self):
        _height = [4]
        _ret = Solution().trap(_height)
        self.assertEqual(_ret, 0)

    def test_demo5(self):
        _height = [1, 0, 2]
        _ret = Solution().trap(_height)
        self.assertEqual(_ret, 1)


class TestSolution2(unittest.TestCase):

    def test_demo1(self):
        _height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        _ret = Solution2().trap(_height)
        self.assertEqual(_ret, 6)

    def test_demo2(self):
        _height = [4, 2, 0, 3, 2, 5]
        _ret = Solution2().trap(_height)
        self.assertEqual(_ret, 9)

    def test_demo3(self):
        _height = []
        _ret = Solution2().trap(_height)
        self.assertEqual(_ret, 0)

    def test_demo4(self):
        _height = [4]
        _ret = Solution2().trap(_height)
        self.assertEqual(_ret, 0)

    def test_demo5(self):
        _height = [1, 0, 2]
        _ret = Solution2().trap(_height)
        self.assertEqual(_ret, 1)


if __name__ == '__main__':
    unittest.main()
