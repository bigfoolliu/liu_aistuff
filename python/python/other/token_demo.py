#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import base64
import hashlib
import os
import time


def generate_token(expire_time):
    """
    :param aging: 时效
    """
    # 基本加密
    sha1_token = hashlib.sha1(os.urandom(24)).hexdigest()
    create_time = int(time.time())
    time_group = str(create_time) + ":" + str(expire_time)
    # 当前时间 + 时间间隔 生成base64编码 并且去掉 "="
    time_token = base64.urlsafe_b64encode(time_group).strip().lstrip().rstrip("=")
    token = sha1_token + time_token
    return token


def verify_token(token):
    result = {}
    decode_split_time = safe_b64decode(token[40:]).split(":")
    decode_create_time = decode_split_time[0]
    decode_aging_time = decode_split_time[1]
    difference_time = int(time.time()) - int(decode_create_time)  # 时间差
    # 判断 是否失效 如果失效state值为0，生成新的token
    if difference_time > int(decode_aging_time):
        result["is_expire"] = True
        result["token"] = generate_token(decode_aging_time)
    else:
        result["is_expire"] = False
        result["token"] = token
    return result


def safe_b64decode(s):
    length = len(s) % 4
    for i in range(length):
        s = s + "="
    return base64.b64decode(s)
