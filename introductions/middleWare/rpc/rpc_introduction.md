# rpc（远程过程调用)介绍

<!-- vim-markdown-toc Marked -->

* [1.概述](#1.概述)
    - [1.1介绍](#1.1介绍)
    - [1.2参考](#1.2参考)
* [2.常用的RPC技术和框架](#2.常用的rpc技术和框架)
    - [2.1应用级的服务框架](#2.1应用级的服务框架)
        + [2.1.1阿里的 Dubbo/Dubbox](#2.1.1阿里的-dubbo/dubbox)
        + [2.1.2Google gRPC](#2.1.2google-grpc)
        + [2.1.3Spring Boot/Spring Cloud](#2.1.3spring-boot/spring-cloud)
        + [2.1.4Twitter的 Finagle](#2.1.4twitter的-finagle)
    - [2.2远程通信协议](#2.2远程通信协议)
        + [2.2.1RMI](#2.2.1rmi)
        + [2.2.2Socket](#2.2.2socket)
        + [2.2.3SOAP(HTTP XML)](#2.2.3soap(http-xml))
        + [2.2.4REST(HTTP JSON)](#2.2.4rest(http-json))
    - [2.3通信框架](#2.3通信框架)
        + [2.3.1MINA](#2.3.1mina)
        + [2.3.2Netty](#2.3.2netty)
* [3.rpc框架-grpc](#3.rpc框架-grpc)
    - [3.1grpc概述](#3.1grpc概述)
    - [3.2python使用grpc](#3.2python使用grpc)
* [4.一次rpc调用流程](#4.一次rpc调用流程)

<!-- vim-markdown-toc -->

## 1.概述

### 1.1介绍

- 即`远程过程调用`,一个服务调用封装在一个本地方法中，调用者像使用本地方法一样调用服务，对其屏蔽实现细节
- 具体的实现是通过调用方和服务方的一套约定，基于TCP长连接进行数据交互达成
- `调用redis,第三方服务的http接口广义上都是调用一次rpc服务`

**rpc特点：**

1. 具有需要约定调用语法
2. 需要约定内容编码方式
3. 需要网络传输

### 1.2参考

- [知乎:rpc概念](https://zhuanlan.zhihu.com/p/148139089)

## 2.常用的RPC技术和框架

### 2.1应用级的服务框架

#### 2.1.1阿里的 Dubbo/Dubbox

#### 2.1.2Google gRPC

**优缺点：**

- Protobuf进行数据编码，提高数据压缩率
- 使用HTTP2.0弥补了HTTP1.1的不足
- 同样在调用方和服务方使用协议约定文件，提供参数可选，为版本兼容留下缓冲空间

**特点：**

- 双方需要维护一个协议文件`*.proto`，proto命令对文件进行解析，会生成对应的Stub程序，客户端和服务端都需要保存这份Stub程序用来进行编解码

#### 2.1.3Spring Boot/Spring Cloud

#### 2.1.4Twitter的 Finagle

### 2.2远程通信协议

#### 2.2.1RMI

#### 2.2.2Socket

#### 2.2.3SOAP(HTTP XML)

#### 2.2.4REST(HTTP JSON)

- 支持广泛，是大多数时候的选择
- HTTP的header和Json的数据冗余和低压缩率使得传输性能差
- JSON难以表达复杂的参数类型，如结构体等

### 2.3通信框架

#### 2.3.1MINA

#### 2.3.2Netty

## 3.rpc框架-grpc

### 3.1grpc概述

- [grpc官方中文文档](http://doc.oschina.net/grpc?t=60133)
- 在一个典型 RPC 的使用场景中，包含了`服务发现`、`负载`、`容错`、`网络传输`、`序列化`等组件，其中“RPC 协议”就指明了程序如何进行网络传输和序列化。
- 一个 RPC 的核心功能主要有 5 个部分组成，分别是：`客户端`、`客户端 Stub`、`网络传输模块`、`服务端 Stub`、`服务端`等。

- `客户端(Client)`：服务调用方
- `客户端存根(Client Stub)`：存放服务端地址信息，将客户端的请求参数数据信息打包成网络消息，再通过网络传输发送给服务端
- `服务端存根(Server Stub)`：接收客户端发送过来的请求消息并进行解包，然后再调用本地服务进行处理
- `服务端(Server)`：服务的真正提供者
- `Network Service`：底层传输，可以是 TCP 或 HTTP

### 3.2python使用grpc

1. 在`.proto`文件中定义服务
2. 使用协议缓冲区编译器生成服务端和客户端代码
3. 使用python grpc api编写简单的客户端和服务端

```sh
# 使用grpc生成RPC代码
python -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/helloworld.proto
```

## 4.一次rpc调用流程

一次 RPC 调用流程如下：

1. 服务消费者(Client 客户端)通过本地调用的方式调用服务。
2. 客户端存根(Client Stub)接收到调用请求后负责将方法、入参等信息序列化(组装)成能够进行网络传输的消息体。
3. 客户端存根(Client Stub)找到远程的服务地址，并且将消息通过网络发送给服务端。
4. 服务端存根(Server Stub)收到消息后进行解码(反序列化操作)。
5. 服务端存根(Server Stub)根据解码结果调用本地的服务进行相关处理
6. 服务端(Server)本地服务业务处理。
7. 处理结果返回给服务端存根(Server Stub)。
8. 服务端存根(Server Stub)序列化结果。
9. 服务端存根(Server Stub)将结果通过网络发送至消费方。
10. 客户端存根(Client Stub)接收到消息，并进行解码(反序列化)。
11. 服务消费方得到最终结果
