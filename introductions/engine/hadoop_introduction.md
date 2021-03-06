# 分布式系统之Hadoop

<!-- vim-markdown-toc Marked -->

* [1.概述](#1.概述)
    - [1.1几种计算的区别](#1.1几种计算的区别)
    - [1.2master-slave结构](#1.2master-slave结构)

<!-- vim-markdown-toc -->

## 1.概述

- 它允许在整个集群`使用简单编程模型计算机的分布式环境存储并处理大数据`
- 目的是从单一的服务器到上千台机器的扩展，每一个台机都可以提供本地计算和存储
- 使用`MapReduce算法`运行，其中数据在使用其他并行处理的应用程序
- Hadoop用于开发可以执行完整的统计分析大数据的应用程序, 广泛应用于`大数据`
- Hadoop生态：Hadoop，Zookeeper(分布式协同系统)，Hbase(面向键/值的列存储数据库)

架构：

1. 底层——存储层，文件系统HDFS
2. 中间层——资源及数据管理层，YARN以及Sentry等
3. 上层——MapReduce、Impala、Spark等计算引擎
4. 顶层——基于MapReduce、Spark等计算引擎的高级封装及工具，如Hive、Pig、Mahout等等

### 1.1几种计算的区别

- 分布式计算
  大的计算问题分成小问题至多个计算机计算，结果再结合起来。
- 云计算
  分布式技术+服务化技术+资源隔离技术+管理技术(虚拟化)
- 并行计算
  同时使用多种计算资源解决同一个问题，区分于串行计算。

### 1.2master-slave结构

一台计算机作为主调度者，其他的计算机根据调度完成任务。
slave和master之间通过`心跳`来保持通信，实际上类似于一台计算机之间的多线程。

缺陷：master和slave之间的耦合性太强，如果master出问题，整个系统就崩溃了

