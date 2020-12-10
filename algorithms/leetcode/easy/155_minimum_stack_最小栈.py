#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.


设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
"""


class MinimumStack(object):
    """
    实现类似栈的结构，但是要有常数时间，可以在存储单个节点的时候存储当前栈的最小值
    """

    def __init__(self):
        self.stack = []

    def push(self, x):
        """
        :param x: int
        :return: None
        """
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][-1])))

    def pop(self):
        """
        :return: None
        """
        self.stack.pop()

    def top(self):
        """
        :return: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :return: int
        """
        return self.stack[-1][-1]


if __name__ == "__main__":
    minimum_stack = MinimumStack()

    print(minimum_stack.push(-2))
    print(minimum_stack.push(0))
    print(minimum_stack.push(-3))

    print(minimum_stack.getMin())

    print(minimum_stack.pop())
    print(minimum_stack.top())

    print(minimum_stack.getMin())
