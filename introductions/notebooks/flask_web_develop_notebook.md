# flask web开发读书笔记

<!-- TOC -->

- [flask web开发读书笔记](#flask-web%e5%bc%80%e5%8f%91%e8%af%bb%e4%b9%a6%e7%ac%94%e8%ae%b0)
  - [1.flask简介](#1flask%e7%ae%80%e4%bb%8b)
    - [1.1上下文](#11%e4%b8%8a%e4%b8%8b%e6%96%87)
    - [1.2请求钩子](#12%e8%af%b7%e6%b1%82%e9%92%a9%e5%ad%90)
    - [Flask MethodView](#flask-methodview)

<!-- /TOC -->

## 1.flask简介

### 1.1上下文

临时将某些对象变为全局可以访问。

| 变量名 | 上下文 | 说明 |
| :-----: | :---: | :--- |
| current_app | 程序上下文 | 当前激活程序的实例 |
| g | 程序上下文 | 处理请求时用作临时存储的对象，每次请求都会重设这个变量 |
| request | 请求上下文 | 请求对象，封装了http请求 |
| session | 请求上下文 | 用户会话，用于存储请求之间需要记住的值的字典 |

### 1.2请求钩子

- 在请求发起之前或者之后执行的代码
- 请求钩子和视图函数之间共享数据一般使用上下文全局变量g

| 钩子 | 说明 |
| :---: | :--- |
| before_first_request | 注册一个函数，在处理第一个请求之前运行 |
| before_request | 注册一个函数，在每次请求之前运行 |
| after_request | 注册一个函数，没有异常的时候每次请求之后运行 |
| teardown_request | 注册一个函数，即使有异常，每次请求之后运行 |

### Flask MethodView

根据每个HTTP的方法执行不同的函数。
