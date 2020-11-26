#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python 字典操作

dict对象的存储结构采用的是散列表(hash表)，其在最优情况下查询复杂度为O(1)。
"""


import random


def inner_func_demo():
    """
    字典内置函数示例
    """
    a = dict(name="tony", age=10)
    b = dict(name="tom", age=11)

    # 统计字典元素个数
    print(len(a))

    # 创建一个新字典，指定默认键值和value
    print(a.fromkeys(["score", "height"], 80))

    # 返回指定键的值，不存在则返回default值
    print(a.get("name"))
    print(a.get("score", None))

    # 返回字典的所有键和值以及键值对
    print(a.keys(), list(a.keys()))  # 默认返回类型为dict_keys
    print(a.values(), list(a.values()))  # 默认返回类型为dict_values
    print(a.items(), list(a.items()))  # 默认返回类型为dict_items

    # 更新键值对
    print(a.update({"name": "sam"}), a)

    # 键值不存在则设置默认值
    print(a.setdefault("class", 1), a)

    # 删除字典的所有键值对
    print(a.clear(), a)

    # 字典解析式以及过滤
    d = {k: random.randint(60, 100) for k in range(10)}
    print(d)
    d = {k: v for k, v in d.items() if v >= 90}
    print(d)


if __name__ == "__main__":
    inner_func_demo()
