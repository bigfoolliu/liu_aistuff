#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python threading模块使用示例

"""

import threading
from threading import Thread
import time

# 创建锁
lock = threading.Lock()
l = []

# 创建事件
event = threading.Event()

# a创建全局的ThreadLocal对象，可以用来存储各个线程的变量，即线程局部变量
# 用来替换即iii要陪你的udjaa
local_obj = threading.local()


def task(num):
    """
    耗时任务
    :param num: int
    """
    time.sleep(num)
    print("task: ", num)
    return


def no_lock_append_task(i):
    """未使用锁的情况下向全局变量列表l中添加元素"""
    global l
    l.append(i)
    print("no lock l:", l)


def lock_append_task(i):
    """
    使用锁的情况下向全局变量列表l中添加元素
    """
    global l
    lock.acquire(blocking=True, timeout=2)  # 获取锁
    l.append(i)
    print("lock l:", l)
    lock.release()  # 释放锁


def event_task():
    """事件的任务"""
    print("event waiting signal")
    event.wait()  # 等待事件的标志位为True才执行后面的代码
    print("event {} is running".format(threading.current_thread().getName()))


class MyThread(Thread):
    """派生出一个线程类,通过重写run方法，来执行某项任务"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        print("my thread runing...")
        time.sleep(3)
        print("my thread end")


def thread_demo():
    """
    join ()方法:
    主线程A中，创建了子线程B，并且在主线程A中调用了B.join()
    那么，主线程A会在调用的地方等待，直到子线程B完成操作后，才可以接着往下执行，
    那么在调用这个线程时可以使用被调用线程的join方法
    """
    # 创建线程并传递任务和参数
    t = Thread(target=task, args=[2, ])
    t.start()
    t.join(timeout=1)  # 阻塞


def thread_demo2():
    """
    setDaemon()方法
    主线程A中，创建了子线程B，并且在主线程A中调用了B.setDaemon(),这个的意思是
    把主线程A设置为守护线程，这时候，要是主线程A执行结束了，就不管子线程B是否完成,
    一并和主线程A退出.这就是setDaemon方法的含义，这基本和join是相反的。
    此外，还有个要特别注意的：必须在start() 方法调用之前设置，如果不设置为守护线程，程序会被无限挂起。
    """
    t = Thread(target=task, args=[3, ])
    print(t.is_alive())
    # t.setDaemon()
    t.daemon = True
    t.name = "stupid thread"
    t.start()
    print(t.is_alive())
    print(t.name)


def mythread_demo():
    """使用自定义的线程类来执行任务"""
    my_t = MyThread()
    my_t.start()
    my_t.join()


def lock_demo():
    """
    是否使用锁的示例

    """
    # for i in range(10):
    #     t = Thread(target=no_lock_append_task, args=[i,])
    #     t.start()

    for i in range(10):
        t = Thread(target=lock_append_task, args=[i, ])
        t.start()


def event_demo():
    """使用事件的示例"""
    t = Thread(target=event_task)
    print("thread start")
    t.start()
    # t.join()
    print("event set signal")
    # 将event信号设置为True，此时t才从阻塞的地方继续执行
    event.set()


def inner_func_demo(session_id=1):

    print("innerfunc demo start")
    t1 = time.time()
    def inner_func():
        print("inner func start")
        time.sleep(3)
        print(f"session_id:{session_id}")
        print("inner func end")

    def inner_func2():
        print("inner func2 start")
        time.sleep(5)
        print(f"2 session_id:{session_id}")
        print("inner func2 end")


    inner_thread = threading.Thread(target=inner_func)
    inner_thread.start()
    # inner_thread.join()   # 写在这里会一直阻塞
    inner2_thread = threading.Thread(target=inner_func2)
    inner2_thread.start()

    inner_thread.join()   # 写在这里不会一直阻塞
    inner2_thread.join()
    print("inner func demo end")
    print(f"time: {time.time()-t1}")


if __name__ == "__main__":
    print("main start")
    # thread_demo()
    # thread_demo2()
    # mythread_demo()
    # lock_demo()
    # event_demo()
    inner_func_demo()
    print("main end")
