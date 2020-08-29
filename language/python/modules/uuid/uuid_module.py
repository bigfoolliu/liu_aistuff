#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
通过uuid库生成uuid

uuid:
通用唯一标识符
通过mac地址，时间戳，命名空间，随机数，伪随机数保证生成的id的唯一性
固定的大小：128位
"""


import uuid


def uuid1_demo():
    """基于时间戳以及mac地址,在Global分布式环境下使用较好"""
    id1 = uuid.uuid1()
    print(id1)


def uuid3_demo():
    """基于名字的MD5散列值,名字有唯一性要求使用较好"""
    id3 = uuid.uuid3(uuid.NAMESPACE_DNS, 'hello')
    print(id3)


def uuid4_demo():
    """基于随机数,概率性重复，最好不要使用"""
    id4 = uuid.uuid4()
    print(id4)


def uuid5_demo():
    """基于名字的SHA-1散列值,名字有唯一性要求使用较好"""
    id5 = uuid.uuid5(uuid.NAMESPACE_DNS, "hello")
    print(id5)


if __name__ == "__main__":
    uuid1_demo()
    uuid3_demo()
    uuid4_demo()
    uuid5_demo()
