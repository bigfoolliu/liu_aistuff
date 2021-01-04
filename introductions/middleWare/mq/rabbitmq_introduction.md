# RabbitMQ介绍

<!-- vim-markdown-toc Marked -->

* [1.概述](#1.概述)
    - [1.1简介](#1.1简介)
        + [1.1.1特点](#1.1.1特点)
        + [1.1.2功能](#1.1.2功能)
    - [1.2概念介绍](#1.2概念介绍)
        + [1.2.1Broker(消息中间件的服务节点)](#1.2.1broker(消息中间件的服务节点))
        + [1.2.2Virtual host(虚拟主机)](#1.2.2virtual-host(虚拟主机))
        + [1.2.3Connection(连接)](#1.2.3connection(连接))
        + [1.2.4Channel(信道)](#1.2.4channel(信道))
        + [1.2.5Exchange(交换器)](#1.2.5exchange(交换器))
        + [1.2.6Queue(队列)](#1.2.6queue(队列))
        + [1.2.7Binding(绑定)](#1.2.7binding(绑定))
        + [1.2.8Producer(生产者)](#1.2.8producer(生产者))
        + [1.2.9Consumer(消费者)](#1.2.9consumer(消费者))
* [2.安装使用](#2.安装使用)
    - [2.1window安装](#2.1window安装)
    - [2.2ubuntu安装](#2.2ubuntu安装)
    - [2.3Macos安装](#2.3macos安装)
* [3.rabbitmq命令](#3.rabbitmq命令)
* [4.工作模式](#4.工作模式)

<!-- vim-markdown-toc -->

## 1.概述

### 1.1简介

#### 1.1.1特点

- 主要思想非常简单:它`接受并转发消息`，基于AMQP协议实现,用于在分布式系统中存储转发消息
- [介绍](http://www.belonk.com/c/rabbitmq_intro_helloworld.html)
- [官网](https://www.rabbitmq.com/)
- [博客园:python操作rabbitmq]https://www.cnblogs.com/shenh/p/10497244.html()

#### 1.1.2功能

- 解耦
- 冗余(存储)
- 削峰
- 扩展性
- 可恢复性
- 顺序保证
- 缓冲
- 异步通信

### 1.2概念介绍

#### 1.2.1Broker(消息中间件的服务节点)

- 接收和分发消息的应用，RabbitMQ Server就是Message Broker
- 可以看作一台Rabbitmq的服务器

#### 1.2.2Virtual host(虚拟主机)

- 出于多租户和安全因素设计的，把AMQP的基本组件划分到一个虚拟的分组中，类似于网络中的namespace概念
- 当多个不同的用户使用同一个RabbitMQ server提供的服务时，可以划分出多个vhost，每个用户在自己的vhost创建exchange／queue等
- `类似于mysql中的数据库`

#### 1.2.3Connection(连接)

- publisher／consumer和broker之间的TCP连接
- 断开连接的操作只会在client端进行，Broker不会断开连接，除非出现网络故障或broker服务出现问题

#### 1.2.4Channel(信道)

- RabbitMQ都建立一个Connection开销巨大效率
- Channel是在connection内部建立的逻辑连接，Channel作为轻量级的Connection极大减少了操作系统建立TCP connection的开销

#### 1.2.5Exchange(交换器)

- 消息先到交换器，`交换器根据分发规则，匹配查询表中的routing key，将消息分发到队列中`
- 常用的类型有:
  1. `direct (point-to-point)`：bindingKey和routingKey进行`精确匹配`，适用于精确将消息发送给指定队列
  2. `topic (publish-subscribe)`：bindingKey和routingKey可进行`模糊匹配`，适用于将消息按照一定的规则发送到匹配的一个或多个队列
  3. `fanout`：广播，这种交换器可以`将消息广播给所有订阅的交换器`
  4. `headers`：不常用

#### 1.2.6Queue(队列)

- 用来存储消息
- 一条消息可以被同时拷贝到多个队列中

#### 1.2.7Binding(绑定)

- `交换器和队列之间的虚拟连接`，可包含`routing_key(路由键，生产者产生用来指定消息的路由，即目的地址),需要和交换器的绑定键(binding_key, 也是地址)联合使用`
- Binding信息被保存到exchange中的查询表中，用于message的分发依据

#### 1.2.8Producer(生产者)

- 发送`消息(标签+消息体)`的程序是生产者

#### 1.2.9Consumer(消费者)

- 通常为等待接收消息的应用程序
- `注意，生产者、消费者和消息代理不需要处于同一台主机上`，事实上，在大多数应用场景都是如此

## 2.安装使用

### 2.1window安装

- [Windows下RabbitMQ的安装和配置](https://blog.csdn.net/zhm3023/article/details/82217222)

### 2.2ubuntu安装

```sh
# 需要erlang环境
sudo apt-get install erlang-nox
# 查看erlang是否安装完成
erl

# 获取公钥
wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -

# 更新软件包并安装
sudo apt-get update
sudo apt-get install rabbitmq-server  # 安装成功自动启动

# 启动或者终止rabbitmq
service rabbitmq start
service rabbitmq stop
service rabbitmq restart

# 启动rabbitmq的web端需要配置插件，通过 http://localhost:15672 查看，使用默认账户guest/guest 登录
rabbitmq-plugins enable rabbitmq_management  # 启用插件
service rabbitmq-server restart  # 重启

# 查看rabbitmq的状态
systemctl status rabbitmq-server
service rabbitmq-server status
```

### 2.3Macos安装

```sh
# 安装rabbitmq
brew install rabbitmq

# 后台开启rabbitmq服务
brew services start rabbitmq

# 关闭后台rabbitmq服务
brew services stop rabbitmq

# 前台开启rabbitmq服务，需要将该配置PATH=$PATH:/usr/local/sbin
rabbitmq-server
```

## 3.rabbitmq命令

```sh
# 启动服务
sudo rabbitmqctl-server  # 前台启动
sudo rabbitmqctl-server --detached  # 后台启动

# 停止服务，永远不要用kill命令终止
sudo rabbitmqctl stop

# 查看所有的用户
rabbitmqctl list_users

# 增加普通用户
rabbitmqctl add_user admin password

# 给普通用户分配管理员角色
rabbitmqctl set_user_tags admin administrator


# 查看当前状态
rabbitmqctl status

# 查看集群的状态信息
rabbitmqctl cluster_status
```

## 4.工作模式

1. `simple`，简单队列
2. `work queues`，工作队列
3. `publish/subscribe`，发布订阅
4. `routing`，路由选择
5. `topics`，主题发送
6. `rpc`，远程过程调用
7. `publisher confirms`，发布者调用
