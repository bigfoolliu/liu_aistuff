#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
termios模块

- 低级终端控制接口
- POSIX 风格的 tty 控制
"""


import termios
import sys


def getchgen():
    fd = sys.stdin.fileno()
    oldattr = termios.tcgetattr(fd)
    # oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    newattr = termios.tcgetattr(fd)
    newattr[3] &= ~termios.ICANON
    newattr[3] &= ~termios.ECHO
    def getch():
        try:
            termios.tcsetattr(fd, termios.TCSANOW, newattr)
            c = sys.stdin.read(1)
            return c
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, oldattr)

    def reset():
        termios.tcsetattr(fd, termios.TCSADRAIN, oldattr)


    return getch, reset


getchgen()

