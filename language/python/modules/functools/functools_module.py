#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
functools模块使用

- 用于高阶函数，即作用于函数或者返回值为函数的函数
"""

# 1.使用自带的缓存机制
# maxsize：最多可以缓存多少个此函数的调用结果，如果为None，则无限制，设置为 2 的幂时，性能最佳
# typed：若为 True，则不同参数类型的调用将分别缓存。
from functools import lru_cache, partial


@lru_cache(maxsize=1024, typed=True)
def calculate(n):
    print(f'calculating...{n}')
    return n * n


def calculate_demo():
    calculate(1)
    calculate(2)
    calculate(1)  # 第二次调用的时候没有真正执行函数体，使用的缓存结果


# 2.借助偏函数和iter函数流式读取超大文件
# partial用法: http://www.xxf-home.net/archives/1004
def read_from_file(file_name, block_size=1024 * 8):
    """
    :param file_name: 文件名称
    :param block_size: 默认为8kb
    :return: generator object
    """
    with open(file_name, 'r') as fp:
        # partial将fp.read函数转换为为一个可被调用的对象,且参数固定
        for chunk in iter(partial(fp.read, block_size), ''):
            yield chunk


def read_demo():
    file_generator = read_from_file('../../python_introduction.md')
    for i in file_generator:
        print(i)


if __name__ == "__main__":
    # calculate_demo()
    read_demo()
