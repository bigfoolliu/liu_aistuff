# framework框架面试

<!-- TOC -->

- [framework框架面试](#framework%e6%a1%86%e6%9e%b6%e9%9d%a2%e8%af%95)
  - [1.Flask](#1flask)
    - [1.1Flask介绍](#11flask%e4%bb%8b%e7%bb%8d)
    - [1.2flask中的数据库连接方式](#12flask%e4%b8%ad%e7%9a%84%e6%95%b0%e6%8d%ae%e5%ba%93%e8%bf%9e%e6%8e%a5%e6%96%b9%e5%bc%8f)
    - [1.3flask依赖的组件](#13flask%e4%be%9d%e8%b5%96%e7%9a%84%e7%bb%84%e4%bb%b6)
    - [1.4蓝图的作用](#14%e8%93%9d%e5%9b%be%e7%9a%84%e4%bd%9c%e7%94%a8)
    - [1.5flask常用扩展包](#15flask%e5%b8%b8%e7%94%a8%e6%89%a9%e5%b1%95%e5%8c%85)
    - [1.6简述flask上下文管理](#16%e7%ae%80%e8%bf%b0flask%e4%b8%8a%e4%b8%8b%e6%96%87%e7%ae%a1%e7%90%86)
    - [1.7flask中g的作用](#17flask%e4%b8%adg%e7%9a%84%e4%bd%9c%e7%94%a8)
  - [2.Django](#2django)
  - [3.Tornado](#3tornado)

<!-- /TOC -->

## 1.Flask

### 1.1Flask介绍

- 一个可扩展，依赖少，轻量级的web框架
- 默认依赖两个外部库：jinja2，Werkzeug WSGI工具
- 适用于做小型网站以及web服务的API

### 1.2flask中的数据库连接方式

1. 使用第三方库正常连接，用sql语句操作数据库，如`pymysql`
2. 使用ORM进行数据库连接，如`flask_sqlalchemy`

### 1.3flask依赖的组件

- Route（路由）
- templates（模板）
- Models（orm模型）
- blueprint（蓝图）
- Jinjia2模板引擎

### 1.4蓝图的作用

```python
bp = Blueprint("book", __name__)
@bp.route("url")
```

- 将不同的功能模块化
- 构建大型应用
- 优化项目结构
- 增强可读性，易于维护

### 1.5flask常用扩展包

- Flask-SQLalchemy: 操作数据库
- Flask-migrate: 迁移数据库
- Flask-Mail: 邮件
- Flask-WTF: 表单
- Flask-Login: 认证用户状态
- Flask-OpenID: 认证
- Flask-RESTful: 开发REST API的工具
- Flask-Bootstrap: 集成前端框架Bootstrap
- Flask-Admin: 简单可扩展的管理接口

### 1.6简述flask上下文管理

**三个阶段：**

- `请求进来时`，将请求相关数据(Request对象，g对象等)放入上下文管理
- `视图函数中`，在上下文中管理中取值
- `请求响应`，将上下文管理中的数据清除

### 1.7flask中g的作用

- 贯穿一次请求的`全局变量`
- 请求进来时，封装为`AppContext`类，通过LocalStack放入Local中
- 取值时通过偏函数在LocalStack和Local中取值
- 响应时将Local中的g数据删除

## 2.Django

## 3.Tornado
