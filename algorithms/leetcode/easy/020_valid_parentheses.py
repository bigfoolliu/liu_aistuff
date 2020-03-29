#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

判断括号是否合法

思路：栈
"""


def is_valid_parentheses(s):
    """
    :param s: str，输入一串只包含括号[]()\{\}的字符串
    return bool
    """
    if s == "":
        return True
    parentheses_map = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    stack = []
    for i in list(s):
        # 若为左半边括号则压入栈中
        if i in parentheses_map:
            stack.append(i)
        # 若为右半边的括号则分类讨论
        else:
            # 如果此时的栈为空或者末尾取出来的元素和当前的不匹配则说明顺序不对
            if len(stack) == 0 or parentheses_map[stack[len(stack)-1]] != i:
                return False
            # 栈尾元素取出来和当前对应则压出元素
            else:
                stack.pop()
    # 当最后的栈为空则说明正确
    return len(stack) == 0


if __name__ == "__main__":
    s1 = r"[({})]"
    print(s1, is_valid_parentheses(s1))

    s2 = r"}[]()"
    print(s2, is_valid_parentheses(s2))

    s3 = r"[](){}{"
    print(s1, is_valid_parentheses(s3))
