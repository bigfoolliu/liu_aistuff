#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
functools模块使用
"""

# 1.使用自带的缓存机制
# maxsize：最多可以缓存多少个此函数的调用结果，如果为None，则无限制，设置为 2 的幂时，性能最佳
# typed：若为 True，则不同参数类型的调用将分别缓存。
from functools import lru_cache


@lru_cache(maxsize=1024, typed=True)
def calculate(n):
    print(f'calculating...{n}')
    return n * n


def calculate_demo():
    calculate(1)
    calculate(2)
    calculate(1)  # 第二次调用的时候没有真正执行函数体，使用的缓存结果


if __name__ == "__main__":
    calculate_demo()
