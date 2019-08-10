#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
draw the pic of function f(x)=x!
"""
import matplotlib.pyplot as plt
import numpy as np


def out_put(x):
    """输出从1-x的各数的阶乘结果"""
    def func(n):
        if n <= 1:
            return 1
        else:
            ret = 1
            i = 1
            while i <= n:
                ret *= i
                i += 1
        return ret
    y = []
    for i in range(1, x+1):
        y.append(func(i))
    return y


def draw(n):
    if n < 0:
        raise ValueError
    else:
        x = np.linspace(1, n, num=n)
        y = np.array(out_put(n))
        plt.scatter(x, y)
        plt.show()


for i in range(6):
    draw(i)
