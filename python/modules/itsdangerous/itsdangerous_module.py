#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
https://pythonhosted.org/itsdangerous/

itsdangerous用来像不可信的环境创建签名，将加密数据发送至不可信的环境
"""

import time
# from itsdangerous import  TimestampSigner
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


def basic_demo():
    # s = TimestampSigner("secret-key")
    # string = s.sign("hello")
    # s.unsign(string, max_age=10)

    serializer = Serializer("secret-key", 5)  # 设置密钥和加密时间
    msg = {"pwd": 123456}
    cry_msg = serializer.dumps(msg)

    print(msg, cry_msg)

    # 超时数据无法解密
    time.sleep(11)

    # 解密数据
    ori_msg = serializer.loads(cry_msg)


if __name__ == "__main__":
    basic_demo()
