#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
argparse模块的简单使用

- 解析命令行的位置参数或者可选参数
- 详细用法官方文档：https://docs.python.org/zh-cn/3/library/argparse.html#argparse.ArgumentParser
"""


import argparse


def basic_demo():
    # 1.创建一个解析器对象, 运行 `python3 argparse_module.py -h` 返回的信息则是description的内容
    parser = argparse.ArgumentParser(description='接受一系列参数')

    # 2.添加位置参数,默认是必填的，否则会报错, 用法是不用带 -， 使用时候 `python3 argparse_module.py ha`
    parser.add_argument('e')

    # 3.可选参数，两种方式，长参数 --version 或者短参数-V， 两种方式可以同存，也可以只存在一个
    # help参数帮助，action='store_true'时候，--version 后面不需要跟具体参数
    parser.add_argument('-V', '--version', help='输出版本', action='store_true')

    # 4.指定输入参数的类型，默认为str, 且输入类型错误会报错，choices 限定可选的值有哪些, default设置默认值
    parser.add_argument('-x', help='输入整数', type=int, choices=[0, 1, 2], default=2)

    # 5.增加互斥参数，即参数不能同时出现
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-a', action='store_true')
    group.add_argument('-b', action='store_true')

    # 6.添加返回对象的属性值,Namespace(mode=False)
    parser.add_argument('--mode', help='输入模式', dest='mode', action='store_true')

    # 解析参数
    args = parser.parse_args()

    print(args, type(args))
    print(f'e: {args.e}')
    if args.version:
        print('version: 0.0.1')
    print(f'x + x: {args.x + args.x}')

    if args.a or args.b:
        group_arg = args.a if args.a else args.b
        print(f'group arg: {group_arg}')
    else:
        print('group_arg: None')

    # 将对象的属性和属性值的字典
    print(f'dict: {vars(args)}')


if __name__ == "__main__":
    basic_demo()
