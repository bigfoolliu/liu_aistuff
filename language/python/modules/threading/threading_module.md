# python threading模块使用示例

<!-- vim-markdown-toc Marked -->

* [1.基本类](#1.基本类)
* [2.Thread类](#2.thread类)
* [3.Lock类](#3.lock类)
* [4.Event类](#4.event类)

<!-- vim-markdown-toc -->

## 1.基本类

获取当前线程的名称：threading.currentThread().getName()

- `Thread`, 表示一个执行线程的对象
- `Lock`,锁对象
- `RLock`,可重入锁对象，使单一线程可以（再次）获得已持有的锁（递归锁）
- `Condition`,条件变量对象，使得一个线程等待另外一个线程满足特定的条件，比如改变状态或者某个数据值
- `Event`, 条件变量的通用版本，任意数量的线程等待某个事件的发生，在该事件发生后所有的线程都将被激活
- `Semaphore`,为线程间的有限资源提供一个计数器，如果没有可用资源时会被阻塞
- `BoundedSemaphore`，与Semaphore相似，不过它不允许超过初始值
- `Timer`，与Thread类似，不过它要在运行前等待一定时间
- `Barrier`,创建一个障碍，必须达到指定数量的线程后才可以继续

## 2.Thread类

Thread类属性:

- `name`, 线程名
- `ident`,线程的标识符
- `daemon`,布尔值，表示这个线程是否是守护线程

Thread类方法:

- __init__(group=None,target=None,name=None,args=(),kwargs={},verbose=None,daemon=None), 实例化一个线程对象，需要一个可调用的target对象，以及参数args或者kwargs。还可以传递name和group参数。daemon的值将会设定thread.daemon的属性
- `start()`, 开始执行该线程
- `run()`, 定义线程的方法。（通常开发者应该在子类中重写）
- `join(timeout=None)`, 直至启动的线程终止之前一直挂起；除非给出了timeout(单位秒)，否则一直被阻塞
- `isAlive`, 布尔值，表示这个线程是否还存活（驼峰式命名，python2.6版本开始已被取代）
- `isDaemon()`, 布尔值，表示是否是守护线程(已经弃用)
- `setDaemon(布尔值)`, 在线程start()之前调用，把线程的守护标识设定为指定的布尔值（已弃用）
- [介绍](https://www.cnblogs.com/hiwuchong/p/8673183.html)

## 3.Lock类

threading.Lock():

- 在多线程中使用lock可以让多个线程在共享资源的时候不会“乱”
- lock.acquire()
- lock.release()

## 4.Event类

threading.Event()：

- 可以创建一个事件管理标志，该标志（event）默认为False，event对象主要有四种方法可以调用：
- event.wait(timeout=None)：调用该方法的线程会被阻塞，如果设置了timeout参数，超时后，线程会停止阻塞继续执行；
- event.set()：将event的标志设置为True，调用wait方法的所有线程将被唤醒；
- event.clear()：将event的标志设置为False，调用wait方法的所有线程将被阻塞；
- event.isSet()：判断event的标志是否为True
