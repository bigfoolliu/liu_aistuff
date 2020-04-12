#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python上下文管理器来改善异常的处理

官方上下文管理器： https://www.python.org/dev/peps/pep-0343/
"""


class RaiseApiError(object):

    """自定义上下文管理器，捕获指定的异常
    进入上下文时不做什么
    退出上下文的时候，会判断当前上下文是否抛出了类型为self.captures的异常,有的话就用APIErrorCode异常类代替
    """

    def __init__(self, captures, code):
        self.captures = captures
        self.code = code

    def __enter__(self):
        """进入上下文的调用"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文时调用
        exc_type: 异常类型
        exc_val: 异常值
        exvc_tb: 错误栈
        """
        if exc_type is None:
            return False
        if exc_type == self.captures:
            raise self.code from exc_val
        return False


def upload_image():
    # 调用自定义的上下文异常
    with RaiseApiError(KeyError, "image not provided"):
        image = request.FILES["image"]

