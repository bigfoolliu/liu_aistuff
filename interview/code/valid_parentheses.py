#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
({}) 括号的合法性
"""


def valid(strs):
    """左括号进栈，右括号出栈，为空则为正常"""
    hash_map = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for i in strs:
        if i in hash_map:
            stack.append(i)
        else:
            if len(stack) == 0 or i != hash_map[stack[-1]]:
                return False
            else:
                stack.pop()
    return len(stack) == 0


print(valid("({[]})"))
print("-------------")
print(valid("{[}]"))
