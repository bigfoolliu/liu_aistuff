#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python内置函数示例

abs()
all()
any()

bin()
bool()
bytearray()

callable()
chr()
classmethod()
cmp()
compile()
complex()

delattr()
dict()
dir()
divmod()

enumerate()
eval()
execfile()

file()
filter()
float()
format()
frozenset()

getattr()
globals()

hasattr()
hash()
help()
hex()

id()
input()
int()
isinstance()
issubclass()
iter()

len()
list()
locals()
long()

map()
max()
memoryview()
min()

next()

object()
oct()
open()
ord()

pow()
print()
property()

range()
raw_input()
reduce()
reload()
repr()
reverse()
round()

set()
setattr()
slice()
sorted()
staticmethod()
str()
sum()
super()
sum()

tuple()
type()

unichr()
unicode()

vars()

xrange()

zip()

__import__()

exec
"""


def abs_demo():
    """
    abs返回数字的绝对值
    """
    print(abs(-23))
    print(abs(-0b1011))


def all_demo():
    """
    判定给定可迭代参数中所有元素是否都为True
    如果iterable的所有元素不为0、''、False或者iterable为空，all(iterable)返回True，否则返回False
    """
    print(all([]))
    print(all(["a", None]))
    print(all(["a", 0]))
    print(all(["a", 1]))
    print(all(["a", 1, ""]))

    print(all(("a", 0)))


def any_demo():
    """
    用于判断给定的可迭代参数 iterable,
    全部为 False，则返回 False; 如果有一个为 True，则返回 True。
    元素除了是 0、空、FALSE 外都算 TRUE
    """
    print(any(["a", 0]))
    print(any(["a", 1]))
    print(any([False, 0]))
    print(any([None, 0]))


def bin_demo():
    """
    返回一个整数 int 或者长整数 long int 的二进制表示
    """
    print(bin(12))


def chr_demo():
    """
    一个整数作为参数，返回对应的字符
    """
    for i in range(0, 128):
        print("{}:{}".format(i, chr(i)))


def ord_demo():
    """
    和chr函数是配对函数
    它以一个字符串（Unicode 字符）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值。
    """
    print(ord("A"))
    print(ord("a"))
    print(ord("?"))


if __name__ == "__main__":
    # abs_demo()
    # all_demo()
    # any_demo()

    # bin_demo()

    # chr_demo()

    ord_demo()
