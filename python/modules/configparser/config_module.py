#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
configparser模块使用

读取配置cfg配置文件
"""


import configparser


def basic_demo():
    cfg = configparser.ConfigParser()  # 定义一个配置解析类的对象
    print(cfg.read("./setting.cfg", encoding="utf-8"))  # 读取配置文件

    print(cfg["french"]["greeting"])

    print(cfg["files"])
    print(cfg["files"]["bin"])


if __name__ == "__main__":
    basic_demo()
