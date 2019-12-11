#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
使用手机发送短信验证码登陆注册

实现流程：
1. 用户在前端或APP输入手机号点击获取验证码
2. 后端获取到手机号并发送验证码
3. 用户接受到验证码，输入并登陆或注册
4. 后端完成登陆或注册操作，授权用户登陆系统


前置条件：
1. 购买手机短信服务(阿里云短信：https://help.aliyun.com/document_detail/112147.html?spm=a2c4g.11186623.2.18.68d050a4O4WF4K)
2. 在短信控制台申请短信模板，成功之后会有短信服务ID、短信服务密钥、短信签名、短信模板等内容。
"""


import uuid

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from app.models.model import User, UserLoginMethod
from app.utils.core import db


# 阿里云申请成功获取到的内容
smss = {
    "SMS_ACCESS_KEY_ID": "128548974",  # key ID
    "SMS_ACCESS_KEY_SECRET": "323232",  # 密钥
    "SMS_SIGN_NAME": "设置签名",  # 签名
    "AUTHENTICATION": "SMS_1551323",  # 身份验证模板编码
    "LOGIN_CONFIRMATION": "SMS_155546",  # 登陆确认模板编码
    "LOGIN_EXCEPTION": "SMS_1556546",  # 登陆异常模板编码
    "USER_REGISTRATION": "SMS_1551654625",  # 用户注册模板编码
    "CHANGE_PASSWORD": "SMS_155126456",  # 修改密码模板编码
    "INFORMATION_CHANGE": "SMS_1551265463",  # 信息修改模板编码
 }


class SendSMS(object):

    def __init__(self, phone, category, template_param):
        """
        :param phone: str,发送的手机号
        :param category: str,选择短信模板
        :param template_param: dict,短信验证码或者短信模板中需要替换的变量字典,如{"code": 123456}
        """
        access_key_id = smss.get("SMS_ACCESS_KEY_ID")
        access_key_secret = smss.get("SMS_ACCESS_KEY_SECRET")
        sign_name = smss.get("SMS_SIGN_NAME")

        if not access_key_id:
            raise ValueError("sms loss of access_key_id")

        if not access_key_secret:
            raise ValueError("sms loss of access_key_secret")

        if not sign_name:
            raise ValueError("sms loss of sign name")

        if not phone:
            raise ValueError("sms loss of phone number")

        if not category:
            raise ValueError("sms template wrong")

        if not template_param:
            raise ValueError("sms template params wrong")

        self.asc_client = AcsClient(access_key_id, access_key_secret)
        self.phone = phone
        self.category = category
        self.template_param = template_param
        self.template_code = self.template_code()
        self.sign_name = sign_name
    
    def template_code(self):
        """
        根据category选择不同的模板编码
        :param self.category,dict
            authentication: 身份验证
            login_confirmation: 登陆验证
            login_exception: 登陆异常
            user_registration: 用户注册
            change_password: 修改密码
            information_change: 信息修改
        :return:
        """
        if self.category == "authentication":
            code = smss.get("AUTHENTICATION")
            if not code:
                raise ValueError("sms configuration loss of AUTHENTICATION")
            return code
        
        elif self.category == "login_confirmation":
            code = smss.get("LOGIN_CONFIRMATION")
            if not code:
                raise ValueError("sms configuration loss of LOGIN_CONFIRMATION")
            return code
        
        elif self.category == "login_exception":
            code = smss.get("LOGIN_EXCEPTION")
            if not code:
                raise ValueError("sms configuration loss of LOGIN_EXCEPTION")
            return code
        
        elif self.category == "user_registration":
            code = smss.get("USER_REGISTRATION")
            if not code:
                raise ValueError("sms configuration loss of USER_REGISTRATION")
            return code
        
        elif self.category == "change_password":
            code = smss.get("CHANGE_PASSWORD")
            if not code:
                raise ValueError("sms configuration loss of CHANGE_PASSWORD")
            return code
        
        elif self.category == "information_change":
            code = smss.get("INFORMATION_CHANGE")
            if not code:
                raise ValueError("sms configuration loss of INFORMATION_CHANGE")
            return code
        
        else:
            raise ValueError("sms category wrong")
    
    def send_sms(self):
        """
        发送短信
        :return:
        """
        sms_request = CommonRequest()

        # 固定设置
        sms_request.set_accept_format("json")
        sms_request.set_domain("dysmsapi.aliyuncs.com")
        sms_request.set_method("POST")
        sms_request.set_protocol_type("https")  # https | http
        sms_request.set_version("2017-05-25")
        sms_request.set_action_name("SendSms")

        # 发送短信的号码列表，必填
        sms_request.add_query_param("PhoneNumbers", self.phone)
        # 短信签名,必填
        sms_request.add_query_param("SignName", self.sign_name)

        # 申请的短信模板编码，必填
        sms_request.add_query_param("TemplateCode", self.template_code)

        # 短信模板变量参数,必填
        sms_request.add_query_param("TemplateParam", self.template_param)

        # 设置业务请求流水号，必填，暂用uuid1代替
        build_id = uuid.uuid1()
        sms_request.add_query_param("OutId", build_id)

        # 调用短信发送接口，返回json数据
        sms_response = self.asc_client.do_action_with_exception(sms_request)

        return sms_response


def phone_login_or_register(phone):
    """
    使用手机号登陆或者注册
    :param phone: str，手机号
    :return:
    """
    # 判断用户是否已经用手机注册,注册过了直接返回，没有则注册返回
    user_login = db.session.query(UserLoginMethod).filter(
        UserLoginMethod.login_method=="P",
        UserLoginMethod.identification==phone).first()

    if user_login:
        user = db.session.query(User.id, User.name).filter(
            User.id==user_login.user_id).first()
        data = dict(zip(user.keys(), user))
        return data
    else:
        try:
            new_user = User(name="nicename", age=20)
            db.session.add(new_user)
            db.session.flush()
            new_user_login = UserLoginMethod(
                user_id=new_user.id,
                login_method="P",
                identification=phone,
                access_code=""
            )
            db.session.add(new_user_login)
            db.session.flush()
            db.session.commit()
        except Exception as e:
            print(e)
            return None

        data = dict(id=new_user.id, name=new_user.name)
        return data
