#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu

"""
"""
class Node(object):

    def __init__(self, data):
        self.left = None
        self.rght = None
        self.data = data


class BasicBinaryTree(object):

    def __init__(self):
        self.left_child = None
        self.right_child = None
        
