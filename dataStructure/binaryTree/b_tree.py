#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
b树python基础实现
"""


class Entity(object):
    """数据实体"""

    def __init__(self, key, value):
        self.key = key
        self.value = value


class Node(object):
    """B树的节点"""

    def __init__(self):
        self.parent = None  # 父节点
        self.entities = []  # 数据节点
        self.childs = []  # 子节点

    def find(self, key):
        """通过key找到并返回一个数据实体"""
        for e in self.entities:
            if key == e.key:
                return e

    def delete(self, key):
        """通过key删除对应的数据实体并返回其下标"""
        for i, e in enumerate(self.entities):
            if key == e.key:
                del self.entities[i]
                return(i, e)

    def is_leaf(self):
        """判断该节点是否为叶子节点"""
        return len(self.childs) == 0

    def add_entity(self, entity):
        """添加数据实体"""
        self.entities.append(entity)
        self.entities.sort(key=lambda x: x.key)  # 数据实体根据key的大小排列

    def add_child(self, node):
        """添加一个孩子节点"""
        self.childs.append(node)
        node.parent = self
        self.childs.sort(key=lambda x: x.entities[0].key)


class BTree(object):
    """B树"""

    def __init__(self, size=10):
        self.size = size
        self.root = None
        self.length = 0

    def add(self, key, value=None):
        """插入一个节点"""
        self.length += 1
        if self.root:
            cur = self.root
            while not cur.is_leaf():
                for i, e in enumerate(cur.entities):
                    if e.key > key:
                        cur = cur.childs[i]
                        break
                    elif e.key == key:
                        e.value = value
                        self.length -= 1
                        return
                else:
                    cur = cur.childs[-1]
            cur.add_entity(Entity(key, value))

            if len(cur.entities) > self.size:
                self.__split(cur)
        else:
            self.root = Node()
            self.root.add_entity(Entity(key, value))

    def get(self, key):
        """通过key查询一个数据"""
        node = self.__find_node(key)
        if node:
            return node.find(key).value

    def delete(self, key):
        """通过key删除一个数据项并返回它"""
        node = self.__find_node(key)

        if node:
            i, e = node.delete(key)
            # 如果节点不是叶子节点时需要做修复
            if not node.is_leaf():
                child = node.childs[i]
                j, entity = child.delete(child.entities[-1], key)
                node.add_entity(entity)

                while not child.is_leaf():
                    node = child
                    child = child.childs[j]
                    j, entity = child.delete(child.entities[-1], key)
                    node.add_entity(entity)
                self.length -= 1
                return e.value

    def is_empty(self):
        """判断B树是否为空"""
        return self.length == 0

    def __find_node(self, key):
        """通过key值查询一个数据在哪个节点，找到就返回该节点"""
        if self.root:
            cur = self.root

            while not cur.is_leaf():
                for i, e in enumerate(cur.entities):
                    if e.key > key:
                        cur = cur.childs[i]
                        break
                    elif e.key == key:
                        return cur
                else:
                    cur = cur.childs[-1]
            if cur.find(key):
                return cur

    def __split(self, node):
        """
        分裂一个节点
        规则如下：

        1. 中间数据项移到父节点
        2. 新建一个右兄弟节点，将中间节点右边的数据移到新节点
        """
        middle = int(len(node.entities) / 2)  # 整数
        top = node.entities[middle]
        right = Node()

        for e in node.entities[middle+1:]:
            right.add_entity(e)

        for n in node.childs[middle+1:]:
            right.add_child(n)

        node.entities = node.entities[:middle]
        node.childs = node.childs[:middle+1]

        parent = node.parent

        if parent:
            parent.add_entity(top)
            parent.add_child(right)

            if len(parent.entities) > self.size:
                self.__split(parent)
        else:
            self.root = Node()
            self.root.add_entity(top)
            self.root.add_child(node)
            self.root.add_child(right)


if __name__ == "__main__":
    t = BTree(4)
    t.add(20)
    t.add(40)
    t.add(60)
    t.add(70, "c")
    t.add(80)
    t.add(10)
    t.add(30)
    t.add(15, "python")
    t.add(75, "java")
    t.add(85)
    t.add(90)
    t.add(25)
    t.add(35, "c#")
    t.add(50)
    t.add(22, "c++")
    t.add(27)
    t.add(32)
