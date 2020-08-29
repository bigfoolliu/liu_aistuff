#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
termios模块

- 低级终端控制接口
- POSIX 风格的 tty 控制
- 所有的函数均接受文件描述符作为参数

https://docs.python.org/zh-cn/3/library/termios.html#module-termios
"""


import termios
import sys


def tcgetattr_demo():
    # 获得tty属性的列表
    # [27394, 3, 19200, 536872399, 38400, 38400, [b'\x04', b'\xff', b'\xff', b'\x7f', b'\x17', b'\x15', b'\x12',
    # b'\x00', b'\x03', b'\x1c', b'\x1a', b'\x19', b'\x11', b'\x13', b'\x16', b'\x0f', b'\x01', b'\x00', b'\x14',
    # b'\x00']]
    attribute_list = termios.tcgetattr(sys.stdin.fileno())
    print(attribute_list)


def tcsetattr_demo():
    # termios.tcsetattr(fd, when, attributes)
    # 根据tty属性列表设置文件描述符在特定时间改变属性

    # TCSANOW, 表示立即改变
    # TCSADRAIN, 表示在传输所有队列输出后再改变，或
    # TCSAFLUSH, 表示在传输所有队列输出并丢失所有队列输入后再改变

    fd = sys.stdin.fileno()
    attribute_list = termios.tcgetattr(fd)
    print(f"old: {attribute_list}")

    attribute_list[3] = attribute_list[3] & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSADRAIN, attribute_list)
    attribute_list = termios.tcgetattr(fd)
    print(f"new: {attribute_list}")


def get_pass(prompt="Password:"):
    """
    提示输入密码并关闭回显
    旧的 tty 属性无论在何种情况下都会被原样保存
    注意：需要在终端下执行
    """
    fd = sys.stdin.fileno()  # 获得输入文件描述符
    old = termios.tcgetattr(fd)  # 获取tty属性列表
    new = termios.tcgetattr(fd)  # 获取tty属性列表并将部分属性改变
    new[3] = new[3] & ~termios.ECHO
    try:
        termios.tcsetattr(fd, termios.TCSADRAIN, new)
        passwd = input(prompt)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return passwd


if __name__ == '__main__':
    # get_pass()
    # tcgetattr_demo()
    tcsetattr_demo()
