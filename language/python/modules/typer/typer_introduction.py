#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
typer模块

- 命令行库， 加速命令行程序的开发
- https://github.com/tiangolo/typer


使用:

python xxx.py --help
python xxx.py echo "a" --lower
python xxx.py eval xxx 
"""


import sys
import typer
 

app = typer.Typer()

# 定义命令 echo，及处理函数
# text 无默认值，视为位置参数，类型为字符串
# lower/upper 类型为 bool，默认值为 False，视为选项 --lower/--upper，
# 且指定了为 True，不指定 False
@app.command(name='echo')
def echo_text(text: str, lower: bool = False, upper: bool = False):
    """Echo input text in multiple forms"""
    if lower:
        print(text.lower())
    elif upper:
        print(text.upper())
    else:
        print(text)
 
 
# 定义命令 eval，及处理函数
# expression 无默认值，视为位置参数，类型为字符串
@app.command(name='eval')
def eval_expression(expression: str):
    """Eval input expression and return result"""
    print(eval(expression))
 

if __name__ == "__main__":
    app()
