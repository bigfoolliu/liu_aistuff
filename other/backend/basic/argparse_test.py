#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
argparse模块的简单使用
"""
import argparse

parser = argparse.ArgumentParser(description="receive arguments")

# 构建一个组来管理参数
group = parser.add_mutually_exclusive_group()
group.add_argument("--mqtt-subscribe")
group.add_argument("--mqtt-publish")

args = parser.parse_args()

print(args, type(args))
