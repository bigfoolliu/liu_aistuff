#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

将有序数组转换为二叉搜索树

区间分治方法
"""


class Node(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sortedArrayToBST(array):
    """
    :param array: list[int],有序数组
    :return: Node
    """
    if array:
        mid_pos = len(array) // 2
        mid_node = array[mid_pos]
        root = Node(mid_node)

        # 递归，根据二叉搜索树的特点，中间的数是根节点
        root.left = sortedArrayToBST(array[:mid_pos])
        root.right = sortedArrayToBST(array[mid_pos+1:])
        return root


if __name__ == "__main__":
    array = [-10, -3, 0, 5, 9]
    print(sortedArrayToBST(array))
