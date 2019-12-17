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


def copy_int_demo():
    """
    当拷贝的对象是数字时候
    """
    a = 1
    b = a
    c = copy.copy(a)
    d = copy.deepcopy(a)

    print(a, b, c, d)
    print(id(a), id(b), id(c), id(d))

    # a重新赋值，则新开辟一块空间来存储2，a的地址改变
    a = 2

    print(a, b, c, d)
    print(id(a), id(b), id(c), id(d))


def copy_str_demo():
    """
    当拷贝的对象是字符串时候
    """
    a = "a"
    b = a
    c = copy.copy(a)
    d = copy.deepcopy(a)

    print(a, b, c, d)
    print(id(a), id(b), id(c), id(d))

    # a重新赋值，则开辟一块新的空间来存储"b",a的地址改变
    a = "b"

    print(a, b, c, d)
    print(id(a), id(b), id(c), id(d))


def copy_list_demo():
    """
    当拷贝的对象是列表的时候
    """
    a = [1, "a", [2, "b"]]

    # 始终和a一致且内存地址一样
    b = a

    # 拷贝第一层，新开辟内存地址，1，"a"不会跟随改变，[2, "b"]只是存储其地址，会跟随改变
    c = copy.copy(a)

    # 考本所有层，新开辟内存地址，所有元素的所有层都不会跟随变化
    d = copy.deepcopy(a)

    print(a, b, c, d)
    print(id(a), id(b), id(c), id(d))

    a[0] = 2

    print(a, b, c, d)
    print(id(a), id(b), id(c), id(d))

    a[2][0] = 3

    print(a, b, c, d)
    print(id(a), id(b), id(c), id(d))


if __name__ == "__main__":
    # copy_int_demo()
    copy_str_demo()
    # copy_list_demo()
