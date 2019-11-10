#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
数据结果栈的实现

- 进栈将元素放到栈顶；出栈从栈顶取出元素
- 先进后出原则
"""
import random


class StackOverFlowError(BaseException):
    """栈溢出"""
    pass


class Stack(object):

    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit
    
    def __bool__(self):
        """调用bool(obj)的时候实际是调用对象的该魔法方法，会判断对象的真假，0时为假"""
        return bool(self.stack)
    
    def __str__(self):
        return str(self.stack)
    
    def push(self, data):
        """入栈"""
        if len(self.stack) >= self.limit:
            raise StackOverFlowError
        self.stack.append(data)
    
    def pop(self):
        """出栈"""
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError("stack is empty")
    
    def peek(self):
        """返回栈顶的元素"""
        return self.stack[-1]
    
    def size(self):
        """返回栈元素数量"""
        return len(self.stack)


if __name__ == "__main__":
    stack = Stack(limit=15)

    l = list(range(12))
    random.shuffle(l)

    for i in l:
        stack.push(i)
    
    print("stack initialize: {}".format(str(stack)))

    # 演示溢出
    # for i in range(5):
    #     stack.push(i)

    for i in range(2):
        stack.pop()
    
    print("stack after pop: {}".format(str(stack)))

    print("stack size: {}".format(stack.size()))
    print("stack peek: {}".format(stack.peek()))
