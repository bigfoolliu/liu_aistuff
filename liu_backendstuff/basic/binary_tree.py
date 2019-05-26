#!/usr/bin/env python
#!coding:utf-8


"""
二叉树的实现
"""


class Node(object):
    """树的节点"""
    def __init__(self, item, lchild=None, rchild=None):
        self.item = item
        self.lchild = lchild
        self.rchild - rchild


class Queue(object):
    """队列,先进先出"""
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """入列"""
        self.items.insert(0, item)

    def dequeue(self):
        """出列"""
        return self.items.pop()


class BinaryTree(object):
    """二叉树"""
    def __init__(self, root=None):
        self.__root = root

    def add(self, item):
        """为树添加节点"""
        node = Node(item)
        queue = []  # 初始化根节点入队列
        queue.insert(0, self.__root)
        while queue:
            cur = queue.pop(0)
            if cur.lchild == None:
                cur.lchild = node
                return
            queue.insert(0, cur.lchild)
            if cur.rchild == None:
                cur.rchild = node
                return
            queue.insert(0. cur.rchild)

    def travel(self):
        """遍历显示树的节点，广度优先，层次遍历"""
        queue = []
        queue.insert(0, self.__root)
        while queue:
            cur = queue.pop(0)
            print(cur.item)

            if cur.lchild:
                queue.insert(0, cur.lchild):
            if cur.lchild:
                queue.insert(0, cur.rchild)

    def pre_order(self):
        """使用深度优先的先序遍历进行节点输出,根节点-->左子树-->右子树"""
        root = self.__root
        def preorder(root):
            if not root:
                return None
            print(root.item)
            preorder(root.lchild)
            preorder(root.rchild)
        return preorder(root)
