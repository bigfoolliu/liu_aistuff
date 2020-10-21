#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python类型注解

- https://blog.csdn.net/Skr_Eric/article/details/83063971?utm_medium=distribute.pc_relevant.none-task-blog-title-2&spm=1001.2101.3001.4242

- 用 : 类型 的形式指定函数的参数类型，用 -> 类型 的形式指定函数的返回值类型。
- 然后特别要强调的是，Python 解释器并不会因为这些注解而提供额外的校验，没有任何的类型检查工作。也就是说，这
- 些类型注解加不加，对你的代码来说没有任何影响：

但这么做的好处是：

- 让别的程序员看得更明白
- 让 IDE 了解类型，从而提供更准确的代码提示、补全和语法检查（包括类型检查，可以看到 str 和 float 类型的参数被高亮提示）

使用特定的库对文件进行类型检查
pip3 install mypy
mypy test.py
"""


def add(x: int = 1, y: int = 2) -> int:
    """类型注解"""
    return x + y


def add2(x, y):
    return x + y


def add3():
    # 变量的类型注解释
    a: int = 1
    l: list = [1, 'a']

    from typing import List
    li: List[int] = [1, 3]  # 指明一个全部由整数构成的列表
    print(a, l, li)


if __name__ == '__main__':
    print(add(2, 4))
    print(add('hello', 'world'))  # ide提示类型问题
    print(add2(2, 4))  # 不会有任何提示

    print(add.__annotations__)  # 可以查看注解
    add3()
