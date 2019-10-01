#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


class Stack(object):

    def __init__(self):
        self._items = []
    
    def is_empty(self):
        return self._items == []
    
    def push(self, item):
        """进栈"""
        self._items.append(item)
    
    def pop(self):
        """出栈"""
        return self._items.pop()
    
    def peek(self):
        """查看最后一个元素"""
        return self._items[len(self._items)-1]
