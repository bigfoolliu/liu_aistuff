#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
响应体的封装
"""


from flask import current_app, request
from utils.code import ResponseCode, ResponseMessage


class ResMsg(object):
    """
    封装响应文本
    """

    def __init__(self, data=None, code=ResponseCode.SUCCESS, rq=request):
        """获取请求中的语言选择，如果不存在，获取配置中的语言，如果配置中的语言不存在则默认返回中文"""
        self.lang = rq.headers.get("lang", current_app.config.get("LANG", "zh_CN"))
        self._data = data
        self._msg = current_app.config[self.lang].get(code, None)  # 根据状态码找到对应的信息
        self._code = code
    
    def update(self, code=None, data=None, msg=None):
        """更新默认响应内容"""
        if code is not None:
            self._code = code
            self._msg = current_app.config[self.lang].get(code, None)
        if data is not None:
            self._data = data
        if msg is not None:
            self._msg = msg
    
    def add_field(self, name=None, value=None):
        """在响应文本中加入新的字段,以扩展响应格式内容"""
        if all([name, value]):
            self.__dict__[name] = value
    
    @property
    def data(self):
        body = self.__dict__
        body["data"] = body.pop("_data")
        body["msg"] = body.pop("_msg")
        body["code"] = body.pop("_code")
        return body
