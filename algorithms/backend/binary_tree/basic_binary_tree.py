#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


"""
一般二叉树
需要对递归的知识进行多加了解
"""

class Node(object):
    """一般二叉树的节点"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def display_tree(tree):
    """展示二叉树的数据"""
    if tree is None:
        return None
    if tree.left:
        display_tree(tree.left)
    print(tree.data)
    if tree.right:
        display_tree(tree.right)
    display_tree(tree.right)
    return


def main():
    """构造一棵结构为下方的数
            0
          /   \
         1     2
       /   \
      3     4
    """
    tree = Node(0)
    tree.left = Node(1)
    tree.right = Node(2)
    tree.left.left = Node(3)
    tree.left.right = Node(4)
    display_tree(tree)


if __name__ == "__main__":
    main()
