# 分布式介绍

<!-- vim-markdown-toc Marked -->

* [1.分布式常用技术](#1.分布式常用技术)
* [2.分布式系统技术](#2.分布式系统技术)
    - [2.1提高架构性能](#2.1提高架构性能)
    - [2.2提高架构可用性](#2.2提高架构可用性)

<!-- vim-markdown-toc -->

## 1.分布式常用技术

- [知乎：分布式常用技术](https://zhuanlan.zhihu.com/p/83160424)

1. 分布式系统常用架构体系
    - 基于对象的架构
    - 面向服务的架构(SOA)
    - REST风格架构
    - 微服务架构(MSA)
    - 容器技术
    - Serverless架构
2. 分布式消息服务
    - ActiveMQ
    - RabbitMQ
    - RocketMQ
    - Kafka
3. 分布式计算
    - MapReduce
    - Hadoop
    - Spark
    - Mesos
4. 分布式存储
    - Bigtable
    - HBase
    - Memcached
    - Reids
    - MongoDB
5. 分布式监控
    - Nagios
    - Zabbix
    - Consul
    - Zookeeper
6. 分布式版本控制
    - Git
    - Bazaar
    - Mercurial
7. RESTfulAPI、微服务及容器技术
    - Jersey
    - Spring boot
    - Docker

## 2.分布式系统技术

### 2.1提高架构性能

1. 加缓存，缓存分区，缓存更新，缓存命中
2. 负载均衡，网关系统，服务路由，服务发现
3. 异步调用，消息队列，消息持久化，异步事务
4. 数据镜像，数据同步，读写分离，数据一致性
5. 数据分区，分区策略，数据访问性，数据一致性

### 2.2提高架构可用性

1. 服务拆分，服务治理，调用，依赖，隔离
2. 服务冗余，弹性伸缩，故障迁移，服务发现
3. 限流降级，异步队列，降级控制，服务熔断
4. 高可用架构，多租户系统，灾备多活，高可用服务
5. 高可用运维，全栈监控，DevOps，自动化运维
