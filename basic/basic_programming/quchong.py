#coding:utf-8


import random


def gener(n):
    """产生n个10000000以内的数并返回"""
    res = []
    for i in range(n):
        res.append(random.randint(1, 10000000))
    return res


def quchong(array):
    array = set(array)
    return array


res = gener(10000)
print(quchong(res))

