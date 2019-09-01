#!/usr/bin/env python
#!coding:utf-8


"""
实现单向链表
"""


class SingleNode(object):
    """单链表节点"""
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    """单链表"""
    def __init__(self):
        self.__head = None

    def add(self, item):
        """在头部插入节点"""
        node = SingleNode(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """尾部插入节点"""
        if self.__head:  # 非空
            cur = self.__head
            while cur:
                cur = cur.next
            node = SingeNode(item)
            cur.next = node
