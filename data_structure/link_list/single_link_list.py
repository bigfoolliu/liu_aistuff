#!/usr/bin/env python
#!coding:utf-8


"""
单向链表以及相关涉及到的算法题
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
        cur = self.__head
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


def reverse_single_link_list(head):
    """
    单链表反转四种方式：https://www.cnblogs.com/petrolero/p/9822008.html
    head: 单链表头节点
    
    head--->1--->2--->3
    head<---1<---2<---3
    """
    if head == None or head.next == None:
        return head
    cur = head
    tmp = None  # 临时节点
    new_head = None  # 新的头节点

    while cur:
        tmp = cur.next  # 临时保存当前节点的下一个节点
        cur.next = new_head  # 断开当前节点和后一个节点的连接
        new_head = cur  # 设置当前节点为新的头节点
        cur = tmp  # 将临时节点设置为当前节点
    return new_head


if __name__ == '__main__':
    # 1-->2-->3-->4
    head = SingleNode(1)
    head.next = SingleNode(2)
    head.next.next = SingleNode(3)
    head.next.next.next = SingleNode(4)

    new_head = reverse_single_link_list(head)
    print(new_head.item)
    assert new_head.item == 4
