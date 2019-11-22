#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
规范化接口响应码

{
	"code":0,
	"msg":"成功",
	"data":null
}
"""


class ResponseCode(object):
    SUCCESS = 0  # 成功
    FAIL = -1  # 失败
    NO_RESOURCE_FOUND = 40001  # 未找到资源
    INVALID_PARAMETER = 40002  # 参数无效
    ACCOUNT_OR_PASS_WORD_ERR = 40003  # 账户或者密码错误


class ResponseMessage(object):
    SUCCESS = "成功"
    FAIL = "失败"
    NO_RESOURCE_FOUND = "未找到资源"
    INVALID_PARAMETER = "参数无效"
    ACCOUNT_OR_PASS_WORD_ERR = "账户或者密码错误"
