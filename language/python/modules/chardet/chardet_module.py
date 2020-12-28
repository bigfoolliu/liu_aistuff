#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
chardet模块使用

自动识别编码
"""


import chardet


def detect_demo():
    """基本识别示例"""
    code = b"\xc8\xcb\xc9\xfa\xbf\xe0\xb6\xcc\xa3\xac\xce\xd2\xd3\xc3Python"
    ret = chardet.detect(code)  # 查看编码信息
    print(ret)

    # 使用解析出来的编码来decode
    decoded_ret = code.decode(ret["encoding"])
    print(decoded_ret)


if __name__ == "__main__":
    detect_demo()
