# rpc（远程过程调用)介绍

<!-- TOC -->

- [rpc（远程过程调用)介绍](#rpc%e8%bf%9c%e7%a8%8b%e8%bf%87%e7%a8%8b%e8%b0%83%e7%94%a8%e4%bb%8b%e7%bb%8d)
  - [1.概念](#1%e6%a6%82%e5%bf%b5)
  - [2.常用的RPC技术和框架](#2%e5%b8%b8%e7%94%a8%e7%9a%84rpc%e6%8a%80%e6%9c%af%e5%92%8c%e6%a1%86%e6%9e%b6)
  - [3.rpc框架](#3rpc%e6%a1%86%e6%9e%b6)
  - [4.一次rpc调用流程](#4%e4%b8%80%e6%ac%a1rpc%e8%b0%83%e7%94%a8%e6%b5%81%e7%a8%8b)

<!-- /TOC -->

## 1.概念

一种通过网络从远程计算机程序上请求服务，而不需要了解底层网络技术的思想。`是一种技术思想，而不是一种规范或者协议`。

## 2.常用的RPC技术和框架

- 应用级的服务框架：
  - 阿里的 `Dubbo/Dubbox`
  - `Google gRPC`
  - `Spring Boot/Spring Cloud`
  - Twitter的`Finagle`
- 远程通信协议
  - `RMI`
  - `Socket`
  - `SOAP(HTTP XML)`
  - `REST(HTTP JSON)`
- 通信框架
  - `MINA`
  - `Netty`

## 3.rpc框架

[gorpc官方中文文档](http://doc.oschina.net/grpc?t=60133)

在一个典型 RPC 的使用场景中，包含了`服务发现`、`负载`、`容错`、`网络传输`、`序列化`等组件，其中“RPC 协议”就指明了程序如何进行网络传输和序列化。

一个 RPC 的核心功能主要有 5 个部分组成，分别是：`客户端`、`客户端 Stub`、`网络传输模块`、`服务端 Stub`、`服务端`等。

- `客户端(Client)`：服务调用方
- `客户端存根(Client Stub)`：存放服务端地址信息，将客户端的请求参数数据信息打包成网络消息，再通过网络传输发送给服务端
- `服务端存根(Server Stub)`：接收客户端发送过来的请求消息并进行解包，然后再调用本地服务进行处理
- `服务端(Server)`：服务的真正提供者
- `Network Service`：底层传输，可以是 TCP 或 HTTP

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
11. 服务消费方得到最终结果。