#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python threading模块使用示例


获取当前线程的名称：threading.currentThread().getName()

- Thread	表示一个执行线程的对象
- Lock	锁对象
- RLock	可重入锁对象，使单一线程可以（再次）获得已持有的锁（递归锁）
- Condition	条件变量对象，使得一个线程等待另外一个线程满足特定的条件，比如改变状态或者某个数据值
- Event　	条件变量的通用版本，任意数量的线程等待某个事件的发生，在该事件发生后所有的线程都将被激活
- Semaphore	为线程间的有限资源提供一个计数器，如果没有可用资源时会被阻塞
- BoundedSemaphore	于Semaphore相似，不过它不允许超过初始值
- Timer	于Thread类似，不过它要在运行前等待一定时间
- Barrier	创建一个障碍，必须达到指定数量的线程后才可以继续


Thread类属性:

- name	线程名
- ident	线程的标识符
- daemon	布尔值，表示这个线程是否是守护线程

Thread类方法:

- __init__(group=None,target=None,name=None,args=(),kwargs={},verbose=None,daemon=None)	实例化一个线程对象，需要一个可调用的target对象，以及参数args或者kwargs。还可以传递name和group参数。daemon的值将会设定thread.daemon的属性
- start()	开始执行该线程
- run()	定义线程的方法。（通常开发者应该在子类中重写）
- join(timeout=None)	直至启动的线程终止之前一直挂起；除非给出了timeout(单位秒)，否则一直被阻塞
- getName()	返回线程名（该方法已被弃用）
- setName()	设定线程名（该方法已弃用）
- isAlive	布尔值，表示这个线程是否还存活（驼峰式命名，python2.6版本开始已被取代）
- isDaemon()	布尔值，表示是否是守护线程(已经弃用)
- setDaemon(布尔值)	在线程start()之前调用，把线程的守护标识设定为指定的布尔值（已弃用）

https://www.cnblogs.com/hiwuchong/p/8673183.html


threading.Lock():

- 在多线程中使用lock可以让多个线程在共享资源的时候不会“乱”
- lock.acquire()
- lock.release()


threading.Event()：

- 可以创建一个事件管理标志，该标志（event）默认为False，event对象主要有四种方法可以调用：
- event.wait(timeout=None)：调用该方法的线程会被阻塞，如果设置了timeout参数，超时后，线程会停止阻塞继续执行；
- event.set()：将event的标志设置为True，调用wait方法的所有线程将被唤醒；
- event.clear()：将event的标志设置为False，调用wait方法的所有线程将被阻塞；
- event.isSet()：判断event的标志是否为True。
"""

import threading
from threading import Thread
import time

# 创建锁
lock = threading.Lock()
l = []

# 创建事件
event = threading.Event()

# 
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
    print("innner func demo end")
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
