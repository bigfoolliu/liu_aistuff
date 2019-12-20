#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

给一个二叉树，返回其最小的深度
"""


class Node(object):
    
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def minimum_depth_of_binary_tree(root):
    """
    :param root: Node
    :return: int
    """
    if not root:
        return 0
    
    left_depth = minimum_depth_of_binary_tree(root.left)
    right_depth = minimum_depth_of_binary_tree(root.right)

    if not left_depth and not right_depth:
        return 1
    elif not left_depth:
        return 1 + right_depth
    elif not right_depth:
        return 1 + left_depth
    else:
        return 1 + min(left_depth, right_depth)


if __name__ == "__main__":
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    # root.left.left = Node(10)
    root.right.left = Node(15)
    root.right.right = Node(7)

    print(minimum_depth_of_binary_tree(root))
