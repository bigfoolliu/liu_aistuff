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

from flask import jsonify
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
