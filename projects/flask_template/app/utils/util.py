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


from functools import wraps

import redis
from flask import current_app, jsonify

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
        r.expire(name, expire=expire_seconds)
