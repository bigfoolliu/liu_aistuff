#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


# kmp算法
# 一种无回溯的更高效的字符串匹配算法

# 比如字符集为 abcdabcdefabcdefg
# 需要匹配的为 abcdefg

# 1. 首先匹配到第一个a-e不匹配
# 2. 将abcdefg直接移动至不匹配的a位置
# 3. 匹配到第一个g-a不匹配
# 4. 将abcdeg直接移动到第二个a
# 5. 匹配成功


# https://blog.csdn.net/weixin_39561100/article/details/80822208


def kmp_matching(original, substring):
    """
    kmp匹配算法 Main Function
    original: 带匹配的原始字符串
    substring: 待匹配字符串
    return: 匹配成功的首字母的下标
    """
    pnext = gen_pnext(substring)
    print(pnext)
    m, n = len(original), len(substring)
    i, j = 0, 0
    while i < m and j < n:
        if original[i] == substring[j]:
            i += 1
            j += 1
        elif j != 0:
            j = pnext[j-1]
        else:
            i += 1
    if j == n:
        return i-j
    else:
        return -1


def gen_pnext(substring):
    """
    产生前缀表
    substring: 待匹配字符窜
    """
    index = 0
    i = 1
    m = len(substring)
    pnext = [0] * m  # 初始元素全部为 0
    while i < m:
        if substring[i] == substring[index]:
            pnext[i] = index + 1
            index += 1
            i += 1
        elif index != 0:
            index = pnext[index - 1]
        else:
            pnext[i] = 0
            i += 1

    return pnext


str1 = "abcdjhhdfabc"
print(kmp_matching(str1, "jhh"))
