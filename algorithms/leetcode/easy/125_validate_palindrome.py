#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
"""


import string


def validate_palindrome(s):
    """
    借助第三方模块
    :param s: str
    :return: bool
    """
    if s == "":
        return True
    
    new_s = ""
    for i in s:
        if i in string.ascii_letters or i in string.digits:
            if i in string.ascii_uppercase:
                i = i.lower()
            new_s += i
    print(new_s)
    if new_s == new_s[::-1]:
        return True
    return False


def validate_palindrome2(s):
    """
    不借助第三方模块
    :param s: str
    :return: bool
    """
    if s == "":
        return True
    
    new_s = ""
    s = s.lower()
    for i in s:
        if i.isalnum():
            new_s += i
    if new_s == new_s[::-1]:
        return True
    return False


if __name__ == "__main__":
    s = "1A man, a plan, a canal: Panama1"
    print(validate_palindrome(s))
    print(validate_palindrome2(s))
