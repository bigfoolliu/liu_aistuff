#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
列表或者字典的嵌套解包
"""


def list_pickle_demo():
    l = [[1, 2, 3, 4], [2, 3, 4, 5], [2, 3, [22, 11]]]
    ret = []

    def list_pickle(l):
        """对多重列表的解包，输出所有的元素"""
        # global ret
        if isinstance(l, list):
            for item in l:
                if isinstance(item, list):
                    list_pickle(item)
                else:
                    ret.append(item)
        else:
            ret.append(item)

    list_pickle(l)
    print(ret)


def dict_pickle_demo():
    d = {"s1": {"name": "tony", "age": 12, "a": {"school": "mit"}}, "s2": {"name": "jim", "age": 20}}
    ret = []

    def dict_pickle(d):
        """对多重字典的解包，输出所有元素"""
        if isinstance(d, dict):
            for key, value in d.items():
                if isinstance(value, dict):
                    dict_pickle(value)
                else:
                    ret.append(value)
        else:
            ret.append(value)

    dict_pickle(d)
    print(ret)


if __name__ == "__main__":
    # list_pickle_demo()
    dict_pickle_demo()
