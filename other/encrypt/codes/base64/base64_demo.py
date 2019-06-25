#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import base64


meg = "jiangxing"


def base64_encrypt(meg):
    """
    meg: str
    return: bytes
    """
    b64_meg = base64.b64encode(meg.encode("utf-8"))
    return b64_meg


def base64_decrypt(meg_data):
    """
    meg_data: bytes
    return: str
    """
    meg = base64.b64decode(meg_data)
    return meg.decode("utf-8")


ret = base64_encrypt(meg)
print(ret, len(ret))

ret = base64_decrypt(ret)
print(ret, len(ret))