#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
SQLAlchemy库使用
"""

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Integer, String, Column


with open('../../../private/mysql', mode='r') as f:
    mysql = f.read()
    print(mysql)


# orm的基类
Base = declarative_base()


def show_version():
    print(sqlalchemy.__version__)


def create_db():
    """创建数据库连接"""
    return create_engine('{}'.format(mysql), encoding='utf-8', echo=True)


def create_session():
    """创建会话，用以操作数据库"""
    db = create_db()
    Session = sessionmaker(db)
    session = Session()  # 使用的是实例化后的Session
    return session


def create_all_table():
    """修改表格的时候就需要运行来更改表结构"""
    db = create_db()
    Base.metadata.create_all(db)


class User(Base):

    """至少需要一个表名和一个主键列"""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    age = Column(Integer, default=5)

    def __repr__(self):
        return 'User(name: {}, email: {})'.format(self.name, self.email)


def create_user(name, email):
    return User(name=name, email=email)


def add_user(user):
    session = create_session()
    session.add(user)
    session.commit()


def query_demo():
    """查询示例"""
    session = create_session()
    ret = session.query(User).filter(User.name.in_(['Liu1'])).all()
    print(ret)


def rollback_demo():
    """回滚示例"""
    session = create_session()
    fake_user = create_user('fake', 'fake@a.com')
    session.add(fake_user)  # 暂存
    all_users = session.query(User).all()
    print('all_users:{}'.format(all_users))
    session.rollback()  # 回滚，取消暂存
    new_all_users = session.query(User).all()
    print('new_all_users:{}'.format(new_all_users))


if __name__ == '__main__':
    create_all_table()
    # test_user = create_user('liu1', '1231@qq.com')
    # add_user(test_user)
    # query_demo()
    # rollback_demo()
