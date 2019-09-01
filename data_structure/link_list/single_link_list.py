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

    def insert_head(self, data):
        """在头部插入节点"""
        node = SingleNode(item)
        if self.__head:
            node.next = self.__head
        self.__head = node

    def insert_tail(self, data):
        """尾部插入节点"""
        if not self.__head:
            self.add(data)
        else:
            cur = self.__head
            while cur:  # 遍历到最后一个节点
                cur = cur.next
            cur.next = SingleNode(data)
    
    def delete_head(self):
        """删除头部节点"""
        cur = self.__head
        if self.__head:
            self.__head = self.__head.next
            cur.next = None
        return cur
    
    def delete_tail(self):
        """删除尾部节点"""
        cur = self.__head:
        if self.__head:
            if not self.__head.next:
                self.__head = None  # 只有一个头节点
            else:
                while cur.next.next:  # 找到倒数第二个节点
                    cur = cur.next
                cur.next, cur = None, cur.next
        return cur
    
    def is_empty(self):
        """判断单链表是否为空"""
        return self.__head is None
    