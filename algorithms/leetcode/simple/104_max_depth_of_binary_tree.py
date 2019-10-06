#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

求取二叉树的最大深度。
"""


class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def max_depth_of_binary_tree(root):
    """
    :param root: tree_node
    return int
    """
    if not root:
        return 0
    q, depth = [root, None], 1
    while q:
        node = q.pop(0)
        if node:
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        elif q:
            q.append(None)
            depth += 1
    return depth


if __name__ == "__main__":
    array = [3, 9, 20, None, None, 15, 7]
    root = Node(3)
    root.left = 
    print(max_depth_of_binary_tree(array))
