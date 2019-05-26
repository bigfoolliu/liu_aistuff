#!/usr/bin/env python
#!coding: utf-8


"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.
    Example 2:

    Input: "cbbd"
    Output: "bb"
"""


"""
回文问题
"""


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    l, r = 0, 0

    for i in range(len(s)):
        for j in range(min(i + 1, len(s) - i)):
            if s[i - j] != s[i + j]:
                break
            if 2 * j + 1 > m:
                m = 2 * j + 1
                l = i - j
                r = i + j

        if i + 1 < len(s) and s[i] == s[i + 1]:
            for j in range(min(i + 1, len(s) - i -1)):
                if s[i - j] != s[i + j + 1]:
                    break
                if 2 * j + 2 > m:
                    m = 2 * j + 2
                    l = i - j
                    r = i + j + 1

    return s[l:r+1]



