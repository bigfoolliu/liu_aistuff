#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
rich 模块使用

可以在终端展示不同的颜色等 https://github.com/willmcgugan/rich

展示rich模块的使用
python -m rich
"""


from rich import print
from rich.console import Console
from rich.progress import track
import time


def basic_demo():
    print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())



def time_line_demo():
	def do_step(step):
        time.sleep(0.1)

    for step in track(range(100)):
        do_step(step)


def console_demo():
    console = Console()
    console.print('hello, world', style='red bold')


if __name__ == '__main__':
    console_demo()

