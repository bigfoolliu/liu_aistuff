#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
pyjwt模块的使用
用来编解码json web token
"""


import jwt


key = '123456'  # 密钥


def create_jwt():
    """
    编码示例, 需要声明待编码的信息，使用的密钥，使用的加密算法
    """
    global key
    payload = {
        'iss': 'tony',  # 预定义的声明
        'sub': 'program',
        'aud': 'dev',
        'jti': '0001',
        'exp': 1609392766,
        'nbf': 1609292766,
        'iat': 1609292766,

        'msg': 'hello',  # 公共声明

        'admin': True  # 私有声明
    }
    headers = {
        'alg': 'HS256',
        'typ': 'JWT'
    }
    encoded_jwt = jwt.encode(payload, key, algorithm=headers['alg'])
    return encoded_jwt


def decode_jwt(encoded_jwt):
    """
    解码jwt
    """
    global key
    # 注意当载荷里面申明了 aud 受众的时候，解码时需要说明
    decoded_jwt = jwt.decode(encoded_jwt, key, audience='dev', algorithms=["HS256"])
    return decoded_jwt


def decode_demo():
    """
    解码示例
    """
    global key
    encoded_jwt = create_jwt()
    print(encoded_jwt, type(encoded_jwt), '\n')

    decoded_jwt = decode_jwt(encoded_jwt)
    print(decoded_jwt, type(decoded_jwt))


if __name__ == "__main__":
    decode_demo()
