#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

判断一棵二叉树是否高度平衡，即左右子树的高度相差不超过1
"""


class Node(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_balanced(root):
    """
    使用深度优先的方式判断左右子树的深度差是否超过1
    :param root: Node
    :return: bool
    """
    def dfs(p):
        if not p:
            return 0
        
        left_height = dfs(p.left)
        right_height = dfs(p.right)

        if left_height == -1 or right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return 1 + max(left_height, right_height)
    
    if dfs(root) == -1:
        return False
    return True


def test_true():
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    print(is_balanced(root))


def test_false():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(3)
    root.left.left.left = Node(4)
    root.left.left.right = Node(4)
    print(is_balanced(root))


if __name__ == "__main__":
    test_true()
    test_false()
