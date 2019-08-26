# go框架之 macaron

<!-- TOC -->

- [go框架之 macaron](#go框架之-macaron)
    - [1.基本概念](#1基本概念)
        - [1.1macaron经典实例](#11macaron经典实例)
        - [1.2处理器(handler)](#12处理器handler)
        - [1.3服务注入](#13服务注入)
        - [1.4中间件机制](#14中间件机制)
        - [1.5macaron环境变量](#15macaron环境变量)
    - [2.核心服务](#2核心服务)
        - [2.1请求上下文(Context)](#21请求上下文context)
        - [2.2cookie](#22cookie)
        - [2.3设置/获取url参数](#23设置获取url参数)
        - [2.4获取查询参数](#24获取查询参数)
        - [2.5辅助方法](#25辅助方法)
        - [2.6响应流](#26响应流)
        - [2.7请求对象](#27请求对象)
        - [其他](#其他)
    - [3.路由模块](#3路由模块)
        - [3.1路由定义](#31路由定义)
        - [3.2命名参数](#32命名参数)
    - [4.模板引擎](#4模板引擎)
        - [4.1渲染html](#41渲染html)
        - [4.2渲染xml,json和原始数据](#42渲染xmljson和原始数据)
        - [4.3指定相应状态码](#43指定相应状态码)

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

### 2.2cookie

Cookie，设置 Cookie 最完整的用法为：`SetCookie("user", "unknwon", 999, "/", "localhost", true, true)`,参数的顺序是固定的。

如果需要更加安全的 Cookie 机制，可以先使用 `macaron.SetDefaultCookieSecret` 设定秘钥然后使用(这两个方法将会自动使用您设置的默认密钥进行加密/解密 Cookie 值)：

- `*macaron.Context.SetSecureCookie`
- `*macaron.Context.GetSecureCookie`

对于那些对安全性要求特别高的应用，可以为每次设置 Cookie 使用不同的密钥加密/解密：

- `*macaron.Context.SetSuperSecureCookie`
- `*macaron.Context.GetSuperSecureCookie`

```go
// 设置cookie
m.Get("/set", func(ctx *macaron.Context) {
    ctx.SetCookie("user", "Unknwon", 1)
})

// 获取cookie
m.Get("/get", func(ctx *macaron.Context) string {
    return ctx.GetCookie("user")
})
```

### 2.3设置/获取url参数

```go
// 设置url参数
m.Get("/set", func(ctx *macaron.Context) {
    name := ctx.SetParams("name", "new_name")
})

// 获取url参数
m.Get("/get/:name", func(ctx *macaron.Context) {
    name := ctx.Params("name")
})
```

其他：`ctx.ParamsEscape`、`ctx.ParamsInt`、`ctx.ParamsInt64`、`ctx.ParamsFloat64`

### 2.4获取查询参数

```go
// 获取查询参数
m.Get("/get", func(ctx *macaron.Context) {
    name := ctx.Query("name")  // 单个
    ids := ctx.QueryStrings("ids")  // 多个
})
```

其他：`ctx.QueryInt`、`ctx.QueryInt64`、`ctx.QueryFloat64`、`ctx.QueryTrim`

### 2.5辅助方法

- 服务内容或文件：`ctx.ServeContent`、`ctx.ServeFile`、`ctx.ServeFile`, `ctx.ServeFileContent`
- 获取远程 IP 地址：`ctx.RemoteAddr`

### 2.6响应流

```go
m.Get("/get", func(ctx *macaron.Context) {
    ctx.Resp.Write([]byte("the request path is : " + ctx.Req.RequestURI))
})
```

### 2.7请求对象

`请求体在每个请求中只能被读取一次`

```go
m.Get("/get", func(ctx *macaron.Context) {
    reader, err := ctx.Req.Body().ReadCloser()  // 获取io.ReadCloser类型的请求体
    data, err := ctx.Req.Body().Bytes()  // 获取[]byte类型的请求体
    data, err := ctx.Req.Body().String()  // 获取string类型的请求体
})
```

### 其他

1. Next()，可用于中间件处理器暂时放弃执行，等待其他处理器执行完毕后执行。`ctx.Next()`
2. 路由日志,`m.Use(macaron.Logger())`
3. 容错恢复`m.Use(macaron.Recovery())`
4. 静态文件`m.Use(macaron.Static("public"))`
5. 自定义选项,该服务允许接受第二个参数进行自定义选项操作`macaron.StaticOptions`
6. 全局日志,可选,`logger *log.Logger`
7. 相应流,可选，一般情况下可直接使用 `*macaron.Context.Resp`
8. 请求对象,可选，一般情况下可直接使用 `*macaron.Context.Req`

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
