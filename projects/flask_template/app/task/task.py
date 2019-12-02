#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu

from datetime import datetime

from app.models.model import User
from app.utils.core import db


def my_job():
    """自定义简单定时任务"""
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def db_query():
    """定时查询数据库的任务"""
    with db.app.app_context():
        data = db.session.query(User).first()
        print(data)
