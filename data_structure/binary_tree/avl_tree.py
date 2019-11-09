#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
平衡二叉树python实现

avl树实现
"""
import math
import random


class queue(object):
    """实现简易队列"""

    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = 0
    
    def is_empty(self):
        return self.head == self.tail
    
    def push(self, data):
        """入队列"""
        self.data.append(data)
        self.tail = self.tail + 1
    
    def pop(self):
        """出队列"""
        ret = self.data[self.head]
        self.head = self.head + 1
        return ret
    
    def count(self):
        return self.tail - self.head
    
    def queue_print(self):
        """队列打印"""
        print(self.data)
        print("***********")
        print(self.data[self.head:self.tail])


class Node(object):
    """平衡二叉树节点"""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1  # 平衡二叉树的高度
    
    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data
    
    def get_left(self):
        return self.left
    
    def set_left(self, node):
        self.left = node
        return
    
    def get_right(self):
        return self.right
    
    def set_right(self, node):
        self.right = node
        return
    
    def get_height(self):
        return self.height
    
    def set_height(self, height):
        self.height = height
        return


def get_height(node):
    """获取节点的高度"""
    if node is None:
        return 0
    return node.get_height()


def left_rotation(node):
    r"""
    将节点左翻转,即：LR翻转
            A                    B
          /   \                /   \
        B      C              Bl    A  
       /  \         --->     /     / \
      Bl   Br               UB    Br  C
     /
    UB
    UB: unbalanced node
    传入的参数node为节点A
    """
    print("left rotation node:{}".format(node.get_data()))
    ret = node.get_left()  # ret为节点B
    node.set_left(ret.get_right())  # 将A的左子树设置为B的右子树
    ret.set_right(node)  # B的右子树设置为A
    h1 = max(get_height(node.get_right()), get_height(node.get_left())) + 1  # 获取A的左右子树的高度最大值并加1
    node.set_height(h1)  # 将A的高度设置为新的值
    h2 = max(get_height(ret.get_left()), get_height(ret.get_right())) + 1  # 获取B的左右子树的高度最大值加1
    ret.set_height(h2)  # 将B的高度设置为新的值
    return ret


def right_rotation(node):
    r"""
    将节点右翻转，即：RR翻转
            A                    C
          /   \                /   \
        B      C              A     Cr
              /  \    --->   /  \    \
             Cl   Cr        B   Cl   UB
                   \
                   UB
    UB: unbalanced node
    传入的参数node为节点A
    """
    print("right rotation node:{}".format(node.get_data()))
    ret = node.get_right()  # ret为节点C
    node.set_right(ret.get_left())  # 将A的右子树设置为C的左子树
    ret.set_left(node)  # C的左子树设置为A
    h1 = max(get_height(node.get_left()), get_height(node.get_right())) + 1  # 获取A的左右子树的高度最大值加1
    node.set_height(h1)  # 将A的高度设置为新值
    h2 = max(get_height(ret.get_left()), get_height(ret.get_right())) + 1  # 获取C的左右子树的高度最大值加1
    ret.set_height(h2)  # 将C的高度设置为新值
    return ret


def rl_rotation(node):
    r"""
    先右翻转，再左翻转
         A                 A                Br
        / \               / \              /  \
        B  C    RR       Br  C    LR      B    A
       / \      --->    /  \      --->   /    / \
      Bl  Br           B   UB           Bl   UB  C
            \         /
            UB       Bl
    RR = right_rotation
    LR = left_rotaiton
    传入的参数node为节点A
    """
    node.set_left(right_rotation(node.get_left()))  # 将A的左子树B进行右翻转，然后将A的左子树设置为右翻转的结果
    return left_rotation(node)  # 将A进行左翻转


def lr_rotation(node):
    r"""
    先左翻转，再右翻转
         A                 A                    Cl
        / \               / \                  /  \
        B  C      LR     B   Cl        RR     A    C
          / \     --->      /  \      --->   / \    \
         Cl  Cr            UB   C           B   UB   Cr
        /                        \
       UB                         Cr 
    RR = right_rotation
    LR = left_rotaiton
    传入的参数node为节点A
    """
    node.set_right(left_rotation(node.get_right()))  # 将A的右子树C进行左翻转，然后将A的右子树设置为左翻转的结果
    return right_rotation(node)  # 将A进行右翻转


def insert_node(node, data):
    """插入节点"""
    print("node is:{}, data is:{}".format(node, data))
    if node is None:
        return Node(data)
    # 根据插入的数据的大小确定是在左节点还是右节点
    # 待插入的数据小于节点的值，应该放置在左子树的位置
    if data < node.get_data():
        node.set_left(insert_node(node.get_left(), data))
        if get_height(node.get_left()) - get_height(node.get_right()) == 2:  # 发现不平衡
            if data < node.get_left().get_data():
                node = left_rotation(node)
            else:
                node = rl_rotation(node)
    else:
        node.set_right(insert_node(node.get_right(), data))
        if get_height(node.get_right()) - get_height(node.get_left()) == 2:
            if data < node.get_right().get_data():
                node = lr_rotation(node)
            else:
                node = right_rotation(node)
    h1 = max(get_height(node.get_left()), get_height(node.get_right())) + 1
    node.set_height(h1)
    return node


def get_left_most(root):
    """获取最左侧的子树"""
    while root.get_left() is not None:
        root = root.get_left()
    return root.get_data()


def get_right_most(root):
    """获取最右侧的子树"""
    while root.get_right() is not None:
        root = root.get_right()
    return root.get_data()


def delete_node(root, data):
    """
    删除节点
    root: avl树的根节点
    data: 待删除节点的数值
    """
    # 删除的节点为根节点
    if root.get_data() == data:
        if root.get_left() is not None and root.get_right() is not None:
            tmp_data = get_left_most(root.get_right())
            root.set_data(tmp_data)
            root.set_right(delete_node(root.get_right(), tmp_data))
        elif root.get_left() is not None:
            root = root.get_left()
        else:
            root = root.get_right()
    # 删除的节点在左子树
    elif root.get_data() > data:
        if root.get_left() is None:
            print("No such data.")
            return root
        else:
            root.set_left(delete_node(root.get_left(), data))
    # 删除的节点在右子树
    elif root.get_data() < data:
        if root.get_right() is None:
            print("No such data.") 
            return root
        else:
            root.set_right(delete_node(root.get_right(), data))
    
    if root is None:
        return root
    
    # 如果右侧子树的高度比左侧高2
    if get_height(root.get_right()) - get_height(root.get_left()) == 2:
        if get_height(root.get_right().get_right()) > get_height(root.get_right().get_left()):
            root = right_rotation(root)
        else:
            root = lr_rotation(root)
    # 如果左侧子树的高度比右侧高2
    elif get_height(root.get_right()) - get_height(root.get_left()) == -2:
        if get_height(root.get_left().get_left()) > get_height(root.get_left().get_right()):
            root = left_rotation(root)
        else:
            root = rl_rotation(root)
    
    h = max(get_height(root.get_left()), get_height(root.get_right())) + 1
    root.set_height(h)
    return root


class AvlTree(object):

    def __init__(self):
        self.root = None
    
    def get_height(self):
        """获取avl树的高度"""
        return get_height(self.root)
    
    def insert_node(self, data):
        """avl树插入节点"""
        print("self.insert_node: {}".format(str(data)))
        self.root = insert_node(self.root, data)
    
    def delete_node(self, data):
        """avl树删除节点"""
        print("delete: {}".format(str(data)))
        if self.root is None:
            print("tree is empty.")
            return
        self.root = delete_node(self.root, data)
    
    def traversale(self):
        """遍历avl树"""
        q = queue()
        q.push(self.root)
        layer = self.get_height()
        print("layer: {}".format(layer))
        if layer == 0:
            return
        
        cnt = 0
        while not q.is_empty():
            node = q.pop()
            # 输出空格
            space = " " * int(math.pow(2, layer))  # 节点之间的间隔
            print(space, end="")
            if node is None:
                print("*", end="")
                q.push(None)
                q.push(None)
            else:
                print(node.get_data(), end="")
                q.push(node.get_left())
                q.push(node.get_right())
            print(space, end="")

            cnt += 1
            for i in range(100):
                if cnt == math.pow(2, i) - 1:
                    layer -= 1
                    if layer == 0:
                        print()
                        print("*" * 30)
                        return
                    print()
                    break
        print()
        print("*" * 30)
        return
    
    def test(self):
        get_height(None)
        print("*" * 30)
        self.get_height()


if __name__ == "__main__":
    avl_tree = AvlTree()
    avl_tree.traversale()

    l = list(range(10))
    random.shuffle(l)

    for i in l:
        avl_tree.insert_node(i)
        avl_tree.traversale()
    print("avl_tree height:{}".format(avl_tree.get_height()))

    for i in l:
        avl_tree.delete_node(i)
        avl_tree.traversale()
