#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
dbutils模块

- 允许以安全有效的方式连接线程化的Python应用程序和数据库
- python实现的线程化数据库连接(连接池)，DBUtils支持所有遵循 DP-API 2规范的数据库连接模块，例如：mysql、sqlserver、oracle、sqlite3等


dbutils提供两种外部接口： 

* PersistentDB ：提供线程专用的数据库连接，并自动管理连接。 
* PooledDB ：提供线程间可共享的数据库连接，并自动管理连接。


推荐用法以及步骤:

PooledDB, 创建一批连接供所有的线程共享使用

1. POOL = PooledDB()  - 实例化池对象，写入池的配置信息；创建一批连接放入连接池，共享使用
2. conn = POOL.connection() - 池连接
3. conn.cursor().execute('select * from user') - 执行SQL语句
4. conn.cursor().fetchall() - 获取执行SQL后的返回
5. conn.close() - 未关闭连接，只是将连接放回池子，供所有线程共享使用；当线程终止时，连接自动关闭；
"""

import os

import pymysql
from dbutils.pooled_db import PooledDB


pwd = os.getenv('pwd')


def demo():
    POOL = PooledDB(creator=pymysql,  # 使用连接数据库的模块
                    mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
                    maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
                    maxshared=3,  # # 链接池中最多共享的链接数量，0和None表示全部共享
                    maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
                    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
                    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
                    setsession=[],  # 开始会话前执行的命令列表
                    reset=True,
                    failures=None,
                    ping=0,
                    host='127.0.0.1',  # ping MySQL服务端，检查是否服务可用
                    port=3306,
                    user='root',
                    password=pwd,
                    database='liu',
                    charset='utf8')

    print(POOL, dir(POOL))
    
    
    # 检测当前正在运行连接数的是否小于最大链接数，如果不小于则：等待或报raise TooManyConnections异常
    # 否则 则优先去初始化时创建的链接中获取链接 SteadyDBConnection。
    # 然后将SteadyDBConnection对象封装到PooledDedicatedDBConnection中并返回。
    # 如果最开始创建的链接没有链接，则去创建一个SteadyDBConnection对象，再封装到PooledDedicatedDBConnection中并返回。
    # 一旦关闭链接后，连接就返回到连接池让后续线程继续使用。
    conn = POOL.connection()
    
    cursor = conn.cursor()
    cursor.execute('select * from user')
    result = cursor.fetchall()

    print(result)

    conn.close()


if __name__ == "__main__":
    demo()

