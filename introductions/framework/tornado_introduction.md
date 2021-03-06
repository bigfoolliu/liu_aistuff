# tornado web框架介绍

<!-- vim-markdown-toc Marked -->

* [1.概述](#1.概述)
    - [1.1基础](#1.1基础)
    - [1.2特点](#1.2特点)
    - [1.3tornado协程(coroutine)原理](#1.3tornado协程(coroutine)原理)
    - [1.4tornado,flask,django的区别](#1.4tornado,flask,django的区别)
* [2.常见函数和方法](#2.常见函数和方法)
* [3.运行和部署的方式](#3.运行和部署的方式)
    - [3.1使用内置的HTTPServer](#3.1使用内置的httpserver)
    - [3.2在负载均衡器（如nginx）后面运行](#3.2在负载均衡器（如nginx）后面运行)
* [4.tornado异步](#4.tornado异步)

<!-- vim-markdown-toc -->

## 1.概述

### 1.1基础

- [参照教程](https://www.tornadoweb.org/en/stable/guide/structure.html)
- [tornado源码解析](http://www.nowamagic.net/academy/detail/13321002)
- [Introduction to tornado中文版](http://demo.pythoner.com/itt2zh/index.html)

一个普通的tornado web服务器通常由四大组件组成:

1. `ioloop实例`，它是全局的tornado事件循环，是服务器的引擎核心，示例中tornado.ioloop.IOLoop.current()就是默认的tornado ioloop实例。
2. `app实例`，它代表着一个完成的后端app，它会挂接一个服务端套接字端口对外提供服务。一个ioloop实例里面可以有多个app实例，示例中只有1个，实际上可以允许多个，不过一般几乎不会使用多个。
3. `handler类`，它代表着业务逻辑，我们进行服务端开发时就是编写一堆一堆的handler用来服务客户端请求。
4. `路由表`，它将指定的url规则和handler挂接起来，形成一个路由映射表。当请求到来时，根据请求的访问url查询路由映射表来找到相应的业务handler。

其中，**一个ioloop包含多个app(管理多个服务端口)，一个app包含一个路由表，一个路由表包含多个handler，当一个请求到来时，ioloop读取这个请求解包成一个http请求对象，找到该套接字上对应app的路由表，通过请求对象的url查询路由表中挂接的handler，然后执行handler。handler方法执行后一般会返回一个对象，ioloop负责将对象包装成http响应对象序列化发送给客户端。**

### 1.2特点

- `异步非阻塞`, [tornado的异步非阻塞](https://www.cnblogs.com/becker/p/9335136.html)
- 为减小并发连接的开销,使用`单线程事件循环`,即所有代码都应是异步和非阻塞的,因为在同一时刻只有一个操作是有效的
- 推荐用`协程`来编写异步代码

最小的hello-world程序:

```python
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    # 创建的Application对象负责全局配置，包括将请求映射到路由表里面
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
```

### 1.3tornado协程(coroutine)原理

- [csdn:tornado协程工作原理](https://blog.csdn.net/wyx819/article/details/45420017)

### 1.4tornado,flask,django的区别

**底层io处理机制：**

1. tornado，自带异步特性，底层io处理机制是`事件循环+协程`
2. django, flask， 传统的模型，同步框架，阻塞io模型。api写同步代码，使用celery/APScheduler处理异步任务

**性能对比：**

1. 基本的json序列化：django和flask占优
2. 处理远程http的请求的能力：tornado占有优势
3. 数据库和模板处理性能：tornado和flask相当， Django ORM很慢,但开发效率与维护好，深度绑定了该框架，若换成其它轮子，意味着诸多优秀特性消失

## 2.常见函数和方法

```python
self.write()
self.render()

self.get_query_argument()
self.get_body_argument()

self.reverse_url()
self.redirect()
```

## 3.运行和部署的方式

### 3.1使用内置的HTTPServer

### 3.2在负载均衡器（如nginx）后面运行

```sh
# nginx的一项配置
http {
    # Enumerate all the Tornado servers here(列举所有的Tornado服务器)
    upstream frontends {
        server 127.0.0.1:8000;
        server 127.0.0.1:8001;
        server 127.0.0.1:8002;
        server 127.0.0.1:8003;
    }
```

## 4.tornado异步

- tornado默认是单进程，单线程
- 为减小并发开销，使用一种单线程事件循环方式，所有代码都是异步非阻塞的
- 其中使用`协程`来写异步代码，使用`yield`替代链式回调，实现挂起

几种类型的异步接口：

1. 回调函数(基本不用)
2. tornado协程 + 生成器
3. tornado协程 + Future
4. 线程池，进程池
