#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
普通二叉树实现
"""


class Node(object):
    """一般二叉树的节点"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def display_tree(tree):
    """展示二叉树的数据,深度优先"""
    if tree is None:
        return
    if tree.left:
        display_tree(tree.left)
    print(tree.data)
    if tree.right:
        display_tree(tree.right)
    display_tree(tree.right)
    return


def depth_of_tree(tree):
    """显示树的深度"""
    if tree is None:
        return 0
    depth_l_tree = depth_of_tree(tree.left)
    depth_r_tree = depth_of_tree(tree.right)
    if depth_l_tree > depth_r_tree:
        return 1 + depth_l_tree
    return 1 + depth_r_tree


def is_full_binary_tree(tree):
    """是否为完全二叉树，即最底层叶节点均处于次底层叶节点的左侧"""
    if tree is None:
        return True
    if tree.left is None and tree.right is None:
        return True
    if tree.left is not None and tree.right is not None:
        return is_full_binary_tree(tree.left) and is_full_binary_tree(tree.right)
    return False


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

    print("display the tree:")
    display_tree(tree)
    print("depth of the tree: {}".format(depth_of_tree(tree)))
    print("is full binary tree: {}".format(is_full_binary_tree(tree)))


if __name__ == "__main__":
    main()
