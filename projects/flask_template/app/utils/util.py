#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
统一封装response,通过装饰器的方式

flask视图函数通常返回三个内容:

1. 返回的数据
2. 状态码
3. 头部字典
"""


import base64
import io
import random
import re
import string
from functools import wraps

import redis
from flask import current_app, jsonify
from PIL import Image, ImageDraw, ImageFont

from app.utils.response import ResMsg


def route(bp, *args, **kwargs):
    """
    路由设置，统一返回格式
    :param bp: 蓝图
    : return: 
    """
    kwargs.setdefault("strict_slashes", False)

    def decorator(f):
        @bp.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*args, **kwargs):
            rv = f(*args, **kwargs)
            # 视图函数返回整型和浮点型
            if isinstance(rv, (int, float)):
                res = ResMsg()
                res.update(data=rv)
                return jsonify(res.data)
            # 视图函数返回元组
            elif isinstance(rv, tuple):
                if len(rv) >= 3:
                    return jsonify(rv[0], rv[1], rv[2])
                else:
                    return jsonify(rv[0], rv[1])
            # 视图函数返回字典
            elif isinstance(rv, dict):
                return jsonify(rv)
            # 视图函数返回字节
            elif isinstance(rv, bytes):
                rv = rv.decode("utf-8")
                return jsonify(rv)
            else:
                return jsonify(rv)
        return f
    return decorator


def view_route(f):
    """
    路由装饰器，返回同一的格式
    :param f: 被装饰函数
    """
    
    def decorator(*args, **kwargs):
        rv = f(*args, **kwargs)
        if isinstance(rv, (int, float)):
            res = ResMsg()
            res.update(data=rv)
            return jsonify(res.data)
        elif isinstance(rv, tuple):
            if len(rv) >= 3:
                return jsonify(rv[0]), rv[1], rv[2]
            else:
                return jsonify(rv[0]), rv[1]
        elif isinstance(rv, dict):
            return jsonify(rv)
        elif isinstance(rv, bytes):
            rv.decode("utf-8")
            return jsonify(rv)
        else:
            return jsonify(rv)

    return decorator


class Redis(object):
    """封装对redis的操作"""

    @staticmethod
    def _get_r():
        """获取Redis操作对象"""
        db = current_app.config["REDIS_DB"]
        host = current_app.config["REDIS_HOST"]
        port = current_app.config["REDIS_PORT"]
        r = redis.StrictRedis(host=host, port=port, db=db)
        return r
    
    @classmethod
    def write(cls, key, value, expire=None):
        """
        写入键值对
        :param expire: int,过期时间(s)
        """
        if expire:
            expire_seconds = expire
        else:
            expire_seconds = current_app.config["REDIS_EXPIRE"]
        r = cls._get_r()
        r.set(key, value, ex=expire_seconds)
    
    @classmethod
    def read(cls, key):
        """读取键值对"""
        r = cls._get_r()
        value = r.get(key)
        return value.decode("utf-8") if value else value
    
    @classmethod
    def hset(cls, name, key, value):
        """写入hash表"""
        r = cls._get_r()
        r.hset(name, key, value)
    
    @classmethod
    def hmset(cls, key, *value):
        """读取hash表的指定字段"""
        r = cls._get_r()
        value = r.hmset(key, *value)
        return value
    
    @classmethod
    def hget(cls, name, key):
        """读取指定hash表的所有的值"""
        r = cls._get_r()
        value = r.hget(name, key)
        return value.decode("utf-8") if value else value

    @classmethod
    def hgetall(cls, name):
        """获取指定hash表的所有值"""
        r = cls._get_r()
        value = r.hgetall(name)
        return value
    
    @classmethod
    def delete(cls, *names):
        """删除一个或者多个"""
        r = cls._get_r()
        r.delete(*names)
    
    @classmethod
    def hdel(cls, name, key):
        """删除指定hash表的键值"""
        r = cls._get_r()
        r.hdel(name, key)
    
    @classmethod
    def expire(cls, name, expire=None):
        """设置过期时间"""
        if expire:
            expire_seconds = expire
        else:
            expire_seconds = current_app.config["REDIS_EXPIRE"]
        r = cls._get_r()
        r.expire(name, expire_seconds)


class CaptchaTool(object):
    """创建图形验证码"""

    def __init__(self, width=50, height=20):
        self.width = width
        self.height = height
        self.im = Image.new("RGB", (width, height), "white")
        self.font = ImageFont.load_default()
        self.draw = ImageDraw.Draw(self.im)
    
    def draw_line(self, num=3):
        """划线"""
        for i in range(num):
            x1 = random.randint(0, self.width/2)
            y1 = random.randint(0, self.height/2)
            x2 = random.randint(0, self.width)
            y2 = random.randint(0, self.height)
            self.draw.line(((x1, y1), (x2, y2)), fill="black", width=1)
    
    def get_verify_code(self):
        """
        生成验证码
        :return img_str: str,验证码图片的字符串形式
        :return code: str,生成的随机四位数字验证码
        """
        # 生成随机四位数字
        code = "".join(random.sample(string.digits, 4))
        for item in range(4):
            self.draw.text((6+random.randint(-3, 3)+10*item, 2+random.randint(-2, 2)),
                            text=code[item],
                            fill=(random.randint(32, 127),
                                random.randint(32, 127),
                                random.randint(32, 127)),
                            font=self.font)
        self.im = self.im.resize((100, 24))
        # 将图片转换为base64格式字符串
        buffered = io.BytesIO()
        self.im.save(buffered, format="JPEG")
        img_str = b"data:image/png;base64," + base64.b64encode(buffered.getvalue())
        return img_str, code


class PhoneTool(object):
    """
    手机号码验证工具
    """
    
    @staticmethod
    def check_phone(phone):
        """
        检查传来的号码是否为手机号
        :param phone: str
        :return:
        """
        if not phone or not len(phone) == 11:
            return None
        
        v_phone = re.match(r"^1[3-9][0-9]{9}$", phone)
        if not v_phone:
            return None
        else:
            phone = v_phone.group()
            return phone
    
    @staticmethod
    def check_phone_code(phone, code):
        """
        检查手机号码和验证码是否正确
        :param phone: str，手机号码
        :param code: str，验证码
        :return: bool
        """
        re_phone = PhoneTool.check_phone(phone)
        if not re_phone:
            return False
        
        # 将传入的验证码和存储在redis中的对比
        r_code = Redis.hget(re_phone, "code")
        if code == r_code:
            return True
        else:
            return False
