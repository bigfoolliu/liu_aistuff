#!/usr/bin/env python
#!coding:utf-8


"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, and characters like . or *.
    Example 1:

    Input:
    s = "aa"
    p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".
    Example 2:

    Input:
    s = "aa"
    p = "a*"
    Output: true
    Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
    Example 3:

    Input:
    s = "ab"
    p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".
    Example 4:

    Input:
    s = "aab"
    p = "c*a*b"
    Output: true
    Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
    Example 5:

    Input:
    s = "mississippi"
    p = "mis*is*p*."
    Output: false
"""


def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    m, n = len(s), len(p)
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

    dp[0][0] = 1

    for i in range(2, n + 1):
        if p[i - 1] == "*":
            dp[0][i] = dp[0][i - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                if p[j - 2] != s[i - 1] and p[j - 2] != ".":
                    dp[i][j] = dp[i][j - 2]
                elif p[j - 2] == s[i - 1] or p[j - 2] == ".":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 2]

            elif s[i - 1] == p[j - 1] or p[j - 1] == ".":
                dp[i][j] = dp[i - 1][j - 1]

    return dp[m][n] == 1


print("input aa, a*, true")
print("result:", isMatch("aa", "a*"))

print("input ab, .*, true")
print("result:", isMatch("ab", ".*"))

print("input aab, c*a*b*, true")
print("result:", isMatch("aab", "c*a*b*"))

print("input mississippi, mis*is*p*, false")
print("result:,", isMatch("mississippi", "mis*is*p*"))

