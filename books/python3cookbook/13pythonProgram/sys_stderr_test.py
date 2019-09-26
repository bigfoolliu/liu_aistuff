#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
向标准错误打印一条消息并返回某个非零状态码来终止程序运行
"""
import sys

# 有一个程序像下面这样终止，抛出一个 SystemExit 异常，使用错误消息作为参数
raise SystemExit("Failed")

# 到达不了这里，因为上面终止了程序
sys.stderr.write("Failed.\n")
raise SystemExit(1)
