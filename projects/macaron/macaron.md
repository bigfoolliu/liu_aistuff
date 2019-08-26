# go框架之 macaron

<!-- TOC -->

- [go框架之 macaron](#go%e6%a1%86%e6%9e%b6%e4%b9%8b-macaron)
  - [1.基本概念](#1%e5%9f%ba%e6%9c%ac%e6%a6%82%e5%bf%b5)
    - [1.1macaron经典实例](#11macaron%e7%bb%8f%e5%85%b8%e5%ae%9e%e4%be%8b)
    - [1.2处理器(handler)](#12%e5%a4%84%e7%90%86%e5%99%a8handler)
    - [1.3服务注入](#13%e6%9c%8d%e5%8a%a1%e6%b3%a8%e5%85%a5)
    - [1.4中间件机制](#14%e4%b8%ad%e9%97%b4%e4%bb%b6%e6%9c%ba%e5%88%b6)
    - [1.5macaron环境变量](#15macaron%e7%8e%af%e5%a2%83%e5%8f%98%e9%87%8f)
  - [2.核心服务](#2%e6%a0%b8%e5%bf%83%e6%9c%8d%e5%8a%a1)
    - [2.1请求上下文(Context)](#21%e8%af%b7%e6%b1%82%e4%b8%8a%e4%b8%8b%e6%96%87context)
    - [2.2其他](#22%e5%85%b6%e4%bb%96)
  - [3.路由模块](#3%e8%b7%af%e7%94%b1%e6%a8%a1%e5%9d%97)
    - [3.1路由定义](#31%e8%b7%af%e7%94%b1%e5%ae%9a%e4%b9%89)
    - [3.2命名参数](#32%e5%91%bd%e5%90%8d%e5%8f%82%e6%95%b0)
  - [4.模板引擎](#4%e6%a8%a1%e6%9d%bf%e5%bc%95%e6%93%8e)
    - [4.1渲染html](#41%e6%b8%b2%e6%9f%93html)
    - [4.2渲染xml,json和原始数据](#42%e6%b8%b2%e6%9f%93xmljson%e5%92%8c%e5%8e%9f%e5%a7%8b%e6%95%b0%e6%8d%ae)
    - [4.3指定相应状态码](#43%e6%8c%87%e5%ae%9a%e7%9b%b8%e5%ba%94%e7%8a%b6%e6%80%81%e7%a0%81)

<!-- /TOC -->

## 1.基本概念

[官方文档](https://go-macaron.com/docs/middlewares)

### 1.1macaron经典实例

```go
// 创建一个macaron经典实例
m := macaron.Classic()
```

下面是 macaron.Classic 已经包含的功能：

- 请求/响应日志 - macaron.Logger
- 容错恢复 - macaron.Recovery
- 静态文件服务 - macaron.Static

### 1.2处理器(handler)

1. 一个处理器基本上可以是任何的函数
2. 要将同一个函数作用于多个路由，则可以使用一个命名函数
3. 同一个路由还可以注册任意多个处理器

### 1.3服务注入

下面的这些服务已经被包含在经典 Macaron 中（macaron.Classic）中间:

1. `*macaron.Context` - HTTP 请求上下文
2. `*log.Logger` - Macaron 全局日志器
3. `http.ResponseWriter` - HTTP 响应流
4. `*http.Request` - HTTP 请求对象

### 1.4中间件机制

中间件处理器是工作于请求和路由之间的。本质上来说和 Macaron 其他的处理器没有分别。

```go
m.Use(func() {
// 处理中间件事务
})
```

### 1.5macaron环境变量

`macaron.env`来查看环境变量。
建议使用环境变量 MACARON_ENV=production 来指示当前的模式为部署模式.

## 2.核心服务

### 2.1请求上下文(Context)

包含了您所需要的请求对象、响应流、模板引擎接口、数据存储和注入与获取其它服务.

```go
func Home(ctx *macaron.Context) {
    // ...
}
```

### 2.2其他

1. Next()，可用于中间件处理器暂时放弃执行，等待其他处理器执行完毕后执行。`ctx.Next()`
2. Cookie，`*macaron.Context.SetCookie`, `*macaron.Context.GetCookie`,设置时候参数固定(`SetCookie(<name>, <value>, <max age>, <path>, <domain>, <secure>, <http only>)`)
3. 路由日志,`m.Use(macaron.Logger())`
4. 容错恢复`m.Use(macaron.Recovery())`
5. 静态文件`m.Use(macaron.Static("public"))`
6. 自定义选项,该服务允许接受第二个参数进行自定义选项操作`macaron.StaticOptions`
7. 全局日志,可选,`logger *log.Logger`
8. 相应流,可选，一般情况下可直接使用 `*macaron.Context.Resp`
9. 请求对象,可选，一般情况下可直接使用 `*macaron.Context.Req`

## 3.路由模块

### 3.1路由定义

```go
m.Get("/", func() {
    // show something
})

m.Post("/", func() {
    // create something
})
```

### 3.2命名参数

`*Context.Params`来获取。

```go
// 从路由表中匹配参数
m.Get("/hello/:name", func(ctx *macaron.Context) string {
    return "Hello " + ctx.Params(":name")
    // 或者去掉: return "Hello " + ctx.Params("name")
})
```

## 4.模板引擎

[官方文档](https://gowalker.org/html/template)两款官方模板引擎中间件可供选择，即`macaron.Renderer`和`pongo2.Pongoer`.

共有特性：

1. 均支持 XML、JSON 和原始数据格式的响应，它们之间的不同只体现在 HTML 渲染上。
2. 均使用 templates 作为默认模板文件目录。
3. 均使用 .tmpl 和 .html 作为默认模板文件后缀。
4. 均支持通过 Macaron 环境变量 来判断是否缓存模板文件（当 macaron.Env == macaron.PROD 时）

### 4.1渲染html

该服务可以通过函数`macaron.Renderer`来注入，并通过类型`macaron.Render`来体现。该服务为可选，一般情况下可直接使用`*macaron.Context.Render`.

```go
m.Use(macaron.Renderer())
ctx.HTML(200, "hello")
```

### 4.2渲染xml,json和原始数据

```go
type Person struct {
    Name string
    Age  int
    Sex  string
}

m.Use(macaron.Renderer())

p := Person{"Unknwon", 21, "male"}

// 渲染xml
ctx.XML(200, &p)
// 渲染json
ctx.JSON(200, &p)
// 渲染原始数据
ctx.RawData(200, []byte("raw data goes here"))
// 渲染文本
ctx.PlainText(200, []byte("plain text goes here"))
```

### 4.3指定相应状态码

```go
// 指定状态码
ctx.Status(403)
// 指定错误码
ctx.Error(500)
// 设置重定向
ctx.Redirect("/")
```
