#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
单表接口，主要对一个数据表的增删改查，不会对其他的数据表造成干扰
"""


import logging

from flask import current_app, request
from flask.views import MethodView
from sqlalchemy import inspect

from app.utils.core import db
from app.utils.response import ResMsg, ResponseCode
from app.utils.util import view_route

logger = logging.getLogger(__name__)


class BaseParse(object):
    """
    基础字段解析类
    识别要查询的字段
    """

    __model__ = None
    __request__ = request
    by = frozenset(["by"])
    query = frozenset(["gt", "ge", "lt", "le", "ne", "eq", "ic", "ni", "in"])  # 查询操作

    def __init__(self):
        self._operator_funcs = {
            "gt": self.__gt_model,
            "ge": self.__ge_model,
            "lt": self.__lt_model,
            "le": self.__le_model,
            "ne": self.__ne_model,
            "eq": self.__eq_model,
            "ic": self.__ic_model,
            "ni": self.__ni_model,
            "by": self.__by_model,
            "in": self.__in_model,
        }
    
    def _parse_page_size(self):
        """
        获取页码和获取每页的数据量
        :return page: 页码
                page_size: 每页的数据量
        """
        default_page = current_app.config["DEFAULT_PAGE_INDEX"]
        default_size = current_app.config["DEFAULT_PAGE_SIZE"]
        page = self.__request__.args.get("page", default_page)
        page_size = self.__request__.args.get("page_size", default_size)
        page = int(page) - 1
        page_size = int(page_size)
        return page, page_size
    
    def _parse_query_field(self):
        """
        解析查询字段
        :return query_field: 查询字段
                by_field: 排序字段
        """
        args = self.__request__.args
        query_field = list()
        by_field = list()
        for query_key, query_value in args.items():
            key_split = query_key.split("_", 1)
            if len(key_split) != 2:
                continue
            operator, key = key_split
            if not self._check_key(key=key):
                continue
            if operator in self.query:
                data = self._operator_funcs[operator](key=key, value=query_value)
                query_field.append(data)
            elif operator in self.by:
                data = self._operator_funcs[operator](key=key, value=query_value)
                by_field.append(data)
        return query_field, by_field
    
    def _parse_create_field(self):
        """
        解析创建字段,并判断字段是否为model的字段并过滤无关字段
        list(dict) ==> list(dict)
        dict ==> list(dict)
        """
        obj = self.__request__.get_json(force=True)
        if isinstance(obj, list):
            create_field = list()
            for item in obj:
                if isinstance(item, dict):
                    base_dict = self._parse_field(obj=item)
                    create_field.append(base_dict)
            return create_field
        elif isinstance(obj, dict):
            return [self._parse_field(obj=obj)]
        else:
            return list()
    
    def _parse_field(self, obj=None):
        """
        检查字段模型中是否有，并删除主键值
        :param obj:
        :return:
        """
        obj = obj if obj is not None else self.__request__.get_json(force=True)
        field = dict()
        # 获取model的主键,TODO:需要理解inspect函数的意义
        primary_key = map(lambda x: x.name, inspect(self.__model__).primary_key)

        for key, value in obj.items():
            if key in primary_key:
                continue
            if self._check_key(key):
                field[key] = value
        return field
    
    def _check_key(self, key):
        """
        检查model是否存在key
        :param key:
        :return:
        """
        if hasattr(self.__model__, key):
            return True
        else:
            return False
    
    def __gt_model(self, key, value):
        """大于"""
        return getattr(self.__model__, key) > value
    
    def __ge_model(self, key, value):
        """大于等于"""
        return getattr(self.__model__, key) >= value
    
    def __lt_model(self, key, value):
        """小于"""
        return getattr(self.__model__, key) < value
    
    def __le_model(self, key, value):
        """小于等于"""
        return getattr(self.__model__, key) <= value
    
    def __eq_model(self, key, value):
        """等于"""
        return getattr(self.__model__, key) == value
    
    def __ne_model(self, key, value):
        """不等于"""
        return getattr(self.__model__, key) != value
    
    def __ic_model(self, key, value):
        """包含于"""
        return getattr(self.__model__, key).like("%{}%".format(value))
    
    def __ni_model(self, key, value):
        """不包含于"""
        return getattr(self.__model__, key).notlike("%{}%".format(value))
    
    def __by_model(self, key, value):
        """
        :param value: 0：正序，1：倒序
        """
        try:
            value = int(value)
        except ValueError as e:
            logger.error(e)
            # TODO:需要知道asc作用
            return getattr(self.__model__, key).asc()
        else:
            if value == 1:
                return getattr(self.__model__, key).asc()  # 正序
            elif value == 0:
                return getattr(self.__model__, key).desc()  # 降序
            else:
                return getattr(self.__model__, key).asc()
    
    def __in_model(self, key, value):
        """查询多个相同字段的值"""
        value = value.split("|")
        return getattr(self.__model__, key).in_(value)


class BaseQuery(object):
    """
    基础查询类
    """

    __model__ = None

    def _find(self, query):
        """根据查询参数获取内容"""
        return self.__model__.query.filter(*query).all()
    
    def _find_by_page(self, page, size, query, by):
        """根据查询参数，分页，排序获取内容"""
        base = self.__model__.query.filter(*query).order_by(*by)
        cnt = base.count()
        data = base.slice(page*size, (page+1)*size).all()
        return cnt, data
    
    def _get(self, key):
        """根据主键id获取数据"""
        return self.__model__.query.get(key)
    
    def _create(self, args):
        """创建一条新的数据或者批量新建"""
        for base in args:
            model = self.__model__()
            for k, v in base.items():
                setattr(model, k, v)
            db.session.add(model)
        try:
            db.session.commit()
            return True
        except Exception as e:
            logger.error(e)
            return False
    
    def _update(self, key, kwargs):
        """更新数据"""
        model = self._get(key)
        if model:
            for k, v in kwargs.items():
                setattr(model, k, v)
            try:
                db.session.add(model)
                db.session.commit()
                return True
            except Exception as e:
                logger.error(e)
                return False
        else:
            return False
    
    def _delete(self, key):
        """删除数据"""
        model = self._get(key)
        if model:
            try:
                db.session.delete(model)
                db.session.commit()
                return True
            except Exception as e:
                logger.error(e)
                return False
        else:
            return False
    
    def parse_data(self, data):
        """解析查询的数据,获取模型对象的属性"""
        if data:
            if isinstance(data, (list, tuple)):
                data = list(map(lambda x: {p.key: getattr(x, p.key)
                                            for p in self.__model__.__mapper__.iterate_properties
                                            }, data))
            else:
                data = {p.key: getattr(data, p.key) for p in self.__model__.__mapper__.iterate_properties}
        
        return data


class Service(BaseParse, BaseQuery, MethodView):
    """将数据解析，数据查询，以及对请求的分发结合起来
    就可以自定义不同的http请求的逻辑，完成单表接口"""

    __model__ = None

    # 装饰器控制数据返回格式
    decorators = [view_route]

    def get(self, key=None):
        """获取列表或者单表数据"""
        res = ResMsg()
        # 获取单表的信息
        if key is not None:
            data = self.parse_data(self._get(key=key))
            print(data, type(data))
            if data:
                res.update(data=data)
            else:
                res.update(code=ResponseCode.NO_RESOURCE_FOUND)
        # 获取列表的信息
        else:
            query, by = self._parse_query_field()
            page, size = self._parse_page_size()
            cnt, data = self._find_by_page(page=page, size=size, query=query, by=by)
            data = self.parse_data(data)
            if data:
                res.update(data=data)
            else:
                res.update(code=ResponseCode.NO_RESOURCE_FOUND)
            # 在响应中多增加几条字段
            res.add_field(name="total", value=cnt)
            res.add_field(name="page", value=page+1)
            res.add_field(name="size", value=size)
            res.update(data=data)
        return res.data
    
    def post(self):
        """创建单条或者多条数据"""
        res = ResMsg()
        data = self._parse_create_field()
        if data:
            if not self._create(args=data):
                res.update(code=ResponseCode.FAIL)
        else:
            res.update(code=ResponseCode.INVALID_PARAMETER)
        return res.data
    
    def put(self, key=None):
        """更新某条数据"""
        res = ResMsg()
        if key is None:
            res.update(code=ResponseCode.INVALID_PARAMETER)
        else:
            data = self._parse_field()
            if not self._update(key=key, kwargs=data):
                res.update(code=ResponseCode.FAIL)
        return res.data
    
    def delete(self, key=None):
        """删除某条数据"""
        res = ResMsg()
        if key is None:
            res.update(code=ResponseCode.INVALID_PARAMETER)
        elif not self._delete(key=key):
            res.update(code=ResponseCode.FAIL)
        return res.data
