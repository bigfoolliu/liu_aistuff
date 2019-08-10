#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
一般二叉树
需要对递归的知识进行多加了解
二叉树的几个种类: https://www.cnblogs.com/love-yh/p/7423301.html

应用：
1.二叉排序树既有链表的好处（删除和插入元素较快，但是查找很慢），又有数组的好处（查找很快，但是插入和删除元素很慢）
2.在处理大批量的动态数据时候比较有用
3.文件系统和数据库系统一般都采用树（特别是B树）的数据结构
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
