#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
二叉搜索树的实现
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
        self.left = None
        self.right = None
    
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

    def __is_right_children(self, node):
        """判断当前节点是否为右子树的节点"""
        if (node == node.get_parent().get_right()):
            return True
        return False

    def __reassign_node(self, node, new_children):
        """在某节点下重新分配一个新的节点，替换掉原先的节点，即将node替换为new_children"""
        # 如果新的子节点存在，则将新节点的父节点设置为同级节点的父节点
        if new_children:
            new_children.set_parent(node.get_parent())
        # 如果同级节点的父节点存在，则判断该新节点是应该设置为左节点还是右节点
        if node.get_parent():
            if self.__is_right_children(node):
                node.get_parent().set_right(new_children)
            else:
                node.get_parent().set_left(new_children)

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
    
    def get_max(self, root=None):
        """找到指定根节点下的数据域最大的节点"""
        if root:
            cur_node = root
        else:
            cur_node = self.root
        if not self.is_empty():
            while cur_node.get_right():
                cur_node = cur_node.get_right()
        return cur_node

    def get_min(self, root=None):
        """找到整个二叉搜索树的数据域最小的节点"""
        if root:
            cur_node = root
        else:
            cur_node = self.root
        if not self.is_empty():
            while cur_node.get_left():
                cur_node = cur_node.get_left()
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
                # 如果待删除节点的左右子节点都不存在，则将其置为None，也说明其为叶子节点
                if not node.get_left() and not node.get_right():
                    self.__reassign_node(node, None)
                # 如果待删除节点的左右子节点只有右子节点，将其自身置为自己的右子节点
                elif not node.get_left() and node.get_right():
                    self.__reassign_node(node, node.get_right())
                # 如果待删除节点的左右子节点只有左子节点，将其自身置为自己的左子节点
                elif node.get_left() and not node.get_right():
                    self.__reassign_node(node, node.get_left())
                # 如果待删除节点同时有左节点和右节点,将左节点替换掉为自身，同时调整子节点下的结构
                else:
                    tmp_node = self.get_max(node.get_left())
                    self.delete(tmp_node.get_label())
                    node.set_label(tmp_node.get_label())


def main():
    bst = BinarySearchTree()
    bst.insert(12)
    bst.insert(5)
    bst.insert(18)
    bst.insert(2)
    bst.insert(9)
    bst.insert(15)
    bst.insert(19)
    bst.insert(13)

    bst.delete(18)
    print(bst)


if __name__ == "__main__":
    main()
 