#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \\     \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
"""

from collections import deque


class Node(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def has_path_sum(root, target):
    """
    使用一个队列来存储到每一个节点的节点值和到该节点的和
    :param root: Node
    :param target: int
    :return: bool
    """
    if not root:
        return False

    queue = deque([(root, root.val)])
    while queue:
        node, s = queue.popleft()
        if node.left:
            queue.append((node.left, s + node.left.val))
        if node.right:
            queue.append((node.right, s + node.right.val))
        if not node.left and not node.right and s == target:
            return True
    return False


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(4)
    root.right = Node(8)
    root.left.left = Node(11)
    root.right.left = Node(13)
    root.right.right = Node(4)
    root.left.left.left = Node(7)
    root.left.left.right = Node(2)
    root.right.right.right = Node(1)

    print(has_path_sum(root, 10))
    print(has_path_sum(root, 22))
    print(has_path_sum(root, 23))
