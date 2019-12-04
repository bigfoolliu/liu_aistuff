#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
相关api接口的测试
"""


import logging
from datetime import datetime
from decimal import Decimal

from flask import Blueprint, jsonify, request, session

from app.models.model import Article, ChangeLogs, User
from app.utils.code import ResponseCode
from app.utils.core import db
from app.utils.response import ResMsg
from app.utils.util import CaptchaTool, Redis, route

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


# ------------------------创建数据库表测试-------------------------


@route(test_bp, "/createUser", methods=["POST"])
def test_create_user():
    """创建单个用户"""
    db.create_all()
    new_user = User(name="liu", age=20)
    db.session.add(new_user)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return "error: {}".format(e)
    return "create user ok"


@route(test_bp, "/createArticle", methods=["POST"])
def test_create_article():
    """创建单篇文章"""
    db.create_all()
    new_article = Article(title="title1", body="this is article1", last_change_time=datetime.now())
    db.session.add(new_article)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return "error: {}".format(e)
    return "create article ok"


@route(test_bp, "/createChangeLog", methods=["POST"])
def test_create_change_log():
    """创建单篇修改日志"""
    db.create_all()
    new_change_log = ChangeLogs(author_id=1, article_id=2, modify_context="hahaha", create_time=datetime.now())
    db.session.add(new_change_log)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return "error: {}".format(e)
    return "create change log ok"


@route(test_bp, "/getUsers", methods=["GET"])
def test_get_users():
    """查询所有用户"""
    # 或者users = db.session.query(User).all()
    users = User.query.all()
    ret = ResMsg()
    data = []
    for user in users:
        data.append({"id": user.id, "name": user.name, "age": user.age})
    ret.update(code=ResponseCode.SUCCESS, data=data)
    return ret.data


@route(test_bp, "/getUser", methods=["GET"])
def test_get_user():
    """查询单个用户"""
    user_id = request.args.get("id")
    # 或者user = db.session.query(User).filter(User.id == user_id).first()
    user = User.query.filter(User.id == user_id).first()
    ret = ResMsg()
    data = []
    data.append({"id": user.id, "name": user.name, "age": user.age})
    ret.update(code=ResponseCode.SUCCESS, data=data)
    return ret.data


# TODO：更多关于数据库的操作


@route(test_bp, "/redisWrite", methods=["GET"])
def test_redis_write():
    Redis.write("test_key", "test_value", 60)
    return "write ok"


@route(test_bp, "/redisRead", methods=["GET"])
def test_redis_read():
    value = Redis.read("test_key")
    return value


# ------------------------验证码生成和验证测试-------------------------


@route(test_bp, "/getCaptcha", methods=["GET"])
def test_get_captcha():
    """
    测试获取图形验证码
    将返回的字符串去除首尾引号直接粘贴至浏览器搜索栏即可看到图片
    """
    cap_tool = CaptchaTool()
    img_str, code = cap_tool.get_verify_code()
    session["code"] = code
    print("session_code:", session.get("code"))
    return img_str


@route(test_bp, "/verifyCaptcha", methods=["POST"])
def test_verify_captcha():
    """测试验证图形验证码"""
    obj = request.get_json(force=True)
    code = obj.get("code", None)
    s_code = session.get("code", None)
    print("code:", code, type(code), "s_code:", s_code, type(s_code))
    if not all([code, s_code]):
        return "parameter wrong"
    if code != s_code:
        return "captcha wrong"
    return "success"
