# framework框架面试

<!-- vim-markdown-toc Marked -->

* [1.Flask](#1.flask)
        - [1.1Flask介绍](#1.1flask介绍)
        - [1.2flask中的数据库连接方式](#1.2flask中的数据库连接方式)
        - [1.3flask依赖的组件](#1.3flask依赖的组件)
        - [1.4蓝图的作用](#1.4蓝图的作用)
        - [1.5flask常用扩展包](#1.5flask常用扩展包)
        - [1.6简述flask上下文管理](#1.6简述flask上下文管理)
        - [1.7flask中g的作用](#1.7flask中g的作用)
* [2.Django](#2.django)
* [3.Tornado](#3.tornado)

<!-- vim-markdown-toc -->

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

1. Django是走大而全的方向，它最出名的是其全自动化的管理后台：只需要使用起ORM，做简单的对象定义，它就能自动生成数据库结构、以及全功能的管理后台。

2. Django内置的ORM跟框架内的其他模块耦合程度高。应用程序必须使用Django内置的ORM，否则就不能享受到框架内提供的种种基于其ORM的便利；理论上可以切换掉其ORM模块，但这就相当于要把装修完毕的房子拆除重新装修，倒不如一开始就去毛胚房做全新的装修。

3. Django的卖点是超高的开发效率，其性能扩展有限；采用Django的项目，在流量达到一定规模后，都需要对其进行重构，才能满足性能的要求。

4. Django适用的是中小型的网站，或者是作为大型网站快速实现产品雏形的工具。

5. 5.Django模板的设计哲学是彻底的将代码、样式分离； Django从根本上杜绝在模板中进行编码、处理数据的可能。

MVC与MVT：

- M全拼为Model，主要封装对数据库层的访问，对数据库中的数据进行增、删、改、查操作。
- V全拼为View，用于封装结果，生成页面展示的html内容。
- C全拼为Controller，用于接收请求，处理业务逻辑，与Model和View交互，返回结果。

- M全拼为Model，与MVC中的M功能相同，负责和数据库交互，进行数据处理。
- V全拼为View，与MVC中的C功能相同，接收请求，进行业务处理，返回应答。
- T全拼为Template，与MVC中的V功能相同，负责封装构造要返回的html。

**两者的模板层相似，视图层不同，MVC（视图层用来展示界面），MVT（视图层用来控制业务流程，接受函数）。MVC（控制层用来接收参数，控制流程，分发请求），MVT（模板层用来展示页面，省去了分发请求的步骤，将其交给了django路由）.**

MVT是`一个请求一个坑`；MVC是`controller来分发请求`

## 3.Tornado
