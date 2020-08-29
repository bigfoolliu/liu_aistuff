#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
io模块的简单实例

https://www.cnblogs.com/zhangxinqi/p/9135038.html

主要有三种类型的I/O:

1. 文本I/O
2. 二进制I/O
3. 原始I/O
"""

import io


def file_io_demo():
    """文本I/O实例"""
    # 常用使用文件创建文本流
    with open("./test.log", "r", encoding="utf-8") as f:
        print(f, type(f))

    # 使用StringIO对象来创建内存中的文本流
    f1 = io.StringIO("some text data")
    print(f1.getvalue(), type(f1))


def binary_io_demo():
    """二进制I/O实例"""
    # 通过读取文件创建二进制流
    with open("./io_test.jpg", "rb") as f:
        print(f, type(f))

    # 通过BytesIO创建二进制流
    f1 = io.BytesIO(b"some binary data:\x00\x01")
    print(f1, f1.getvalue())


def original_io_demo():
    """原始I/O,也被称为无缓冲I/O"""
    # 设置buffering为0就是禁止缓冲
    with open("./io_test.jpg", "rb", buffering=0) as f:
        print(f, type(f))


if __name__ == "__main__":
    # file_io_demo()
    # binary_io_demo()
    original_io_demo()
