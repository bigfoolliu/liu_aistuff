#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


"""
红黑树
特殊的二叉查找树（bsd），每个节点上都存储位表示节点的颜色，红色或者黑色。
https://www.cnblogs.com/xuxinstyle/p/9556998.html

特性：
1.每个节点为红色或者黑色
2.根节点是黑色
3.每个叶子节点（NIL）是黑色。 [注意：这里叶子节点，是指为空(NIL或NULL)的叶子节点！]
4.如果一个节点是红色的，则它的子节点必须是黑色的。
5.从一个节点到该节点的子孙节点的所有路径上包含相同数目的黑节点。
6.一棵含有n个节点的红黑树的高度至多为2log(n+1)。
7.红黑树确保没有一条路径会比其他路径长出俩倍，因而是接近平衡的。

应用：
1.存储有序的数据，时间复杂度为O(logn)

操作：
1.添加，删除，修改，查找
2.左旋，右旋，变色，其是为了保证满足其红黑树的特性
"""


def color(node):
    """判断节点的颜色"""
    if node is None:
        return 0
    else:
        return node.color


class RedBlackTree(object):

    def __init__(self, label=None, color=0, parent=None, left=None, right=None):
        """
        label: 某个节点的值
        color: 0为black, 1为red
        """
        self.label = label
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent
    
    @property
    def sibling(self):
        """返回兄弟节点"""
        if self.parent is None:
            return None
        elif self.parent.left is self:
            return self.parent.right
        else:
            return self.parent.left

    @property
    def grandparent(self):
        """返回当前节点的祖父节点"""
        if self.parent is None:
            return None
        else:
            return self.parent.parent

    def is_left(self):
        return self.parent and self.parent.left is self

    def is_right(self):
        return self.parent and self.parent.right is self

    def rotate_left(self):
        """
        左旋：逆时针旋转两个节点，使父节点被自己的右孩子取代，自己成为自己的左孩子
        https://blog.csdn.net/lsr40/article/details/85245027
        核心是控制需要旋转节点的指向问题
        """
        parent = self.parent
        right = self.right
        self.right = right.left
        if self.right:
            self.right.parent = self
        self.parent = right
        right.left = self
        if parent is not None:
            if parent.left == self:
                parent.left = right
            else:
                parent.right = right
        right.parent = parent
        return right

    def rotate_right(self):
        """
        右旋：顺时针旋转两个节点，使父节点被自己的左孩子取代，自己成为自己的右孩子
        https://blog.csdn.net/lsr40/article/details/85245027
        """
        parent = self.parent
        left = self.left
        self.left = left.right
        if self.left:
            self.left.parent = self
        self.parent = left
        left.right = self
        if parent is not None:
            if parent.left == self:
                parent.left = left
            else:
                parent.right = left
        left.parent = parent
        return left

    def insert(self, label):
        """插入节点类似于bsd,只是多了一些限制"""
        if self.label is None:
            self.label = label
            return self
        if self.label == label:
            return self
        elif self.label > label:
            if self.left:
                self.left.insert(label)
            else:
                self.left = RedBlackTree(label, 1, self)
                self.left._inert_repair()
                # TODO:
    
    def _inert_repair(self):
        """当插入节点会破坏红黑树的结构时，需要变色等修复其结构"""
        if self.parent is None:
            self.color = 0  # 根节点为黑色
        elif color(self.parent) == 0:
            self.color = 1  # 父节点为黑色则子节点为红色
        else:
            uncle = self.parent.sibling
            if color(uncle) == 0:
                if self.is_left() and self.parent.is_right():
                    self.parent.rotate_right()
                    self.right._inert_repair()
                    # TODO: