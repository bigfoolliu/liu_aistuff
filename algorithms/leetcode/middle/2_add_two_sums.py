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

两个非空链表，代表两个非负整数，且数字是逆向存储的
除了数字0之外，可以假设0不在首位

思路：
"""


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    # 将链表转换为数字，相加后的结果在转换会链表
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
        num1 = int(''.join(str(i) for i in list1[::-1]))
        num2 = int(''.join(str(i) for i in list2[::-1]))
        ret_num = num1 + num2

        # transfer the ret to listNode
        tmp = str(ret_num)[::-1]
        ret = ListNode(int(tmp[0]))

        for i in range(1, len(tmp)):
            ret = ListNode(int(tmp[i]))
            ret = ret.Next

        return ret
