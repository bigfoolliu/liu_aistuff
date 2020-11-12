#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu



"""
使用redis缓存html页面
直接缓存整个网页的情况是很少的
"""


import redis
from flask import Flask, request


app = Flask(__name__)
print(app)

@app.route('/index')
def index():
    conn = redis.Redis(connection_pool=pool)
    content = cache_request(conn, request.url, callback)
    return content


def cache_request(conn, request, callback):
    # 1.判断请求是否可以被缓存
    if not can_cache(conn,request):
        return callback(request)
    # 2.生成key
    page_key = "cache" + hash_request(request)
    print("page_key:",page_key)
    #3.判断是否已经被缓存
    content = conn.get(page_key)
    #如果没有被缓存，则生成缓存，过期时间300秒
    if not content:
        content = callback(request)
        conn.setex(page_key,300,content)
    return content


# 判断此请求是否应该被缓存
def can_cache(conn, request):
    return True


def hash_request(request):
    return str(hash(request))


def callback(request):
   return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    app.run(host='127.0.0.1', port=8080, debug=True)

