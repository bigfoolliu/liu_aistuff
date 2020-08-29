#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
string模块的简单实例
"""


import string


def basic_demo():
    """简单展示"""
    print(string.digits)  # 展示阿拉伯数字
    print(string.ascii_letters)  # 展示大小写字母
    print(string.ascii_lowercase)  # 展示小写字母
    print(string.ascii_uppercase)  # 展示大写字母
    print(string.punctuation)  # 展示所有标点
    print(string.printable)  # 展示所有标点


if __name__ == "__main__":
    basic_demo()
