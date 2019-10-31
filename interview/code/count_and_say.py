#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
1
11
21
1211
111221
"""


def count_and_say(n):
    s = "1"
    for i in range(1, n):  # 遍历次数
        count = 0  # 统计次数
        tmp = s[0]  # 记录每次遇到新的数字
        ret = ""  # 记录最终结果
        for j in range(0, len(s)):
            if s[j] == tmp:
                count += 1
            else:
                ret = ret + str(count) + tmp
                tmp = s[j]
                count = 1
            if j == len(s)-1:
                ret = ret + str(count) + tmp  # 最后一次结果合并
        s = ret
    return s


print(count_and_say(5))

