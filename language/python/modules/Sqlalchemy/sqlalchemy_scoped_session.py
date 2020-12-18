#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Sqlalchemy scoped_session演示

1. scoped_session 目的主要是为了线程安全
2. scoped_session类似单例模式，当我们调用使用的时候，会先在Registry里找找之前是否已经创建session了, 要是有，就把这个session返回,
    要是没有，就创建新的session，注册到Registry中以便下次返回给调用者
3. scoped_session的实现使用了thread local storage技术，使session实现了线程隔离。这样我们就只能看见本线程的session。

这样就实现了这样一个目的：在同一个线程中，call scoped_session 的时候，返回的是同一个对象


- 介绍: https://blog.csdn.net/lucyxu107/article/details/82699996
"""


from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from language.python.modules.Sqlalchemy.sqlalchemy_base import User, engine


# 获得session工厂
Session = sessionmaker(bind=engine)

# 获得scoped_session工厂
session = scoped_session(session_factory=Session)


def demo1():
    print('demo1')
    User.query = session.query_property()
    ret = User.query.all()
    print(f'ret: {ret}')


def demo2():
    print('demo2')
    _session = session()
    ret = _session.query(User).all()
    print(f'ret: {ret}')


def demo3():
    print('demo3')
    _session = session()
    cursor = _session.execute(r'select * from user limit 1;')
    print(f'cursor: {cursor}')
    ret = cursor.fetchall()
    print(f'ret: {ret}')


if __name__ == '__main__':
    demo3()