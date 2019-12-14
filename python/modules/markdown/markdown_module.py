#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
markdown模块的使用
使用markdown来进行文件格式转换
"""


import markdown


def basic_demo():
    with open("./md_demo.md", "r") as md_file:
        html_content = markdown.markdown(md_file.read())

    with open("./md_demo_ret.html", "w") as html_file:
        html_file.write(html_content)


if __name__ == "__main__":
    basic_demo()
