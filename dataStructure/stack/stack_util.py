#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
栈的一些小操作
"""

import unittest


def generate_adjective_stack(array):
    """
    输入数组，生成一个单调递增栈
    :param array: List(int)
    :return: list
    """
    if not array:
        raise ValueError

    stack = []
    for i in array:
        while stack and stack[-1] > i:
            stack.pop()
        stack.append(i)
    print(stack)
    return stack


class TestDemo(unittest.TestCase):

    def test1(self):
        _array = [2, 4, 1, 5, 6]
        self.assertEqual(generate_adjective_stack(_array), [1, 5, 6])

    def test2(self):
        _array = [1, 4, 1, 5, 6]
        self.assertEqual(generate_adjective_stack(_array), [1, 1, 5, 6])


if __name__ == '__main__':
    unittest.main()
