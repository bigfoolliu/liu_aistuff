#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
函数标志


1..使用函数参数标注，能提示程序员应该怎样正确使用这个函数

2.以字典的形式存放在函数的 __annotations__ 属性中，并且不会影响函数的任何其他部分

3.形参标注的定义方式是在形参名称后加上冒号，后面跟一个表达式，该表达式为标注的值。

4.返回值标注的定义方式是加上一个组合符号 ->，后面跟一个表达式，该标注位于形参列表和表示 def 语句结束的冒号之间
"""


from typing import List


def add(a: int, b: int) -> int:
    return a + b


def add_list(l: List[float]) -> float:
    return sum(l)


if __name__ == "__main__":

    print(add.__annotations__)  # 输出函数的标注

    print(add(1, 3))
    # print(add(1, 'a'))  # 会报错不支持的变量类型

    print(add_list([1.0, 2.0]))
    print(add_list([1, 2]))
    print(add_list([1, 2, 'a']))
