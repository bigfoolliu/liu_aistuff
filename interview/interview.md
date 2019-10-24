# interview面试问题总结

<!-- TOC -->

- [interview面试问题总结](#interview%e9%9d%a2%e8%af%95%e9%97%ae%e9%a2%98%e6%80%bb%e7%bb%93)
  - [1.tcp/udp](#1tcpudp)
    - [适用场景](#%e9%80%82%e7%94%a8%e5%9c%ba%e6%99%af)
    - [tcp粘包](#tcp%e7%b2%98%e5%8c%85)
  - [2.进程线程](#2%e8%bf%9b%e7%a8%8b%e7%ba%bf%e7%a8%8b)
  - [3.高并发](#3%e9%ab%98%e5%b9%b6%e5%8f%91)
    - [3.1提升系统并发能力](#31%e6%8f%90%e5%8d%87%e7%b3%bb%e7%bb%9f%e5%b9%b6%e5%8f%91%e8%83%bd%e5%8a%9b)
    - [3.2高并发指标](#32%e9%ab%98%e5%b9%b6%e5%8f%91%e6%8c%87%e6%a0%87)
    - [3.3python解决高并发](#33python%e8%a7%a3%e5%86%b3%e9%ab%98%e5%b9%b6%e5%8f%91)
  - [4.go语言](#4go%e8%af%ad%e8%a8%80)
    - [4.1go与python对比](#41go%e4%b8%8epython%e5%af%b9%e6%af%94)
  - [5.缓存](#5%e7%bc%93%e5%ad%98)
    - [5.1缓存介绍](#51%e7%bc%93%e5%ad%98%e4%bb%8b%e7%bb%8d)
    - [浏览器缓存](#%e6%b5%8f%e8%a7%88%e5%99%a8%e7%bc%93%e5%ad%98)
  - [概念](#%e6%a6%82%e5%bf%b5)
    - [领域驱动模型(DDD)](#%e9%a2%86%e5%9f%9f%e9%a9%b1%e5%8a%a8%e6%a8%a1%e5%9e%8bddd)
  - [web框架的本质](#web%e6%a1%86%e6%9e%b6%e7%9a%84%e6%9c%ac%e8%b4%a8)
  - [其他](#%e5%85%b6%e4%bb%96)
  - [python](#python)

<!-- /TOC -->

概念回答原则：

1. **What**，这个概念是什么
2. **Why**，为什么存在
3. **How**，怎么使用

## 1.tcp/udp

### 适用场景

- udp提供的无状态的连接，适合语音，直播，视频等
- tcp面向连接，适合文件传输，远程登录

### tcp粘包

- [什么是TCP粘包以及如何解决](https://blog.csdn.net/weixin_41047704/article/details/85340311)

原因：

1. 当连续发送数据时候，TCP的nagle算法将较小的内容拼接为大的内容，一次性发送，造成粘包;
2. 发送的数据较大时，服务端的buff_size较小，不能一次性接收所有的内容，下次请求到达时候接收的是上次没有完全接收完的东西，造成粘包。

## 2.进程线程

## 3.高并发

`高并发`指的是系统能够同时并行处理多个请求。

参考:

- [Python高并发详解](https://www.cnblogs.com/daofaziran/p/10154986.html)

### 3.1提升系统并发能力

1. 垂直扩展
   1. 增加单机硬件性能,更好的cpu, ssd, 更大的内存
   2. 提升单机架构性能，减少cache来减少IO次数，使用异步来增加单服务吞吐量
2. 水平扩展
   1. 增加服务器的数量
   2. 反向代理层：通过DNS轮询，`dns-server对于一个域名配置多个解析ip,每次DNS解析请求来访问dns-server，会轮询返回ip`
   3. 站点层：通过`改nginx.conf，配置多个web后端`
   4. 服务层：通过`服务连接池`实现，站点层的RPC-client与下游服务建立多个连接，服务成为瓶颈的时候，只要增加服务器数量即可
   5. 数据层：`主从同步`等

### 3.2高并发指标

- 响应时间
- 吞吐量
- 每秒查询率
- 并发用户数

### 3.3python解决高并发

1. HTML页面静态化
2. 图片服务器分离
3. 使用缓存(使用redis作为缓存的数据库)
4. 数据库集群，库表散列
5. 使用负载均衡

    ```nginx
    <!-- 简单的负载均衡nginx配置 -->
    upstream myserver {
        server 192.168.72.49:8080;
        server 192.168.72.49:8081;
    }
    ```

6. 镜像，CDN加速等

## 4.go语言

### 4.1go与python对比

- [go语言与python对比](https://zhuanlan.zhihu.com/p/62728193)
- go因为是编译型语言，大部分情况下执行速度更快
- go内建并发机制
- go相对更适合系统编程
- go作为静态型语言，更易于在编译时捕获BUG

## 5.缓存

### 5.1缓存介绍

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

### 浏览器缓存

`通过响应头告知浏览器该资源是否应该缓存`

- `Expires`: 告知客户端资源缓存失效的绝对时间
- `Cache-Control`：控制缓存的行为
- `Last-Modified`：资源最后一次修改的时间
- `ETag`: 服务器生成资源的唯一标识

## 概念

### 领域驱动模型(DDD)

[基于领域驱动模型架构设计的京东用户管理后台](https://www.cnblogs.com/wanghzh/p/5847643.html)
[领域驱动模型(DDD)介绍](https://www.jianshu.com/p/fb319d7674ff)

企业级应用设计目录架构：

- Infrastructure：一些公共组件，例如md5加密，分页模块，session等。
- Model ：关于数据库的逻辑处理模块
- Repository ：数据访问层，包含数据库的增删改查
- Service ：服务层，调用Model，包含带有规则的请求和返回
- Statics：静态文件目录
- UI层：业务处理
- Views：模板文件
- Application：tornado程序的起始文件
- Config：配置文件
- Mapper：依赖注入文件，负责整个框架不同类的依赖注入

## web框架的本质

[web框架的本质以及自定义简单web框架](https://www.cnblogs.com/wanghzh/p/5807883.html)

- web应用的本质就是socket服务端，浏览器就是socket客户端
- python的web框架遵循相同的WSGI标准，从而可以互相配和使用

## 其他

- [python实现支持并发以及断点续传的FTP程序](https://www.cnblogs.com/wanghzh/p/5571122.html)
- [白话https加密机制](https://www.cnblogs.com/jymblog/p/11646766.html)

## python
