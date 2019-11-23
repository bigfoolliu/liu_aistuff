#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
相关api接口的测试
"""


import logging
from datetime import datetime
from decimal import Decimal

from app.utils.code import ResponseCode
from app.utils.response import ResMsg
from app.utils.util import route
from flask import Blueprint, jsonify

test_bp = Blueprint("test", __name__, url_prefix="/test")
logger = logging.getLogger(__name__)


# ---------------------------原生蓝图路由-------------------------


@test_bp.route("/logs", methods=["GET"])
def test_logger():
    """
    测试自定义的logger
    :return:
    """
    logger.info("this is info")
    logger.debug("this is debug")
    logger.warning("this is warning")
    logger.error("this is error")
    logger.critical("this is critical")
    return "ok"


@test_bp.route("/unifiedResponse", methods=["GET"])
def test_unified_response():
    """
    测试统一返回消息
    :return:
    """
    res = ResMsg()
    test_dict = dict(name="zhang", age=18)
    res.update(code=ResponseCode.SUCCESS, data=test_dict)
    return jsonify(res.data)


# -----------------------自定义封装蓝图测试----------------------------


@route(test_bp, "/packagedResponse", methods=["GET"])
def test_packed_response():
    """
    测试响应封装
    :return:
    """
    res = ResMsg()
    test_dict = dict(name="zhang", age=18)
    # 此处只需要填入响应状态码,即可获取到对应的响应消息
    res.update(code=ResponseCode.SUCCESS, data=test_dict)
    # 此处不再需要用jsonify，如果需要定制返回头或者http响应如下所示
    # return res.data,200,{"token":"111"}
    return res.data


@route(test_bp, "/typeResponse", methods=["GET"])
def test_type_response():
    """
    测试使用自定义的Flask的json解析类
    :return:
    """
    res = ResMsg()
    now = datetime.now()
    date = datetime.now().date()
    num = Decimal(11.111111)
    test_dict = dict(now=now, date=date, num=num)
    res.update(code=ResponseCode.SUCCESS, data=test_dict)
    return res.data
