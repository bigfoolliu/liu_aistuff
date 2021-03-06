#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
相关api接口的测试
"""


import logging
import random
from datetime import datetime, timedelta
from decimal import Decimal

from flask import Blueprint, jsonify, request, session

from app.api.phone_login_register import SendSMS, phone_login_or_register
from app.api.wx_login_register import (get_access_code, get_wx_user_info,
                                       login_or_register)
from app.models.model import Article, ChangeLogs, User, UserLoginMethod
from app.utils.auth import (decode_auth_token, generate_access_token,
                            generate_refresh_token, login_required)
from app.utils.code import ResponseCode
from app.utils.core import db
from app.utils.response import ResMsg
from app.utils.util import CaptchaTool, PhoneTool, Redis, route

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


# -----------------------redis读写测试-------------------------


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


# ------------------------鉴权测试-------------------------


@test_bp.route("/testLogin", methods=["POST"])
def test_login():
    """
    测试登录成功获取到数据获取token和刷新token
    """
    obj = request.get_json(force=True)
    name = obj.get("name")
    if not obj or not name:
        return "parameter wrong"
    if name == "tony":
        access_token = generate_access_token(user_name=name)
        refresh_token = generate_refresh_token(user_name=name)
        data = {"access_token": access_token.decode("utf-8"),
                "refresh_token": refresh_token.decode("utf-8")}
        # print(data)
        return jsonify(data)
    else:
        return "user name or pwd wrong"


@test_bp.route("/testGetData", methods=["GET"])
@login_required
def test_get_data():
    """
    测试登录保护下获取数据
    需要首先请求/test/testLogin获取access_token，将其作为请求头Authorization的内容
    """
    name = session.get("user_name")
    return "hello, {}".format(name)


@test_bp.route("/testRefreshToken", methods=["GET"])
def test_refresh_token():
    """
    刷新token，将原有的token换成新的token
    需要首先请求/test/testLogin获取access_token，将其作为请求参数refresh_token的内容
    """
    refresh_token = request.args.get("refresh_token")
    if not refresh_token:
        return "parameter wrong"
    payload = decode_auth_token(refresh_token)
    if not payload:
        return "please log in"
    if "user_name" not in payload:
        return "please log in"
    access_token = generate_access_token(user_name=payload["user_name"])
    data = {"access_token": access_token.decode("utf-8"), "refresh_token": refresh_token}
    return jsonify(data)


# ------------------------微信测试-------------------------


@test_bp.route("/testCreateWXUser", methods=["POST"])
def test_create_WXUser():
    """
    测试创建一个微信用户
    :return:
    """
    data = request.get_json(force=True)
    unionid = data.get("unionid")
    nickname = data.get("nickname")

    if not all([unionid, nickname]):
        return "parameters wrong"
    
    db.create_all()
    new_wx_user_method = UserLoginMethod(
        user_id=111222,
        login_method="WX",
        identification="123456",
        access_code="wx_access_code"
    )
    try:
        db.session.add(new_wx_user_method)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
        return "create wx user failed"
    
    return "create wx user success"


@test_bp.route("/testWXLoginOrRegister", methods=["GET"])
def test_wx_login_or_register():
    """
    测试微信登陆测试
    :return:
    """
    code = request.args.get("code")  # 前端获取到的临时授权码
    flag = request.args.get("flag")  # 标识是web端还是app端登陆或者注册

    if not all([code, flag]):
        return "parameters failed"
    
    # TODO:需要申请一个微信开发者账号
    # access_code = get_access_code(code, flag)
    # if not access_code:
    #     return "get wx access_code failed"
    
    # wx_user_info = get_wx_user_info(access_data=access_code)
    # if not wx_user_info:
    #     return "get wx user info failed"

    wx_user_info = {
        "unionid": "wx_union_id",
        "nickname": "wx_nickname"
    }
    
    data = login_or_register(wx_user_info)
    if not data:
        return "login failed"
    
    return data


# ------------------------手机验证码测试-------------------------


@test_bp.route("/testGetPhoneVerifyCode", methods=["GET"])
def test_get_phone_verify_code():
    """
    测试获取手机号验证码
    :return:
    """
    now = datetime.now()
    category = request.args.get("category", None) or request.headers.get("category", None)
    phone = request.args.get("account", None)

    re_phone = PhoneTool.check_phone(phone)
    if not phone or not re_phone:
        return "phone number wrong"
    if not category:
        return "parameters wrong"

    print("phone:", phone, "\nre_phone:", re_phone, "\ncategory:", category)
    try:
        # 获取手机验证码的设置时间
        flag = Redis.hget(re_phone, "expire_time")
        if flag:
            flag = datetime.strptime(flag, "%Y-%m-%d %H:%M:%S")
            print("flag:", flag)
            if (flag-now).total_seconds() < 60:
                return "operate too frequent"
        # 生成随机的6位数字验证码
        code = "".join([str(random.randint(0, 9)) for _ in range(6)])
        print("sms code:", code)
        template_param = {"code": code}

        # TODO:发送短信,需要注册阿里云的短信服务
        # sms = SendSMS(phone=re_phone, category=category, template_param=template_param,)
        # sms.send_sms()

        # 将验证码存入redis,方便验证,同时设置之间防止短时间内重复操作,设置其过期时间为3分钟
        Redis.hset(re_phone, "code", code)
        Redis.hset(re_phone, "expire_time", (now+timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S"))
        Redis.expire(re_phone, 60*3)

        return "get or save sms code success"
    except Exception as e:
        print(e)
        return "get or save sms code failed"


@test_bp.route("/testPhoneLoginRegister", methods=["POST"])
def test_phone_login_or_register():
    """
    测试使用手机号注册或者登录
    :return:
    """
    data = request.get_json(force=True)
    phone = data.get("account")
    code = data.get("code")
    if not phone or not code:
        return "parameters wrong"

    # 从redis中取出对应的code
    flag = PhoneTool.check_phone_code(phone, code)
    if not flag:
        return "sms code wrong"

    # 根据信息注册或者登录
    data = phone_login_or_register(phone)
    if not data:
        return "phone register or login wrong"

    return data
