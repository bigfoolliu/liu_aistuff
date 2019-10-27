# redis面试

<!-- TOC -->

- [redis面试](#redis%e9%9d%a2%e8%af%95)
  - [1.redis基础](#1redis%e5%9f%ba%e7%a1%80)
    - [1.1介绍一下redis](#11%e4%bb%8b%e7%bb%8d%e4%b8%80%e4%b8%8bredis)
  - [2.数据](#2%e6%95%b0%e6%8d%ae)
    - [2.1支持的数据类型及其特点](#21%e6%94%af%e6%8c%81%e7%9a%84%e6%95%b0%e6%8d%ae%e7%b1%bb%e5%9e%8b%e5%8f%8a%e5%85%b6%e7%89%b9%e7%82%b9)
    - [2.2数据淘汰策略](#22%e6%95%b0%e6%8d%ae%e6%b7%98%e6%b1%b0%e7%ad%96%e7%95%a5)
  - [redis集群](#redis%e9%9b%86%e7%be%a4)

<!-- /TOC -->

- [redis面试三十问](http://blog.itpub.net/31545684/viewspace-2213990/)

## 1.redis基础

- [redis基础](../introductions/db/redis_introduction.md)

### 1.1介绍一下redis

`Remote Dictionary Server`

- 纯内存的key-value数据库，整个数据库加载到内存中，性能极高，通过异步定期将数据持久化到硬盘
- 支持多种数据类型，且最大的value值为GB级别，因此可以实现多种功能
- 数据库容量受物理内存限制，适合较小数量的高性能操作和运算

## 2.数据

### 2.1支持的数据类型及其特点

`string, list, set, sorted set, hash`

### 2.2数据淘汰策略

- [redis数据淘汰策略](https://www.cnblogs.com/mysql-hang/articles/10532720.html)
- [redis数据淘汰策略及其相关注意事项](https://blog.csdn.net/qq_22860341/article/details/80681373)

1. allkeys-lru, 尝试回收使用最少的键
2. allkeys-random, 回收随机的键
3. volatile-lru,尝试回收使用最少的键，但仅限于已经过期的
4. volatile-random, 回收随机的键，仅限于已经过期的
5. volatile-ttl, 回收过期的键，优先回收存活时间短的键

## redis集群
