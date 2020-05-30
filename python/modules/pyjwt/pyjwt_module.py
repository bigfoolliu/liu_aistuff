#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
pyjwt模块的使用

用来编解码json web token

基本介绍：https://pyjwt.readthedocs.io/en/latest/
更多使用：https://pyjwt.readthedocs.io/en/latest/usage.html
"""

import jwt


def encode_demo():
    """编码示例"""
    # 需要声明待编码的信息，使用的密钥，使用的加密算法
    encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
    print(encoded_jwt, type(encoded_jwt))
    return encoded_jwt


def decode_demo():
    """解码示例"""
    encoded_jwt = encode_demo()
    decoded_jwt = jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
    print(decoded_jwt, type(decoded_jwt))


if __name__ == "__main__":
    # encode_demo()
    decode_demo()
