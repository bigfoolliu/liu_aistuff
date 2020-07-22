#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

    Input: "abcabcbb"
    Output: 3 
    Explanation: The answer is "abc", with the length of 3. 
    Example 2:

    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    Example 3:

    Input: "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3. 
                 Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

找到没有重复的最长子序列

思路：
"""


def length_of_longest_substring(s):
    """
    :type s: s
    :rtype: int
    """
    # define the result and the target substring
    ret = 0
    start = 0  # 每次不重复子串的首字母的下标
    dict1 = {}  # 存放不重复的字符的hashmap

    for i in range(len(s)):
        # 当后面的字符不在dict1中的时候，ret的结果加1
        start = max(start, dict1.get(s[i], -1)+1)
        ret = max(ret, i-start+1)
        dict1[s[i]] = i

    print(dict1)
    return ret


if __name__ == "__main__":
    # print(length_of_longest_substring("pwwkew"))
    # print(length_of_longest_substring("pwwksdfsdfew"))
    print(length_of_longest_substring("pwwasdgfgddddddkew"))
