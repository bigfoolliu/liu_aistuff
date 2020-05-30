#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
markdown模块的使用
使用markdown来进行文件格式转换
"""

import markdown


def basic_demo():
    """基本实例"""
    with open("md_demo.md", "r") as md_file:
        html_content = markdown.markdown(md_file.read(),
                                         extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite'])

    with open("ret.html", "w") as html_file:
        html_file.write(html_content)


def extensions_demo():
    """扩展实例"""
    pass


if __name__ == "__main__":
    basic_demo()
    # extensions_demo()
