#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
decimal模块使用

- 提供十进制浮点运算支持

1.提供十进制数据类型，并且存储为十进制数序列；
2.有界精度：用于存储数字的位数是固定的，可以通过decimal.getcontext（）.prec=x 来设定，不同的数字可以有不同的精度
3.浮点：十进制小数点的位置不固定（但位数是固定的）
"""


import decimal


def basic_demo():
    """基本演示"""
    # python3环境中，这里最好传入一个字符串，如果传入了一个浮点型，decimal对象的浮点精度得不到保证
    c = decimal.Decimal("3.1415926")
    print(c)
    a = decimal.Decimal(2)
    print(a)
    b = decimal.Decimal(2.123)
    print(b)

    # 进行计算
    ret1 = 1/3
    ret2 = decimal.Decimal(1) / decimal.Decimal(3)
    ret3 = 2.1 + 3.3
    print("Decimal结果:", ret2, type(ret2))
    print("普通计算结果:", ret1, type(ret1))
    print("普通计算结果2:", ret3, type(ret3))


def context_demo():
    """设置精度示例"""
    # 设置当前环境的context,设置小数点精度为6
    context = decimal.getcontext()
    context.prec = 6
    print(context)


def quantize_demo():
    """设置小数位数示例"""
    d = decimal.Decimal("3.24234324")
    ret = d.quantize(decimal.Decimal("0.00"))
    print(ret)


if __name__ == "__main__":
    # basic_demo()
    # context_demo()
    quantize_demo()
