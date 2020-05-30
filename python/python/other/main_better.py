#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
写更好的main函数

https://blog.csdn.net/qq_36185242/article/details/83576003

python3 main_better.py -a 1 -c --help --i 3 abc
"""

import sys
import getopt


class Usage(Exception):
    """自定义一个异常"""

    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            # h:a:b:c定义短选项，列表中定义长选项
            opts, args = getopt.getopt(argv[1:], "h:a:b:c", ["help", "ip", "port"])
            print("opts:", opts)
            print("args:", args)
            for name, value in opts:
                if name == "--help":
                    print("this is a for write a better main function.")
        except getopt.error as msg:
            raise Usage(msg)
    except Usage as err:
        print(err.msg)
        print("for help, use --help")
        return 2


if __name__ == "__main__":
    sys.exit(main())
