#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
通过重定向/管道/文件接收输入

eg:
$ ls | ./filein.py          # Prints a directory listing to stdout.
$ ./filein.py /etc/passwd   # Reads /etc/passwd to stdout.
$ ./filein.py < /etc/passwd # Reads /etc/passwd to stdout.
"""
import fileinput


with fileinput.input() as f_input:
    for line in f_input:
        print(line, end="")