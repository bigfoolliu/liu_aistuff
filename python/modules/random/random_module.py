#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
random模块的简单应用
"""

import random


def random_demo():
    """随机生成0-1之间的浮点数"""
    a = random.random()  # 0<=a<1.0
    print(a, type(a))


def uniform_demo():
    """生成指定范围内的随机浮点数"""
    a = random.uniform(1.0, 5.0)  # 1.0<=a<=5.0
    print(a, type(a))


def randint_demo():
    """生成指定范围内的整数"""
    a = random.randint(0, 10)  # 0<=a<=10
    print(a, type(a))


def randrange_demo():
    """从指定范围按照基数递增的集合中获取一个随机数"""
    a = random.randrange(0, 10, 2)  # 从[0, 2, 4, 6, 8]中选择一个数
    print(a, type(a))


def choice_demo():
    """从一个序列中获取一个随机元素"""
    a = random.choice([0, 1, "a"])
    print(a, type(a))


def shuffle_demo():
    """将列表中的元素打乱"""
    a = [0, 2, 4, "a"]
    print(a)
    random.shuffle(a)
    print(a)


def sample_demo():
    """从指定序列中获取指定长度的片段并随机排列"""
    a = [1, 2, 3, "a", "b"]
    ret = random.sample(a, 3)  # 从a中挑选三个元素并随机排列
    print(a, ret)


if __name__ == "__main__":
    # random_demo()
    # uniform_demo()
    # randint_demo()
    # randrange_demo()
    # choice_demo()
    # shuffle_demo()
    sample_demo()
