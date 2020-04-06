# RESTful API实践

<!-- vim-markdown-toc Marked -->

* [1.url设计](#1.url设计)
        * [1.1动词即对应的5种HTTP方法](#1.1动词即对应的5种http方法)
        * [1.2宾语则必须是名词](#1.2宾语则必须是名词)
        * [1.3动词的覆盖](#1.3动词的覆盖)
        * [1.4复数url](#1.4复数url)
        * [1.5避免多级url](#1.5避免多级url)
* [2.状态码](#2.状态码)
        * [2.1状态码必须明确](#2.1状态码必须明确)
* [3.api](#3.api)
        * [3.1 open api](#3.1-open-api)
* [ａ.api,sdk,app的区别](#ａ.api,sdk,app的区别)

<!-- vim-markdown-toc -->

***核心思想：客户端发出的数据操作指令都是"动词 + 宾语"结构。***

## 1.url设计

### 1.1动词即对应的5种HTTP方法

- GET：读取（Read）
- POST：新建（Create）
- PUT：更新（Update）
- PATCH：更新（Update），通常是部分更新
- DELETE：删除（Delete）

### 1.2宾语则必须是名词

### 1.3动词的覆盖

有些客户端只能使用GET和POST这两种方法。服务器必须接受POST模拟其他三个方法（PUT、PATCH、DELETE）。

这时，客户端发出的 HTTP 请求，要加上X-HTTP-Method-Override属性，告诉服务器应该使用哪一个动词，覆盖POST方法。

```text
POST /api/Person/4 HTTP/1.1  
X-HTTP-Method-Override: PUT
```

上面代码中，X-HTTP-Method-Override指定本次请求的方法是PUT，而不是POST。

### 1.4复数url

无统一规定，因为常见的操作都是读取一个集合，所有使用复数。如：GET /books。

### 1.5避免多级url

- 多级url不利于扩展
- 语义不明确
- **尽量使用查询字符串。**

## 2.状态码

### 2.1状态码必须明确

***每一次的请求,服务器都必须做出回应，包括状态码和数据两部分。***

HTTP状态码:

- [常用HTTP状态码](https://www.runoob.com/http/http-status-codes.html)：

- 1xx：相关信息
- 2xx：操作成功
- 3xx：重定向
- 4xx：客户端错误
- 5xx：服务器错误

| 状态码 | 英文名称 | 中文描述 |
| :------: | :------ | :------ |
| 100 | Continue | 继续，客户端应该继续请求 |
| 200 | OK | 请求成功，一般用于GET和POST请求 |
| 204 | No Content | 无内容，服务器处理成功，但是未返回内容 |
| 206 | Partical Content | 部分内容，服务器成功处理了部分Get请求 |
| 300 | Multiple Choices | 多种选择，请求的资源包含多个位置，相应可以返回一个资源特征与地址的列表用于用户终端 |
| 301 | Moved Permanently | 永久移动，请求的资源永久移动到新的URI，返回信息会包括新的URI |
| 304 | Not Modified | 未修改，所请求的数据没有变化，服务端不会返回资源 |
| 307 | Temporary Redirect | 临时重定向 |
| 400 | Bad Request | 客户端请求错误 |
| 401 | Unauthorized | 请求要求用户的身份认证 |
| 403 | Forbidden | 服务端理解客户端请求，但是拒绝执行 |
| 404 | Not Found | 服务器找不到请求的资源 |
| 500 | Internal Server Error | 服务器内部错误，无法完成该请求 |
| 502 | Bad Gateway | 网关或者代理服务器接收尝试执行请求时，从远程服务器接收到无效的响应 |
| 503 | Service Unaviable | 超载或者系统维护，服务器暂时无法处理客户端的请求 |

## 3.api

- 应用程序接口，是一组预先定义好的函数，便于访问一组资源或者软硬件，而不需访问源码或者了解内部工作细节
- 大到两个完整的不同的系统，小到两段程序

**api分类：**

- 系统级api(和硬件等交互)
- 非系统级api

- 开放式api(open api)
- 私有api

### 3.1 open api

- 将网站的服务封装成一系列计算机易识别的数据接口开放，允许任务人的调用
- 可以对一些原有的碎片化数据进行重组，使其变得有关联

**open api分类：**

- 标准api
- 专有api

## ａ.api,sdk,app的区别

`API`：预先定义好的统一接口
`SDK`：调用API实现功能，是你的车轮和引擎,包含了使用 API 的必需资料
`APP`：你造出来的宇宙飞船~
