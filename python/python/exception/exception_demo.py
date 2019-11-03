#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


"""
python内置的一些异常
官方：https://docs.python.org/zh-cn/3/library/exceptions.html#FileExistsError
菜鸟：https://www.runoob.com/python/python-exceptions.html
"""
import logging


# try:
#     with open("test.txt", "r") as f:
#         test_data = f.read()
# except OSError as e:
#     logging.info(e)
# except FileNotFoundError as e:
#     logging.error(e)
# except Exception as e:
#     logging.exception(e)


class MyException(BaseException):

    def run(self):
        pass


try:
    name = input("input name")
except EOFError as e:
    print(e)
finally:
    print("haha")
