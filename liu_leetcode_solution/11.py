#!/usr/bin/env python
#!coding:utf-8


"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

![](https://github.com/apachecn/awesome-algorithm/blob/master/images/011/question_11.jpg)


Example:

    Input: [1,8,6,2,5,4,8,3,7]
    Output: 49
"""

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    l, r, max_area = 0, len(height) - 1, 0
    print("original l:{}, r:{}".format(l, r))
    while l <= r:
        area = (r - l) * min(height[l], height[r])
        max_area = max(area, max_area)
        if height[l] < height[r]:
            l += 1
        elif height[l] > height[r]:
            r -= 1
        else:
            l += 1
            r -= 1
    print("l:{}, r:{}".format(l, r))
    return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print("input:{}, result:{}".format(height, maxArea(height)))

height = [1, 2, 3, 4, 5, 6]
print("input:{}, result:{}".format(height, maxArea(height)))
