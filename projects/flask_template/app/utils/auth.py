#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
jwt验证

jwt验证流程：
1. 用户发送请求到服务端
2. 服务端验证用户信息
3. 服务端通过验证发送和用户数据访问token和刷新token
4. 客户端存储token,并在每次请求时附上这个token
5. 服务端验证token,并返回数据
6. 服务端验证token失败，客户端使用刷新token刷新数据访问token,并重新请求数据


jwt构成：
1. header(头部)
    声明类型和加密算法
    {
        "type": "JWT",
        "alg": "HS256"
    }

2. payload(载荷)
    存放具体的信息，下面的参数建议都写，但是不强制使用，也可以自定义载荷，不可以存入敏感信息

    iss: jwt签发者
    sub: jwt所面向的用户
    aud: 接收jwt的一方
    exp: jwt的过期时间，这个过期时间必须要大于签发时间
    nbf: 定义在什么时间之前，该jwt都是不可用的.
    iat: jwt的签发时间
    jti: jwt的唯一身份标识，主要用来作为一次性token,从而回避重放攻击。

3. signature(签名)
    三部分：
     1. 转base64的header
     2. 转base64的payload
     3. secret(私钥)
    
生成的token示例:
0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTc3MjI1NTgsImlzcyI6InFpbiIsInVzZXJfbmFtZSI6InpoYW5nIn0.YHNkSdAMEUIY__U5f9e1tQFAdqiHv_ai_gfaPpPnWLc


简单现实了flask和jwt的结合，实际中使用也会有一定的问题:
1. 载荷可以直接用base64解密。
2. 如果截获了token，可以利用暴力破解等方式，直接破解加密，提升用户权限。
3. 一旦拿到刷新token，就可以无限次获取授权，直到刷新token过期。

一些解决思路：
- 载荷不存入敏感信息
- 用户进行某项关键操作，再次验证用户。
- 限制请求次数
- 服务端管理token有效性
"""


from datetime import datetime, timedelta
from functools import wraps

import jwt
from flask import request, session

key = "qweqweqwe@#$"


def generate_access_token(user_name="", algorithm="HS256", exp=2.0):
    """
    产生进入token
    :param user_name: str
    :param algorithm：str,使用的加密算法
    :param exp: float, 过期时间
    :return: bytes, token
    """
    now = datetime.now()
    exp_datetime = now + timedelta(hours=exp)
    access_payload = {
        "exp": exp_datetime,  # 过期时间
        "flag": 0,  # 标识是否为一次性的token，0是，1否
        "iat": now,  # 开始时间
        "iss": "tony",  # 签名
        "user_name": user_name  # 自定义部分
    }
    access_token = jwt.encode(access_payload, key, algorithm=algorithm)
    return access_token


def generate_refresh_token(user_name="", algorithm="HS256", fresh=30):
    """
    生成刷新token
    :param user_name: str
    :param algorithm: str
    :param fresh: float,过期时间
    :return: bytes, refresh_token
    """
    now = datetime.utcnow()
    exp_datetime = now + timedelta(days=fresh)
    refresh_payload = {
        "exp": exp_datetime,
        "flag": 1,
        "iat": now,
        "iss": "tony",
        "user_name": user_name
    }
    refresh_token = jwt.encode(refresh_payload, key, algorithm=algorithm)
    return refresh_token


def decode_auth_token(token):
    """
    解密token
    :token: str,待解密的token
    """
    try:
        # 取消过期时间验证
        # payload = jwt.decode(token, key=key, options={"verify_exp": False})
        payload = jwt.decode(token, key=key,)
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, jwt.ImmatureSignatureError):
        return ""
    else:
        return payload


def identify(auth_header):
    """
    用户鉴权
    :param auth_header: str
    """
    if auth_header:
        payload = decode_auth_token(auth_header)
        if not payload:
            return False
        if "user_name" in payload and "flag" in payload:
            # 用来获取新access_token的refresh_token无法获取数据
            if payload["flag"] == 1:
                return False
            elif payload["flag"] == 0:
                return payload["user_name"]
            else:
                return False
        else:
            return False
    else:
        return False


def login_required(f):
    """
    登录保护，验证用户是否登录
    :param f: function
    :return:
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization",default=None)
        if not token:
            return "please log in"
        user_name = identify(token)
        if not user_name:
            return "please log in"
        session["user_name"] = user_name
        return f(*args, **kwargs)
    return wrapper
