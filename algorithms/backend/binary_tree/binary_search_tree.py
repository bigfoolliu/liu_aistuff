#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
二叉搜索树

空树或者具有以下特征：
1.左子树不空则左子树上所有节点的值均小于根节点的值
2.右子树不空则右子树上所有节点的值均大于根节点的值
3.左右子树分别为二叉排序树

                12
            /       \
          5          18
        /   \      /    \
       2     9    15     19
"""


class Node(object):
    """
    self.label: 节点的数据域，即节点的数值
    self.parent: 该节点的父节点
    self.left: 左子树节点
    self.right: 右子树节点
    """
    def __init__(self, label, parent):
        self.label = label
        self.parent = parent
    
    def get_label(self):
        return self.label
    
    def set_label(self, label):
        self.label = label
    
    def get_left(self):
        return self.left
    
    def set_left(self, left):
        self.left = left
    
    def get_right(self):
        return self.right
    
    def set_right(self, right):
        self.right = right
    
    def get_parent(self):
        return self.parent
    
    def set_parent(self, parent):
        self.parent = parent


class BinarySearchTree(object):

    def __init__(self):
        self.root = None
    
    def is_empty(self):
        if not self.root:
            return True
        return False
    
    def get_node(self, label):
        """找到指定数据域的节点"""
        cur_node = None
        if not self.is_empty():
            cur_node = self.root
            while cur_node is not None and cur_node.get_label() is not label:
                if label < cur_node.get_label():
                    cur_node = cur_node.get_left()
                else:
                    cur_node = cur_node.get_right()
            
            return cur_node
    
    def insert(self, label):
        """
        向二叉搜索树中插入一个节点
        1.根节点为空则设置该节点为根节点
        2.需要找到该新节点的父节点
        3.从根节点开始查找：
            新节点的值小于该节点，则应该处于左子树，继续
            新节点的值大于该节点，则应该处于右子树，继续
        4.一直找到最后叶子节点
        """
        new_node = Node(label, None)
        if self.is_empty():
            self.root = new_node
        else:
            cur_node = self.root
            # 找到新建节点的父节点
            while cur_node is not None:
                parent_node = cur_node
                if new_node.get_label() < cur_node.get_label():
                    cur_node = cur_node.get_left()
                else:
                    cur_node = cur_node.get_right()
            
            # 找到父节点之后，则根据其数据域判断放置在父节点的左侧还是右侧
            if new_node.get_label() < parent_node.get_label():
                parent_node.set_left(new_node)
            else:
                parent_node.set_right(new_node)
            
            new_node.set_parent(parent_node)
    
    def delete(self, label):
        """
        删除二叉搜索树的一个节点
        1.首先找到数据域为该值的节点
        2.找到之后
        """
        if not self.is_empty():
            node = self.get_node(label)
            if node:
                # TODO:



def main():
    pass


if __name__ == "__main__":
    main()
