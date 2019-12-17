#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]

二叉树的层次遍历
"""


class Node(object):

      def __init__(self, x):
          self.val = x
          self.left = None
          self.right = None


def binary_tree_level_order_travelsal(root):
    """
    :param root: Node
    :return: list[list[int]]
    """
    pass
