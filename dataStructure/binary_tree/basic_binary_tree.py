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


def display_tree_deep(root):
    """展示二叉树,深度优先"""
    if root is None:
        return
    print(root.data)
    display_tree_deep(root.left)
    display_tree_deep(root.right)


def display_tree_wild(root):
    """展示二叉树,广度优先,又叫层次遍历"""
    if root is None:
        return
    queue = []
    queue.append(root)
    while queue:
        cur = queue.pop(0)
        print(cur.data)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)


def pre_travel(root):
    """深度优先,前序遍历,即：当前节点-->左子树-->右子树"""
    print(root.data)
    if root.left is not None:
        pre_travel(root.left)
    if root.right is not None:
        pre_travel(root.right)


def after_travel(root):
    """深度优先,后序遍历,即：左子树-->右子树-->当前节点"""
    if root.left is not None:
        after_travel(root.left)
    if root.right is not None:
        after_travel(root.right)
    print(root.data)


def mid_travel(root):
    """深度优先,中序遍历,即：左子树-->当前节点-->右子树"""
    if root.left is not None:
        mid_travel(root.left)
    print(root.data)
    if root.right is not None:
        mid_travel(root.right)


def depth_of_tree(root):
    """显示树的深度"""
    if root is None:
        return 0
    return max(depth_of_tree(root.left), depth_of_tree(root.right)) + 1


def is_full_binary_tree(root):
    """是否为完全二叉树，即最底层叶节点均处于次底层叶节点的左侧"""
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return is_full_binary_tree(root.left) and is_full_binary_tree(root.right)
    return False


def is_same_tree(root1, root2):
    """判断两棵树是否相同"""
    if root1 is None and root2 is None:
        return True
    elif root1 and root2:
        return root1.data == root2.data and is_same_tree(root1.left, root2.left) and is_same_tree(root1.right, root2.right)
    else:
        return False


def main():
    """构造一棵结构为下方的数
            0
          /   \
         1     2
       /   \
      3     4
    """
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)

    print("display the tree deep:")
    display_tree_deep(root)
    
    print("display the tree wild:")
    display_tree_wild(root)

    print("pre travel:")
    pre_travel(root)

    print("after travel:")
    after_travel(root)

    print("mid travel:")
    mid_travel(root)

    print("depth of the tree: {}".format(depth_of_tree(root)))
    print("is full binary tree: {}".format(is_full_binary_tree(root)))


if __name__ == "__main__":
    main()
