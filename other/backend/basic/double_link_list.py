#!/usr/bin/env python
#!coding:utf-8


"""
实现双向链表
"""


class Node(object):
    """双向链表节点"""
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DoubleLinList(object):
    """双向链表"""
    def __init__(self):
        self.__head = None

    def add(self, item):
        """头部添加节点"""
        node = Node(item)
        node.next = self.__head
        self.__head.prev = node
        self.__head = node

    def append(self, item):
        node = Node(item)
        cur = self.__head
        while cur:
            cur = cur.next
        cur.next = node
        node.prev = cur


