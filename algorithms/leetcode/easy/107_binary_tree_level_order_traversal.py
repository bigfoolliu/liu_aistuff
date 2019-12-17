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


from collections import deque


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
    if not root:
        return []

    ret = [[root.val]]  # 存储最后的结果
    q = deque([root])

    while q:
        level_ret = []
        for _ in range(0, len(q)):
            root = q.popleft()
            if root.left:
                level_ret.append(root.left.val)
                q.append(root.left)
            if root.right:
                level_ret.append(root.right.val)
                q.append(root.right)
        if level_ret:
            ret.append(level_ret)
    
    return ret[::-1]


if __name__ == "__main__":
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.left.left = Node(15)
    root.left.right = Node(7)

    print(binary_tree_level_order_travelsal(root))
