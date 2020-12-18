#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
sqlalchemy库基础
"""

import sqlalchemy
from sqlalchemy import create_engine, Integer, Column, String, JSON, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

print(sqlalchemy.__version__)

engine_url = open('../../../../private/mysql', encoding='utf-8').read()
print(engine_url)

# 基类
Base = declarative_base()

engine = create_engine(engine_url, echo=True)
# print(engine)

Session = sessionmaker(bind=engine)


# print(Session)


def init_db():
    Base.metadata.create_all(bind=engine)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    scores = Column(JSON)

    def __repr__(self):
        return f'User-{self.name}-{self.age}'

    @classmethod
    def create_data(cls, **kwargs):
        pass


# print(User.__table__)


def create_user(name, age, _session):
    user = User(name=name, age=age)
    _session.add(user)
    _session.commit()
    return user


def rollback_demo(_session):
    """回滚示例"""
    fake_user = create_user(name='john', age=11)
    _session.add(fake_user)  # 暂存
    _session.rollback()  # 回滚，取消暂存
    _session.close()


if __name__ == '__main__':
    session = Session()

    # init_db()

    print(Base.metadata.sorted_tables)

    # create_user(name='tony', age=10, session=session)

    # 基础的查询
    _query = session.query(User)  # select * from user
    print(_query)

    _list = _query.all()
    print(_list)

    _list1 = _query.filter(User.scores.in_([5, 6])).all()
    print(_list1)

    # JSON_CONTAINS, json类型的数据包含
    _list2 = _query.filter(func.json_contains(User.scores, '[5, 6]')).all()
    print(_list2)

    # 执行原生sql语句
    cursor = session.execute(r'select * from user;')
    ret = cursor.fetchall()
    cursor.close()
    print(f'ret: {ret}')

    print('done')
