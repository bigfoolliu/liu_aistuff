#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""从尾到头打印单链表"""


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
            node = SingleNode(item)
            cur.next = node


def print_links(links):
    stacks = []
    while links:
        stacks.append(links.item)
        links = links.next
    while stacks:
        print(stacks.pop())


def main():
    links = SingleLinkList()

    # TODO:not done
    node1 = SingleNode(1)
    node2 = SingleNode(6)
    node3 = SingleNode(2)
    node4 = SingleNode(8)

    links.add(node1)
    links.append(node2)
    links.append(node3)
    links.append(node4)
    print(links)


if __name__ == '__main__':
    main()
