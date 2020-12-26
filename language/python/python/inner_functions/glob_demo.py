#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu



"""
glob

- python自带的一个操作文件的相关模块
- 用它可以查找符合特定规则的文件路径名
- 使用该模块查找文件，只需要用到： “*”, “?”, “[]”这三个匹配符;
- python的glob模块可以对文件夹下所有文件进行遍历，并保存为一个list列表


”*”匹配0个或多个字符；
”?”匹配单个字符；
”[]”匹配指定范围内的字符，如：[0-9]匹配数字。


glob.iglob：

- 获取一个可遍历对象，使用它可以逐个获取匹配的文件路径名
- iglob与glob类似，只是这里返回值为迭代器，对于大量文件时更为省内存

https://blog.csdn.net/gufenchen/article/details/90723418
https://www.cnblogs.com/luminousjj/p/9359543.html
"""


import glob


for file_name in glob.glob('./*.py'):
    print(file_name)

_iglob = glob.iglob('./*.py')
print(type(_iglob))
print(list(_iglob))
