#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu



"""
输入文件名作为参数1

创建一个同名的软链接到目录 当前目录下面
"""


import os
import sys


print(sys.argv)

origin_file_path = sys.argv[1]
file_name = origin_file_path.split('/')[-1]

print(origin_file_path, file_name)

# os.system(f'ln -s {origin_file_path} {file_name}')
