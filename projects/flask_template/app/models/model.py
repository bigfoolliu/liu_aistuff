#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
模型类
"""


from app.utils.core import db


class User(db.Model):
    """
    用户表
    """
    __tablename__ = "user"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20), nullable=False)  # 用户姓名
    age = db.Column(db.Integer, nullable=False)  # 用户年龄


class Article(db.Model):
    """
    文章表
    """
    __tablename__ = "article"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(20), nullable=False)  # 文章标题
    body = db.Column(db.String(255), nullable=False)  # 文章内容
    last_change_time = db.Column(db.DateTime, nullable=False)  # 最后一次修改的时间
    # 作者，同时设置外键，注意user是表的名字，而不是类的名字
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # backref用于在关系另一端的类中快捷地创建一个指向当前类对象的属性，注意User是类的名字
    author = db.relationship("User", backref=db.backref("articles"))


class ChangeLogs(db.Model):
    """
    修改日志
    """
    __tablename__ = "change_logs"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    article_id = db.Column(db.Integer, db.ForeignKey("article.id"))
    modify_context = db.Column(db.String(255), nullable=True)  # 修改内容
    create_time = db.Column(db.DateTime, nullable=False)  # 创建日期
