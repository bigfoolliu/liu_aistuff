#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
gevent模块示例

- 主要使用gevent实现协程
- Python通过yield提供了对协程的基本支持，但是不完全。而第三方的gevent为Python提供了比较完善的协程支持。


gevent基本思想是：

1. gevent是python的一个并发框架，以微线程greenlet为核心，使用了epoll事件监听机制
2. 当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。
由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。

由于切换是在IO操作时自动完成，所以gevent需要修改Python自带的一些标准库，这一过程在启动时通过monkey patch完成。


gevent常用方法：

- gevent.spawn()	创建一个普通的Greenlet对象并切换
- gevent.spawn_later(seconds=3)	延时创建一个普通的Greenlet对象并切换
- gevent.spawn_raw()	创建的协程对象属于一个组
- gevent.getcurrent()	返回当前正在执行的greenlet
- gevent.joinall(jobs)	将协程任务添加到事件循环，接收一个任务列表
- gevent.wait()	可以替代join函数等待循环结束，也可以传入协程对象列表
- gevent.kill()	杀死一个协程
- gevent.killall()	杀死一个协程列表里的所有协程
- monkey.patch_all()	非常重要，会自动将python的一些标准模块替换成gevent框架
"""


import datetime
import requests
from gevent import monkey
import gevent

monkey.patch_socket()


def task1():
    for i in range(5):
        # 模拟耗时操作，每当遇到耗时操作就会切花到另外一个协程
        gevent.sleep(1)
        print("task1:", i)


def task2():
    for i in range(5):
        gevent.sleep(2)
        print("task2,", i)


def basic_demo():
    t1 = gevent.spawn(task1)
    t2 = gevent.spawn(task2)
    # 同一将协程阻塞或者单个
    # t1.join()
    gevent.joinall([t1, t2])


def task_get_url(url):
    print(f'time: {datetime.datetime.now()} url: {url}')
    resp = requests.get(url)
    print(f'time: {datetime.datetime.now()} url: {url}')
    print(f'{len(resp.text)} bytes received, {url}')


def demo2():
    gevent.joinall([
        gevent.spawn(task_get_url, 'https://www.python.org/'),
        gevent.spawn(task_get_url, 'https://github.com/'),
        gevent.spawn(task_get_url, 'https://www.baidu.com/'),
    ])



if __name__ == "__main__":
    # basic_demo()
    demo2()
