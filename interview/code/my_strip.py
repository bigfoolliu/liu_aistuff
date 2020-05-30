#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
自己实现str的strip方法
"""


def my_lstrip(target_str, strip_str):
    """
    将字符串左侧的连续出现的字符替换为指定字符
    target_str: 待替换的字符串
    strip_str: 替换使用的字符串
    """
    if not target_str:
        return ""

    # 重复判断首个字符是否为需要替换的字符
    while len(target_str) >= 0 and target_str[0] == strip_str:
        target_str = target_str[1:]
    return target_str


def my_rstrip(target_str, strip_str):
    """
    将字符串右侧的连续出现的字符替换为指定字符
    target_str: 待替换的字符串
    strip_str: 替换使用的字符串
    """
    if not len(target_str) > 0:
        return ""

    while len(target_str) >= 0 and target_str[-1] == strip_str:
        target_str = target_str[:-1]
    return target_str


s = "ggghelloppp"
print(s)

ret = my_lstrip(s, "g")
print(ret)
assert ret == "helloppp"

ret2 = my_rstrip(s, "p")
print(ret2)
assert ret2 == "ggghello"
