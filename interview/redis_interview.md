# redis面试

<!-- TOC -->

- [redis面试](#redis面试)
    - [1.redis基础](#1redis基础)
        - [1.1介绍一下redis](#11介绍一下redis)
    - [2.数据](#2数据)
        - [2.1支持的数据类型及其特点](#21支持的数据类型及其特点)
        - [2.2数据淘汰(回收)策略](#22数据淘汰回收策略)
        - [2.3Key的过期时间和永久有效设置](#23key的过期时间和永久有效设置)
        - [2.4回收进程如何工作](#24回收进程如何工作)
    - [3.redis集群](#3redis集群)
        - [3.1集群方案](#31集群方案)
        - [3.2导致集群方案不可用的情况](#32导致集群方案不可用的情况)
        - [3.3redis哈希槽](#33redis哈希槽)
    - [4.redis使用场景](#4redis使用场景)
        - [4.1会话缓存](#41会话缓存)
        - [4.2全页缓存](#42全页缓存)
        - [4.3排行榜/计数器](#43排行榜计数器)
        - [4.4队列](#44队列)
        - [4.5发布/订阅](#45发布订阅)
    - [5.redis事务](#5redis事务)
        - [5.1事务相关命令](#51事务相关命令)
    - [6.内存优化](#6内存优化)

<!-- /TOC -->

- [redis面试三十问](http://blog.itpub.net/31545684/viewspace-2213990/)
- [漫画:redis面试常见问题1](https://mp.weixin.qq.com/s?__biz=MzI4Njc5NjM1NQ==&mid=2247486641&idx=2&sn=16594b5394e52a5b0884156c271e58cf&chksm=ebd6339ddca1ba8b85df41d508434c2e727ed31736cc353d376e200e62932180f978d7f763a9&scene=21#wechat_redirect)
- [漫画:redis面试常见问题1](https://mp.weixin.qq.com/s?__biz=MzI4Njc5NjM1NQ==&mid=2247486734&idx=2&sn=7ebb4e8d86ddae67522244c8e8584ef0&chksm=ebd63222dca1bb34515cfadd321e3d82bcbeb6210812af087ae254181067cc45cb5f740602b4&scene=21#wechat_redirect)

## 1.redis基础

- [redis基础](../introductions/db/redis_introduction.md)

### 1.1介绍一下redis

`Remote Dictionary Server`

- `纯内存的key-value数据库`，整个数据库加载到内存中，性能极高，通过`异步定期将数据持久化到硬盘`
- 支持多种数据类型，且最大的value值为GB级别，因此可以实现多种功能(如：list实现消息队列，set实现标签系统)
- `数据库容量受物理内存限制`，适合较小数量的高性能操作和运算

## 2.数据

### 2.1支持的数据类型及其特点

`string, list, set, sorted set, hash`

### 2.2数据淘汰(回收)策略

- [redis数据淘汰策略](https://www.cnblogs.com/mysql-hang/articles/10532720.html)
- [redis数据淘汰策略及其相关注意事项](https://blog.csdn.net/qq_22860341/article/details/80681373)
- 比如保证`数据都是热点数据`

1. allkeys-lru, 尝试回收使用最少的键
2. allkeys-random, 回收随机的键
3. volatile-lru,尝试回收使用最少的键，但仅限于已经过期的
4. volatile-random, 回收随机的键，仅限于已经过期的
5. volatile-ttl, 回收过期的键，优先回收存活时间短的键
6. no-enviction, 驱逐，禁止驱逐数据

### 2.3Key的过期时间和永久有效设置

`expire`设置过期时间；`persist`设置永久有效

### 2.4回收进程如何工作

执行命令之后，redis检查内存使用`是否超过maxmemory`，超过了则使用既定的回收策略回收。

## 3.redis集群

### 3.1集群方案

- [redis模式集群原理与搭建](https://www.jianshu.com/p/84dbb25cc8dc)
- [redis集群详细搭建过程](https://blog.csdn.net/qq_42815754/article/details/82912130)

1. **Codis**，使用最多，分布式算法是`一致性hash`，支持在节点数量变化的情况下，将旧节点的数据恢复到新节点上
2. **redis cluster3.0**，分布式算法是`hash槽`，自身节点支持设置从节点
3. **业务层面**，起几个无关联的redis实例，对不同的key进行hash计算，去对应的redis实例操作，对hash层代码要求较高

### 3.2导致集群方案不可用的情况

若有A B C三个节点，但是没有复制模型的情况下，B失效，会导致集群缺失一部分数据。

### 3.3redis哈希槽

- [redis一致性hash与hash槽](https://www.jianshu.com/p/6ad87a1f070e)

**一致性hash对于容错性和扩展性比较好，但是容易出现数据倾斜，对数据控制，节点位置控制不友好。**

redis哈希槽(`hash算法+槽位`)，使用的hash算法是`crc16校验算法`，槽位的概念则是对于空间分配的规则。

- redis哈希槽包含16384个槽位
- 每个key计算后落到一个槽位
- 槽位由用户分配，内存大的可以分配多个槽位

## 4.redis使用场景

### 4.1会话缓存

- [Django获取用户浏览历史，使用redis缓存](https://www.cnblogs.com/mxsf/p/10297271.html)
- [使用redis存储用户浏览记录](https://blog.csdn.net/weixin_44313745/article/details/95754500)

将用户的`会话缓存`，其相对的优势在于可以将会话缓存的数据持久化。

### 4.2全页缓存

将全页(如网站首页)缓存。

### 4.3排行榜/计数器

### 4.4队列

其list和set的数据类型使redis可以作为一个`消息队列`使用。

### 4.5发布/订阅

## 5.redis事务

### 5.1事务相关命令

`multi, exec, discard, watch`

## 6.内存优化

尽量使用散列表(hashes),将数据模型抽象到一个散列表格中，如将人的姓名，邮箱，年龄等存储到一张表。
