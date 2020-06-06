#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:
begin to intersect at node c1.

Example 1:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
 
Example 2:

Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
 
Example 3:

Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.


编写一个程序，找到两个单链表相交的起始节点。
"""


class Node(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def intersection_of_two_linked_list(head_a, head_b):
    """
    使两个链表到达相等位置时走过的是相同的距离，链表1长度是x1+y，链表2长度是x2+y，同时遍历到达末尾时，再指向另一个链表。
    - 则当两链表走到相等的位置时：x1+y+x2 = x2+y+x1
    - 当两个链表没有相交的时候：两个链表的
    :param head_a: Node
    :param head_b: Node
    :return: Node
    """
    if not head_a or not head_b:
        return None
    pa = head_a
    pb = head_b
    while pa is not pb:
        pa = head_b if pa is None else pa.next
        pb = head_a if pb is None else pb.next
    return pa


if __name__ == "__main__":
    # 链表1，包含所有
    node4 = Node(4)
    node1 = Node(1)
    node8 = Node(8)
    node41 = Node(4)
    node5 = Node(5)

    node4.next = node1
    node1.next = node8
    node8.next = node41
    node41.next = node5

    # 链表2，只包含到相交节点之前
    node51 = Node(5)
    node0 = Node(0)
    node11 = Node(1)

    node51.next = node0
    node0.next = node11
    # node11.next = node8

    print(intersection_of_two_linked_list(node4, node51))
    print(intersection_of_two_linked_list(node4, node51).val)
