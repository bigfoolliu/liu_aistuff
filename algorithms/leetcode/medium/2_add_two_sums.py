#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
"""


class Node:

    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    将链表转换为数字，相加后的结果在转换会链表
    :type l1: Node
    :type l2: Node
    :rtype: Node
    """
    if not l1 and not l2:
        return
    elif not l1:
        return l2
    elif not l2:
        return l1
    else:
        # transfer to list
        list1 = [l1.val]
        list2 = [l2.val]

        while l1.next:
            list1.append(l1.next.val)
            l1 = l1.next
        while l2.next:
            list2.append(l2.next.val)
            l2 = l2.next

        # calculate the result
        num1 = int("".join(str(i) for i in list1[::-1]))
        num2 = int("".join(str(i) for i in list2[::-1]))
        ret_num = num1 + num2

        # transfer the ret to listNode
        tmp = str(ret_num)[::-1]
        ret = Node(int(tmp[0]))  # 头节点，需要返回的节点

        tmp_head = ret
        for i in range(1, len(tmp)):
            tmp_node = Node(int(tmp[i]))
            tmp_head.next = tmp_node
            tmp_head = tmp_head.next

        return ret


if __name__ == "__main__":
    l1 = Node(2)
    l1.next = Node(4)
    l1.next.next = Node(3)

    l2 = Node(5)
    l2.next = Node(6)
    l2.next.next = Node(4)
    l2.next.next.next = Node(9)

    ret_node = addTwoNumbers(l1, l2)
    print(ret_node.val)
    print(ret_node.next.val)
    print(ret_node.next.next.val)
    print(ret_node.next.next.next.val)
