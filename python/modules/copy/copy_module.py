#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python深浅拷贝以及赋值的区别

赋值：
- 内存中指向同一个对象，数据完全共享
- 可变类型，如列表等，修改一个，另一个跟着改变
- 不可变类型，如数值，字符串等，修改一个，另一个不会跟着改变

浅拷贝：
- 数据半共享
- 复制其数据独立内存存放，但是只拷贝成功第一层


深拷贝：
- 内存不共享，数据不共享
- 拷贝出来的数据不会因为原数据的变化而变化
"""


import copy


def when_is_int():
    """当拷贝的对象是数字时候"""
    a = 1
    b = a
    c = copy.copy(a)
    d = copy.deepcopy(a)

    print("val:\na:{}\nb:{}\nc:{}\nd:{}".format(a, b, c, d))
    print("id:\na:{}\nb:{}\nc:{}\nd:{}".format(id(a), id(b), id(c), id(d)))

    a = 2

    print("val:\na:{}\nb:{}\nc:{}\nd:{}".format(a, b, c, d))
    print("id:\na:{}\nb:{}\nc:{}\nd:{}".format(id(a), id(b), id(c), id(d)))


def when_is_str():
    """当拷贝的对象是字符串时候"""
    a = "a"
    b = a
    c = copy.copy(a)
    d = copy.deepcopy(a)

    print("val:\na:{}\nb:{}\nc:{}\nd:{}".format(a, b, c, d))
    print("id:\na:{}\nb:{}\nc:{}\nd:{}".format(id(a), id(b), id(c), id(d)))

    a = "b"

    print("val:\na:{}\nb:{}\nc:{}\nd:{}".format(a, b, c, d))
    print("id:\na:{}\nb:{}\nc:{}\nd:{}".format(id(a), id(b), id(c), id(d)))


def when_is_list():
    """当拷贝的对象是列表的时候"""
    a = [1, "a", [2, "b"]]
    b = a
    c = copy.copy(a)
    d = copy.deepcopy(a)

    print("val:\na:{}\nb:{}\nc:{}\nd:{}".format(a, b, c, d))
    print("id:\na:{}\nb:{}\nc:{}\nd:{}".format(id(a), id(b), id(c), id(d)))

    a[0] = 2

    print("val:\na:{}\nb:{}\nc:{}\nd:{}".format(a, b, c, d))
    print("id:\na:{}\nb:{}\nc:{}\nd:{}".format(id(a), id(b), id(c), id(d)))

    a[2][0] = 3

    print("val:\na:{}\nb:{}\nc:{}\nd:{}".format(a, b, c, d))
    print("id:\na:{}\nb:{}\nc:{}\nd:{}".format(id(a), id(b), id(c), id(d)))


if __name__ == "__main__":
    print("a\nb:b=a\nc:c=copy.copy(a)\nd:d=copy.deepcopy(a)")
    print("--------------------int------------------")
    when_is_int()
    print("--------------------str------------------")
    when_is_str()
    print("------------------ list ------------------")
    when_is_list()
