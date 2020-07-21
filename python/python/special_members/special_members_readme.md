# special_members

<!-- vim-markdown-toc Marked -->

- [special_members](#special_members)
  - [1.__dict__](#1dict)
  - [2.__str__](#2str)
  - [3.__doc__](#3doc)
  - [4.__all__](#4all)
  - [5.__name__](#5name)
  - [6.__path__](#6path)

<!-- vim-markdown-toc -->

介绍python内部的一些特殊成员(变量，方法).

## 1.__dict__

## 2.__str__

## 3.__doc__

## 4.__all__

## 5.__name__

- 全局变量，表明当前的模块名称
- python文件名就是模块名后跟文件后缀 .py
- `python a.py`执行的时候，`__name__原本值为a，现在被赋值为__main__`

## 6.__path__

- `包`特有的属性
- 初始化为一个列表，其中包含在执行该文件中的代码之前保存包的文件 __init__.py 的目录的名称
