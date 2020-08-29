#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
emoji模块的使用
"""

import emoji


def basic_demo():
    """显示表情"""
    s = "python is :thumbs_up:"
    print(emoji.emojize(s))  # 将字符串替换为表情

    s1 = "好的购物体验😀😀😀😀😀"
    print(emoji.demojize(s1))  # 去除其中的emoji表情


if __name__ == "__main__":
    basic_demo()
