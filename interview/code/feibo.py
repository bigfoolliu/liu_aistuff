#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
动态规划的方式来计算斐波拉契数列

1, 1, 2, 3, 5, 8 ...

f(0)=f(1)=1
f(n)=f(n-1)+f(n-2), n>=2
"""


def feibo(n):
    if n <= 1:
        return 1
    return feibo(n-1) + feibo(n-2)


def feibo2(n):
    """使用生成器的方式"""
    a, b = 0, 1
    while n:
        a, b = b, a+b
        n -= 1
        yield a


print(feibo(0))
print(feibo(1))
print(feibo(2))
print(feibo(3))
print(feibo(4))
print(feibo(5))


for i in feibo2(5):
    print(i)
