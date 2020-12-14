# celery使用

<!-- vim-markdown-toc Marked -->

* [1.基本概念](#1.基本概念)
        - [1.1celery简介](#1.1celery简介)
        - [1.2工作流程](#1.2工作流程)
        - [1.3功能](#1.3功能)
        - [1.4安装使用](#1.4安装使用)
* [2.Brokers](#2.brokers)
        - [2.1基本介绍](#2.1基本介绍)
        - [2.2RabbitMQ](#2.2rabbitmq)
        - [2.3Redis](#2.3redis)
* [3.Backend](#3.backend)
        - [3.1基本介绍](#3.1基本介绍)
* [4.celery命令](#4.celery命令)
* [a.参考资料](#a.参考资料)

<!-- vim-markdown-toc -->

## 1.基本概念

### 1.1celery简介

- 通过`消息机制`通信,使用`中间人(broker)`作为客户端和`职程(worker)`调节
- 专门的职程(worker)来监视任务队列，进行执行新的任务
- 可一个有多个职程和多个中间人
- 可以在一台机器上运行，也可以在多台机器上运行，甚至可以跨数据中心运行; 可以通过暴露 HTTP 的方式进行，任务交互以及其它语言的集成开发

**特点：**

- 简单
- 高可用，丢失连接或连接失败会自动重连
- 快速，百万级/分钟
- 灵活，扩展性高，可自定义连接池、序列化方式、压缩方式、日志记录方式、任务调度、生产者、消费者、中间人（Broker）等

### 1.2工作流程

1. 启动一个任务
2. 客户端向向消息队列发送一个消息
3. 中间人将消息传递给一个职程
4. 职程执行具体的任务

### 1.3功能

- 监控，整个流程的监控
- 调度，支持cron表达式，定时执行任务
- 工作流，`canvas`组成工作流
- 资源(内存)泄漏保护，`--max-tasks-per-child` 参数适用于可能会出现资源泄漏（例如：内存泄漏）的任务
- 时间和速率的限制，控制单位时间执行任务的次数
- 自定义组件，可定制worker,worker是`bootsteps`构建的一个依赖关系图

### 1.4安装使用

```sh
# Celery 自定义了一组用于安装 Celery 和特定功能的依赖。
# 您可以在中括号加入您需要依赖，并可以通过逗号分割需要安装的多个依赖包。
pip3 install "celery[librabbitmq,redis,auth,msgpack]"
```

## 2.Brokers

### 2.1基本介绍

- 用来`存储消息`的中间装置

### 2.2RabbitMQ

- 默认的中间人
- 功能完备，稳定的并且易于安装的broker. 它是`生产环境中最优的选择`
- [使用rabbitmq作为celery的broker](http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html#broker-rabbitmq)

### 2.3Redis

- 功能完备的broker可选项，但是其更可能因意外中断或者电源故障导致数据丢失的情况
- [使用redis作为celery的broker](http://docs.celeryproject.org/en/latest/getting-started/brokers/redis.html#broker-redis)

```sh
# 使用redis作为中间人
pip3 intall -U "celery[redis]"  # 安装依赖库

# 配置broker为redis, uri的格式为: redis://:password@hostname:port/db_number
app.conf.broken_url = 'redis://localhost:6379/0'

# 配置可见性超时，可见性超时为将消息重新下发给另外一个程序之前等待确认的任务秒数（默认为1小时）
app.conf.broker_transport_options = {'visibility_timeout': 3600} # 一个小时

# 配置使用redis来保存结果
app.conf.result_backend = 'redis://localhost:7379/0'
```

## 3.Backend

### 3.1基本介绍

- Celery需要将结果保存到某个地方
- 有几种保存的方案可选:
    - - SQLAlchemy
    - - Django ORM
    - - Memcached
    - - Redis
    - - RPC (RabbitMQ/AMQP)



## 4.celery命令

```sh
celery -h  # 查看帮助



```

## a.参考资料

中文资料参考书：[celery中文手册](https://www.celerycn.io/)

- [celery初级教程(一)](https://blog.csdn.net/mbl114/article/details/78046694)
- [celery初级教程(二)](https://blog.csdn.net/mbl114/article/details/78046825)
- [celery初级教程(三)](https://blog.csdn.net/mbl114/article/details/78046888)
- [celery初级教程(四)](https://blog.csdn.net/mbl114/article/details/78046937)
- [celery初级教程(五)](https://blog.csdn.net/mbl114/article/details/78046961)
- [celery初级教程(六)](https://blog.csdn.net/mbl114/article/details/78047001)
- [celery初级教程(七)](https://blog.csdn.net/mbl114/article/details/78047032)
- [python之celery使用详解(一)](https://www.cnblogs.com/cwp-bg/p/8759638.html)
- [python之celery使用详解(二)](https://www.cnblogs.com/cwp-bg/p/10575688.html)

