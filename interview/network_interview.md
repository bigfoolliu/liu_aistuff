# 网络面试

<!-- vim-markdown-toc Marked -->

* [4.缓存](#4.缓存)
    - [4.1缓存介绍](#4.1缓存介绍)
    - [4.2浏览器缓存](#4.2浏览器缓存)
* [5.授权](#5.授权)
    - [5.1OAuth2.0](#5.1oauth2.0)
* [8.socket编程](#8.socket编程)
* [9.DNS介绍](#9.dns介绍)
    - [9.1域名系统](#9.1域名系统)
* [a.常见面试题](#a.常见面试题)
    - [a.1web框架的本质](#a.1web框架的本质)
    - [a.2浏览器与服务器的TCP连接是否在一个Http请求完成后断开？什么时候断开](#a.2浏览器与服务器的tcp连接是否在一个http请求完成后断开？什么时候断开)
    - [a.3一个tcp连接可以对应多少http请求](#a.3一个tcp连接可以对应多少http请求)
    - [a.4一个tcp连接中的多个http请求发送可以发送吗](#a.4一个tcp连接中的多个http请求发送可以发送吗)
    - [a.5为什么有时候tcp连接不需要ssl连接](#a.5为什么有时候tcp连接不需要ssl连接)
    - [a.6浏览器对同一host建立的tcp连接数量是否有限制](#a.6浏览器对同一host建立的tcp连接数量是否有限制)
    - [a.7html包含多张图片，其是以什么方式，什么顺序，建立了多少连接，使用什么协议下载的](#a.7html包含多张图片，其是以什么方式，什么顺序，建立了多少连接，使用什么协议下载的)

<!-- vim-markdown-toc -->


## 4.缓存

### 4.1缓存介绍

- [缓存介绍](https://juejin.im/post/5a6c87c46fb9a01ca560b4d7)
- [你应该知道的缓存进化史](https://juejin.im/post/5b7593496fb9a009b62904fa#comment)
- [如何优雅的设计和使用缓存](https://juejin.im/post/5b849878e51d4538c77a974a)
- `保存资源副本并在下一次请求时候直接使用该副本。`

**缓存优点**：

- 不用每次去请求资源，缓解服务器压力
- 因为是打开本地资源，所以提升了性能
- 减少了带宽消耗

**缓存分类**：

- 宏观
  - `私有缓存`: 用户专享的，各级代理不能缓存的缓存
  - `共享缓存`：能被各级代理缓存的缓存
- 微观
  - `浏览器缓存`
  - `代理服务器缓存`
  - `网关缓存`
  - `数据库缓存`

### 4.2浏览器缓存

- [浏览器缓存机制](https://www.cnblogs.com/skynet/archive/2012/11/28/2792503.html)

`通过响应头告知浏览器该资源是否应该缓存`

- `Expires`: 告知客户端资源缓存失效的绝对时间
- `Cache-Control`：控制缓存的行为
- `Last-Modified`：资源最后一次修改的时间
- `ETag`: 服务器生成资源的唯一标识

## 5.授权

### 5.1OAuth2.0

- [阮一峰:OAuth2.0简单解释](http://www.ruanyifeng.com/blog/2019/04/oauth_design.html)

OAuth2.0的四种方式:

1. `授权码`，第三方应用先申请一个授权码，然后利用授权码获得令牌，最常用，且安全性高
2. `隐藏式`，适用于纯前端应用，直接向前端颁发令牌，省略了授权码步骤
3. `密码式`，对于高度信任的应用，直接将用户名以及密码告诉第三方应用
4. `凭证式`，适用于没有前端的应用，直接在命令行下申请令牌

## 8.socket编程

`socket = ip_address + tcp/udp + port`

- ![socket概念](./imgs/socket_concept.png)

## 9.DNS介绍

- [从理论到实践，全方位认识DNS（理论篇）](https://mp.weixin.qq.com/s?__biz=MzAwNDc0MTUxMw==&mid=2649639532&idx=1&sn=19b504cc7a0363d7913022d7dbda4b38&scene=21#wechat_redirect)
- [想搭建自己的网站？先来学点DNS知识吧](https://mp.weixin.qq.com/s?__biz=MzAwNDc0MTUxMw==&mid=2649639534&idx=1&sn=40c5a4b33230be3740e6d38b430a70fb&chksm=833daa88b44a239e452cca8a5c28063dc65df594f7cfc690f92c45c0b33cf9a68c11e01abfa1&mpshare=1&scene=24&srcid=&sharer_sharetime=1573843712975&sharer_shareid=20ab6c09eef32b49dbe03904652b9eb2#rd)
- [DNS域名解析协议详解](https://blog.csdn.net/baidu_37964071/article/details/80500825)
- [DNS解析过程详解](https://www.cnblogs.com/liyuanhong/articles/7353974.html)

### 9.1域名系统

- 一种层次的基于域的命名方案，基于分布式数据库系统实现
- 应用程序向域名服务器发送DNS请求，DNS服务器返回该域名对应的ip地址
  1. 用户计算机不存储所有的名字到ip的映射
  2. 规定了域名的命名规则，保证主机名字不会重复
  3. dns服务器不是单一的服务器，而是一个层次的，合理组织的服务器集群

```sh
# 查询域名服务器
nslookup www.baidu.com
```

- [python实现简单的域名服务器](../python/python/other/dns_python.py)

## a.常见面试题

### a.1web框架的本质

- [web框架的本质以及自定义简单web框架](https://www.cnblogs.com/wanghzh/p/5807883.html)
- web应用的本质就是socket服务端，浏览器就是socket客户端
- python的web框架遵循相同的WSGI标准，从而可以互相配和使用

### a.2浏览器与服务器的TCP连接是否在一个Http请求完成后断开？什么时候断开

- http1.0中默认一个http响应后会断开tcp连接；请求头的connection的keep-alive设置完成http响应不断开tcp连接
- http1.1将connection头写入标准，除非申明connection为close才断开

### a.3一个tcp连接可以对应多少http请求

- 不维持tcp连接，对应一个
- 维持tcp连接，对应多个

### a.4一个tcp连接中的多个http请求发送可以发送吗

- http1.1存在pipelining可以完成，但是浏览器默认关闭，且实现比较复杂
- http2.0使用multiplexing技术可以实现多个http请求在同一个tcp连接中并行执行

### a.5为什么有时候tcp连接不需要ssl连接

tcp连接没有断开，仍然使用之前的ssl.

### a.6浏览器对同一host建立的tcp连接数量是否有限制

- 对于http1.1，没有多路传输，有限制，chrome最多允许同一个host建立6个tcp连接

### a.7html包含多张图片，其是以什么方式，什么顺序，建立了多少连接，使用什么协议下载的

- 如果是https且在同一个域名下，浏览器在ssl握手之后和服务器协商是否可以使用http2.0从而使用multiplexing多路传输下载，不一定只使用一个tcp连接
- 如果不能使用https和http2.0，浏览器会建立多个tcp连接（连接数量取决于浏览器设置），这些连接在空闲的时候被浏览器用来发送行新的请求，如果所有连接都被占用则等待有空闲的连接
