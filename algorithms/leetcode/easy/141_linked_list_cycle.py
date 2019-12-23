#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.


Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


 

Follow up:

Can you solve it using O(1) (i.e. constant) memory?


给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。 
"""


class Node(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head):
    """
    :param head: Node
    :return: bool
    """
    if not head:
        return False
    
    # 遍历的过程中将值置为None
    while head.next and head.val != None:
        head.val = None
        head = head.next
    
    # 如果有节点的下一个节点为None,则说明有环
    if not head.next:
        return False
    return True


if __name__ == "__main__":
    head = Node(3)
    node2 = Node(2)
    node0 = Node(0)
    node4 = Node(4)

    head.next = node2
    node2.next = node0
    node0.next = node4

    # node4.next = node2

    print(has_cycle(head))