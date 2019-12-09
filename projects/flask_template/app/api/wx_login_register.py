#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
使用微信注册或者登录
使用微信登录文档：https://developers.weixin.qq.com/doc/oplatform/Website_App/WeChat_Login/Wechat_Login.html


实现流程：
1. 前端页面拉取微信授权二维码
2. 用户扫码确认授权。
3. 前端将授权码发送到后端。
4. 后端将授权码发送到微信平台验证，获取用户信息及授权信息。
5. 比较本平台用户信息，实现用户登陆和注册。


前提：
1. 在微信开发平台(https://open.weixin.qq.com/)申请了账户并成为开发者
2. 成为开发者之后获得"appid"和"secret"

😃
"""


import json
from urllib import parse, request

from app.models.model import User, UserLoginMethod
from app.utils.core import db


def get_access_code(code, flag):
    """
    获取微信授权码
    :param code: str,前端或者app拉取的临时授权码
    :param flag: str,web端或者app端的标识
    :return: None或者微信授权数据dict

    拉取微信授权成功返回:
    {
        "access_token": "ACCESS_TOKEN",
        "expires_in": 7200,
        "refresh_token": "REFRESH_TOKEN",
        "openid": "OPENID",
        "scope": "SCOPE"
    }

    拉取微信授权失败:
    {
        "errcode":40029,
        "errmsg":"invalid code"
    }
    """
    # 根据平台的不同，使用不同的密钥
    if flag == "web":
        appid = "web_appid"  # 填申请的密钥
        secret = "web_secret"
    elif flag == "app":
        appid = "app_appid"
        secret = "app_secret"
    else:
        return None
    
    # 将查询条件转换为具体的url
    try:
        fields = parse.urlencode({
            "appid": appid,
            "secret": secret,
            "code": code,
            "grant_type": "authorization_code"
        })
        url = "https://api.weixin.qq.com/sns/oauth2/access_token?{}".format(fields)
        print("wx access_token url:", url)

        req = request.Request(url=url, method="GET")
        res = request.urlopen(req, timeout=10)

        access_data = json.loads(res.read().decode())
        print("wx access_data:", access_data)
    
    except Exception as e:
        print(e)
        return None

    # openid在返回数据里来验证返回结果的正确性
    if "openid" in access_data:
        return access_data
    else:
        return None


def get_wx_user_info(access_data):
    """
    获取微信用户的信息
    :param access_data: dict
    :return: None或者微信用户数据dict

    获取成功:
    {
        "openid": "OPENID",
        "nickname": "NICKNAME",
        "sex": 1,
        "province": "PROVINCE",
        "city": "CITY",
        "country": "COUNTRY",
        "headimgurl": "test.png",
        "privilege":[
            "PRIVILEGE1",
            "PRIVILEGE2"
            ],
        "unionid": " o6_bmasdasdsad6_2sgVt7hMZOPfL"
    }

    获取失败：
    {
        "errcode": 40003,
        "errmsg": "invalid openid"
    }
    """
    openid = access_data.get("openid")
    access_token = access_data.get("access_token")
    try:
        fields = parse.urlencode({
            "access_token": access_token,
            "openid": openid
        })
        url = "https://api.weixin.qq.com/sns/userinfo?{}".format(fields)
        req = request.Request(url=url, method="GET")
        print("wx userinfo url:", url)

        res = request.urlopen(req, timeout=10)
        wx_user_info = json.loads(res.read().decode())
        print("wx user info:", wx_user_info)
    except Exception as e:
        print(e)
        return None
    
    # openid在返回数据里来验证返回结果的正确性
    if "openid" in wx_user_info:
        return wx_user_info
    else:
        return None


def login_or_register(wx_user_info):
    """
    验证该用户是否为该平台的用户，未注册则注册后登陆，否则直接登陆
    :param wx_user_info: dict，微信用户信息
    :return:
    """
    unionid = wx_user_info.get("unionid")  # 微信唯一id
    nickname = wx_user_info.get("nickname")  # 微信用户昵称

    if not unionid:
        return None

    # 判断用户是否在本系统中
    user_login = db.session.query(UserLoginMethod).\
        filter(UserLoginMethod.login_method == "WX",
                UserLoginMethod.identification == unionid, ).first()
    
    # 用户存在于本系统则直接返回,否则新建用户
    if user_login:
        user = db.session.query(User.id, User.name).filter(
            User.id == user_login.user_id).first()
        data = dict(zip(user.keys(), user))
        return data
    else:
        try:
            new_user = User(name=nickname, age=20)
            db.session.add(new_user)
            db.session.flush()

            new_user_login = UserLoginMethod(
                user_id=new_user.id,
                login_method="WX",
                identification=unionid,
                access_code=""
            )
            db.session.add(new_user_login)
            db.session.flush()

            db.session.commit()
        except Exception as e:
            print(e)
            return None
    
    data = dict(id=new_user.id, name=User.name)
    return data
