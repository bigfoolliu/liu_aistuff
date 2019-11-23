#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
解决json类型错误，重写flask的json encoder，定义转化规则
"""


import datetime
import decimal
import uuid

from flask.json import JSONEncoder as BaseJSONEncoder


class JSONEncoder(BaseJSONEncoder):
    """
    重写default方法，支持更多的转换方法
    """
    
    def default(self, o):
        """
        如果有其他类型的数据转换需求可以直接添加
        :param o:
        """
        if isinstance(o, datetime.datetime):
            # 格式化时间
            return o.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(o, datetime.date):
            # 格式化日期
            return o.strftime("%Y-%m-%d")
        if isinstance(o, decimal.Decimal):
            # 将高精度数字转换为字符串
            return str(o)
        if isinstance(o, uuid.UUID):
            # 格式化uuid
            return str(o)
        if isinstance(o, bytes):
            # 格式化字节数据
            return o.decode("utf-8")
        return super(JSONEncoder, self).default(o)
