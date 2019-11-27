#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python 字符串操作

https://www.runoob.com/python/python-strings.html
"""

def base_operation_demo():
    """基本操作"""
    a = "hello"
    b = "world"

    # 字符串拼接
    c = a + b
    d = "".join([a, b])
    print(c, d)

    # 字符串操作
    e = a * 5
    print(e)
    print("he" in a)

    # 原始字符串
    print(r"\n")

    # 三引号可以将复杂的字符串进行复制
    m = """this is me,
that is you"""
    print(m)

    # 定义一个unicode字符串
    n = u"python"
    face = chr(0x1F600)  # 表情
    print(n, type(n))
    print(face)


if __name__ == "__main__":
    base_operation_demo()
