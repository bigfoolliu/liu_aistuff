#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

将两个有序链表合并为一个有序链表
思路：递归
"""

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_sorted_lists(l1, l2):
    """
    :param l1: ListNode
    :param l2: ListNode
    :return: ListNode
    """
    if not l1:
        return l2
    if not l2:
        return l1

    start = None  # start为头节点
    if l1.val < l2.val:
        start = l1
        start.next = merge_two_sorted_lists(l1.next, l2)
    else:
        start = l2
        start.next = merge_two_sorted_lists(l1, l2.next)
    return start


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    
    print(merge_two_sorted_lists(l1, l2).val)
