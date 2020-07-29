# 后端架构图谱

<!-- vim-markdown-toc Marked -->

* [1.数据结构](#1.数据结构)
* [2.常用算法](#2.常用算法)
* [3.并发](#3.并发)
* [4.操作系统](#4.操作系统)
* [5.设计模式](#5.设计模式)
* [6.运维&统计&技术支持](#6.运维&统计&技术支持)
* [7.中间件](#7.中间件)
* [8.网络](#8.网络)
* [9.数据库](#9.数据库)
* [10.搜索引擎](#10.搜索引擎)
* [11.性能](#11.性能)
* [12.大数据](#12.大数据)
* [13.安全](#13.安全)
* [14.常用开源框架](#14.常用开源框架)
* [15.分布式设计](#15.分布式设计)
* [16.设计思想&开发模式](#16.设计思想&开发模式)
* [17.项目管理](#17.项目管理)
* [18.通用业务术语](#18.通用业务术语)
* [19.技术趋势](#19.技术趋势)
* [20.政策，法规](#20.政策，法规)
* [21.架构师素质](#21.架构师素质)
* [22.团队管理](#22.团队管理)
* [23.资讯](#23.资讯)
* [24.技术资源](#24.技术资源)

<!-- vim-markdown-toc -->

- [参考项目](https://github.com/xingshaocheng/architect-awesome)

## 1.数据结构

[数据结构笔记](../data_structure/data_structure.md)

- [x] 队列,(python列表)
- [x] 集合,(python集合)
- [x] 链表，数组, [python实现链表](../data_structure/link_list)
- [x] 字典，关联数组,(python字典)
- [x] 栈,[python实现栈](../data_structure/stack)
- [x] 树
  - [x] 二叉树,[python实现二叉树](../data_structure/binary_tree)
  - [ ] 完全二叉树
  - [ ] 平衡二叉树
  - [x] 红黑树,[python实现红黑树](../data_structure/binary_tree/red_black_tree.py)
  - [x] B，B+，B*树,[python实现b树](../data_structure/binary_tree/b_tree.py)
  - [ ] LSM树
- [ ] BitSet

## 2.常用算法

- [算法笔记](../algorithms/algorithms.md)

- [x] 排序查找算法
  - [ ] 选择排序
  - [x] 冒泡排序,[python实现冒泡排序](../algorithms/sort_algorithms/bubble_sort.py)
  - [ ] 插入排序
  - [x] 快速排序,[python实现快速排序](../algorithms/sort_algorithms/quick_sort.py)
  - [ ] 归并排序
  - [ ] 希尔排序
  - [ ] 堆排序
  - [ ] 计数排序
  - [ ] 桶排序
  - [ ] 基数排序
  - [x] 二分查找,[python实现二分查找](../algorithms/search_algorithms/binary_search.py)
  - [x] 斐波那契查找,[python实现斐波那契查找](../algorithms/search_algorithms/fibonacci_search.py)
  - [x] 哈希查找,[python实现哈希查找](../algorithms/search_algorithms/hash_search.py)
  - [x] 跳转查找,[python实现跳转查找](../algorithms/search_algorithms/jump_search.py)
  - [x] 差值搜索,[python实现差值搜索](../algorithms/search_algorithms/interpolation_search.py)
  - [x] 顺序查找,[python实现顺序查找](../algorithms/search_algorithms/sequential_search.py)
- [ ] 布隆过滤器
- [x] 字符串比较
  - [x] KMP算法,[python实现kmp算法]((../algorithms/search_algorithms/match_algorithms/kmp)
- [ ] 深度优先算法
- [ ] 广度优先算法
- [ ] 贪心算法
- [ ] 回溯算法
- [ ] 剪枝算法
- [ ] 动态规划
- [ ] 朴素贝叶斯
- [ ] 最小生成树算法
- [ ] 最短路径算法

## 3.并发

- [ ] 多线程
- [ ] 多进程
- [ ] 线程安全
- [ ] 一致性，事务
  - [ ] 事务ACID特性
  - [ ] 事务的隔离级别
  - [ ] MVCC
- [ ] 锁
  - [ ] 乐观锁&CAS
  - [ ] 悲观锁
  - [ ] 死锁
  - [ ] 互斥锁&共享锁
  - [ ] 公平锁&非公平锁
  - [ ] 可重入锁&不可重入锁

## 4.操作系统

- [ ] 计算机原理
- [ ] CPU
  - [ ] 多级缓存
- [ ] 进程
- [ ] 线程
- [ ] 协程
- [ ] Linux

## 5.设计模式

- [ ] 设计模式的六大原则
- [ ] 23种常见的设计模式
- [ ] 应用场景
- [ ] 单例模式
- [ ] 责任链模式
- [ ] MVC
- [ ] IOC
- [ ] AOP
- [ ] UML
- [ ] 微服务思想
  - [ ] 康威定律

## 6.运维&统计&技术支持

- [ ] 常规监控
- [ ] APM
- [ ] 统计分析
- [ ] 持续集成(CI/CD)
  - [ ] Jenkins
  - [ ] 环境分离
- [ ] 自动化运维
  - [ ] Ansible
  - [ ] puppet
  - [ ] chef
- [ ] 自动化测试
  - [ ] TDD
  - [ ] 单元测试
  - [ ] 压力测试
  - [ ] 全链路压测
  - [ ] A/B、灰度、蓝绿测试
- [ ] 虚拟化
  - [ ] KVM
  - [ ] Xen
  - [ ] OpenVZ
- [ ] 容器技术
  - [ ] Docker
- [ ] 云技术
  - [ ] OpenStack
- [ ] DevOps
- [ ] 文档管理

## 7.中间件

- [ ] Web Server
  - [ ] Nginx
  - [ ] OpenResty
  - [ ] Tengine
  - [ ] Apache
  - [ ] Tomcat
  - [ ] Jetty
- [ ] 缓存
  - [ ] 本地缓存
- [ ] 客户端缓存
- [ ] 服务器缓存
  - [ ] Web缓存
  - [ ] Memached
  - [ ] Redis
    - [ ] 架构
    - [ ] 回收策略
  - [ ] Tair
- [ ] 消息队列
  - [ ] 消息总线
  - [ ] 消息顺序
  - [ ] RabbitMQ
  - [ ] RocketMQ
  - [ ] ActiveMQ
  - [ ] Kafka
  - [ ] Redis消息推送
  - [ ] ZeroMQ
- [ ] 定时调度
  - [ ] 单机定时调度
  - [ ] 分布式定时调度
- [ ] RPC
  - [ ] Dubbo
  - [ ] Thrift
  - [ ] gRPC
- [ ] 数据库中间件
  - [ ] Sharding Jdbc
- [ ] 日志系统
  - [ ] 日志搜集
- [ ] 配置中心
- [ ] API网关

## 8.网络

- [ ] 协议
  - [ ] OSI模型
  - [ ] TCP/IP
  - [ ] HTTP
  - [ ] HTTP2.0
  - [ ] HTTPS
- [ ] 网络模型
  - [ ] Epoll
  - [ ] kqueue
- [ ] 连接和短连接
- [ ] 框架
- [ ] 零拷贝
- [ ] 序列化
  - [ ] Hessian
  - [ ] Protobuf

## 9.数据库

- [ ] 基础理论
  - [ ] 三大范式
- [ ] MySQL
  - [ ] 原理
  - [ ] InnoDB
  - [ ] 优化
  - [ ] 索引
    - [ ] 聚集索引&非聚集索引
    - [ ] 复合索引
    - [ ] 自适应哈希索引
  - [ ] explain
- NoSQL
  - MongoDB
  - Hbase

## 10.搜索引擎

- [ ] 搜索引擎原理
- [ ] Lucence
- [ ] Elasticsearch
- [ ] Solr
- [ ] sphinx

## 11.性能

- [ ] 性能优化评估方法
- [ ] 容量评估
- [ ] CDN网络
- [ ] 连接池
- [ ] 性能调优

## 12.大数据

- [ ] 流式计算
  - [ ] storm
  - [ ] Flink
  - [ ] Kafka Stream
  - [ ] 应用场景
- [ ] Hadloop
  - [ ] HDFS
  - [ ] MapReduce
  - [ ] Yarn
- [ ] Spark

## 13.安全

- [ ] Web安全
  - [ ] XSS
  - [ ] CSRF
  - [ ] SQL注入
  - [ ] Hash Docs
  - [ ] 脚本注入
  - [ ] 漏洞扫描工具
  - [ ] 验证码
- [ ] DDos防范
- [ ] 用户隐私保护
- [ ] 序列化漏洞
- [ ] 加密解密
  - [ ] 对称加解密
  - [ ] 哈希算法
  - [ ] 非对称加解密
- [ ] 服务器安全
- [ ] 数据安全
  - [ ] 数据备份
- [ ] 网络隔离
  - [ ] 内外网隔离
  - [ ] 登录跳板机
- [ ] 授权，认证
  - [ ] RBAC
  - [ ] OAuth2.0
  - [ ] 双因素认证(2FA)
  - [ ] 单点登录(SSO)

## 14.常用开源框架

- [ ] 开源框架
- [ ] 日志框架
  - [ ] Log4j, log4j2
  - [ ] Logback
- [ ] ORM
- [ ] 网络框架
- [ ] Web框架
- [ ] 工具框架

## 15.分布式设计

- [ ] 扩展性设计
- [ ] 稳定性&高可用
  - [ ] 硬件负载均衡
  - [ ] 软件负载均衡
  - [ ] 限流
  - [ ] 应用层跨灾
  - [ ] 跨机房容灾
  - [ ] 容灾演练流程
  - [ ] 平滑启动
- [ ] 数据库扩展
  - [ ] 读写分离模式
  - [ ] 分片模式
- [ ] 服务治理
  - [ ] 服务注册于发现
  - [ ] 服务路由控制
- [ ] 分布式一致
  - [ ] CPA与BASE理论
  - [ ] 分布式锁
  - [ ] 分布式一致性锁
    - [ ] PAXOS
    - [ ] Zab
    - [ ] Raft
    - [ ] Gossip
    - [ ] 两阶段提交，多阶段提交
  - [ ] 幂等
  - [ ] 分布式一致性方案
  - [ ] 分布式Leader节点选举
  - [ ] TCC柔性事务
- [ ] 分布式文件系统
- [ ] 唯一ID生成
- [ ] 一致性Hash算法

## 16.设计思想&开发模式

- [ ] DDD领域驱动设计
- [ ] Actor模式
- [ ] 响应式编程
- [ ] DODAF2.0
- [ ] Serverless
- [ ] Service Mesh

## 17.项目管理

- [ ] 架构评审
- [ ] 重构
- [ ] 代码规范
- [ ] 代码Review
- [ ] RUP
- [ ] 看板管理
- [ ] SCRUM
- [ ] 敏捷开发
- [ ] 极限编程
- [ ] 结对编程
- [ ] PDCA循环质量管理
- [ ] FMEA管理模式

## 18.通用业务术语

## 19.技术趋势

## 20.政策，法规

## 21.架构师素质

## 22.团队管理

## 23.资讯

- [ ] 行业资讯
- [ ] 公众号列表
- [ ] 博客
  - [ ] 团队列表
  - [ ] 个人列表
- [ ] 综合门户，社区
- [ ] 问答讨论类社区
- [ ] 行业数据分析
- [ ] 专项网站
- [ ] 其他类
- [ ] 推荐参考书
  - [ ] 在线电子书
  - [ ] 纸质书
    - [ ] 开发方面
    - [ ] 架构方面
    - [ ] 技术管理方面
    - [ ] 基础理论
    - [ ] 工具方面
    - [ ] 大数据方面

## 24.技术资源

- [ ] 开源资源
- [ ] 手册，文档，教程
- [ ] 在线课堂
- [ ] 会议，活动
- [ ] 常用App
- [ ] 找工作
- [ ] 工具
- [ ] 代码托管
- [ ] 综合云服务商
  - [ ] VPS
