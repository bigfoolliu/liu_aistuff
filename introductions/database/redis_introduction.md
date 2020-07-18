# redis数据库

<!-- vim-markdown-toc Marked -->

- [redis数据库](#redis数据库)
  - [1.概述](#1概述)
    - [1.1介绍](#11介绍)
    - [1.2安装启动](#12安装启动)
    - [1.3数据库操作常用命令](#13数据库操作常用命令)
  - [2.五大数据类型](#2五大数据类型)
    - [2.1字符串(string)](#21字符串string)
    - [2.2哈希(Hash)](#22哈希hash)
    - [2.3列表(List)](#23列表list)
    - [2.4集合(Set)](#24集合set)
    - [2.5有序集合(Sorted List)](#25有序集合sorted-list)
  - [3.使用场景](#3使用场景)
    - [3.1计数器](#31计数器)
    - [3.2缓存](#32缓存)
    - [3.3查找表](#33查找表)
    - [3.4消息队列](#34消息队列)
    - [3.5会话缓存](#35会话缓存)
    - [3.6分布式锁](#36分布式锁)
    - [3.7其他](#37其他)
  - [4.事务](#4事务)
    - [4.1事务基础](#41事务基础)
    - [4.2redis事务机制命令](#42redis事务机制命令)
  - [5.持久化](#5持久化)
    - [5.1RDB](#51rdb)
    - [5.2AOF](#52aof)
    - [5.3虚拟内存方式](#53虚拟内存方式)
  - [6.数据回收](#6数据回收)
    - [6.1数据淘汰(回收)策略](#61数据淘汰回收策略)
    - [6.2回收进程工作](#62回收进程工作)
  - [7.redis集群](#7redis集群)
    - [7.1集群方案](#71集群方案)
    - [7.2导致集群方案不可用的情况](#72导致集群方案不可用的情况)
    - [7.3redis哈希槽](#73redis哈希槽)
  - [a.其他](#a其他)
    - [a.1客户端连接](#a1客户端连接)
    - [a.2安全](#a2安全)
    - [a.3性能测试](#a3性能测试)
    - [a.4发布-订阅](#a4发布-订阅)
    - [a.5面试](#a5面试)
    - [a.6内存优化](#a6内存优化)

<!-- vim-markdown-toc -->

## 1.概述

- [github中redis知识点](https://github.com/CyC2018/CS-Notes/blob/master/notes/Redis.md)
- [redis中文网以及教程](https://www.redis.net.cn/tutorial/3501.html)

### 1.1介绍

- 全称：`Remote Dictionary Server`
- `纯内存的key-value数据库`，整个数据库加载到内存中，性能极高，通过`异步定期将数据持久化到硬盘`
- 支持多种数据类型，且最大的value值为GB级别，因此可以实现多种功能(如：list实现消息队列，set实现标签系统)
- `数据库容量受物理内存限制`，适合较小数量的高性能操作和运算
- 单机的支持并发量可能支持10几万
- **redis的命令不区分大小写**

### 1.2安装启动

```sh
sudo apt-get install redis-server  # 安装
vim /etc/redis/redis.conf  # 可以配置redis的绑定ip为0.0.0.0

sudo service redis-server restart  # 启动redis

redis-server  # 进入redis服务端
redis-cli  # 进入redis客户端，输入ping来判断是否可以连接
redis-cli -h <host> -p <port> -a <password>  # 在远程的服务器上执行
```

### 1.3数据库操作常用命令

- [redis命令参考](http://redisdoc.com/)

```sh
# 数据库的操作
select 1  # 切换到不同的数据库，默认为0，共16个
dbsize  # 查看当前数据库的key的数量

flushdb  # 清空当前数据库的所有key
flushall  # 清空整个redis服务器的数据(所有数据库的所有key)

swapdb 0 1  # 对换0,1两个数据库

info  # 查看redis服务器的信息,进入redis-cli之后


# key的操作
keys *  # 查看所有的key
del key  # 删除键
exists key  # 判断给定的key是否存在

dump key  # 序列化给定key，并返回序列化的值
restore key 0 "\x00\x15hello, dumping world!\x06\x00E\xa0Z\x82\xd8r\xc1\xde"  # 将序列化的值反序列化,0为ttl的时间

expire key 10  # 给key设置过期时间为10秒
ttl key  # 查看key的剩余生存时间(s)
persist key  # 将一个带有过期的key设置为永久的不过期的key

move key 1  # 将key移动到新的数据库1
type key  # 查看key所存储的值的类型
rename key <new_key>  # 修改key的名称


# 调试
ping  # 客户端向服务器发送查看服务器是否正常
```

## 2.五大数据类型

### 2.1字符串(string)

- 最基本的数据类型
- 二级制安全，即string可以包含任何数据，如jpg图片或者序列化的对象
- `一个键最多存储512MB`

```sh
set name "tony"  # 设置键值
get name  # 取值
```

### 2.2哈希(Hash)

- 一个键值对集合
- 适合存储对象
- 每个hash可以存储$2^{32 - 1}$（40多亿）键值对

```sh
hmset user:1 name tony pwd 123456  # 设置hash键值对
hgetall user:1  # 取得hash键值对
```

### 2.3列表(List)

- 简单的字符串列表
- 每个列表最多可以存储$2^{32-1}$键值对

```sh
# 添加一个元素到列表的头部
lpush names tony
lpush names tom

lrange names 0 10  # 获取列表的内容
```

### 2.4集合(Set)

- string的无序集合
- 通过哈希表实现
- 每个集合最多可以存储$2^{32-1}$成员

```sh
# 添加一个string元素到key对应的set集合中，成功返回1
# 再次添加相同的元素会因为唯一性被忽略,返回0
sadd names tony

# 获取集合中的元素
smembers names
```

### 2.5有序集合(Sorted List)

- 类似集合，不同的是每个元素都会关联一个double类型的分数，通过该分数对成员进行从小到大的排列
- 成员唯一，但是分数却可以重复

```sh
# 添加元素到有序集合
zadd names 0 tony
zadd names 10 jim

zrangebyscore names 0 100  # 取有序集合中的元素
```

## 3.使用场景

### 3.1计数器

- 对String进行自增或者自减实现计数

### 3.2缓存

- 将热点数据放到内存中,设置内存的最大使用量以及淘汰策略来保证缓存的命中率
- ![redis使用缓存的模板](./imgs/redis_cache_template.png)

### 3.3查找表

- DNS记录适宜使用redis存储

### 3.4消息队列

- List是双向链表，可以通过lpush和rpop写入和读取消息
- 最好还是使用RabbitMQ等消息中间件比较好

### 3.5会话缓存

- [Django获取用户浏览历史，使用redis缓存](https://www.cnblogs.com/mxsf/p/10297271.html)
- [使用redis存储用户浏览记录](https://blog.csdn.net/weixin_44313745/article/details/95754500)
- 存储多台服务器的会话

### 3.6分布式锁

**分布式锁介绍：**

在分布式的环境下，保证一个方法或属性在高并发的情况之下同一时间只能被同一个线程使用。用来解决跨机器的互斥机制来控制共享资源的访问。

1. 分布式系统环境下，一个方法在同一时间只能被一个机器的一个线程使用
2. 高可用的获取锁和释放锁
3. 高性能的获取锁和释放锁
4. 具备可重入特性
5. 具备锁失效机制，防止死锁
6. 具备非阻塞特性，即没有获取到锁将直接返回获取锁失败

**使用redis实现分布式锁：**

- 可以使用Redis的`SETNX`命令实现分布式锁
- 也可以使用官方的RedLock分布式锁实现
- [python-redis分布式锁的简单实现](../../python/modules/redis/redis_lock/redis_lock.py)

### 3.7其他

- Set可以实现交集，并集等操作，实现共同好友功能
- ZSet可以实现有序性操作，实现排行榜功能

## 4.事务

### 4.1事务基础

- 一次执行`多个命令`
- `事务是一个单独的隔离操作`：事务中的所有命令都会序列化，按顺序的执行,事务执行的过程中不会被其他命令打断
- 事务是`原子操作`，要么全部执行，要么全部不执行

### 4.2redis事务机制命令

- `MULTI`
- `EXEC`
- `DISCARD`
- `WATCH`

```sh
# 开始事务。
# 命令入队。
# 执行事务。

# 一下为一个事务的全过程

multi
set name tony
get name tony
exec
```

## 5.持久化

即`数据备份和恢复`

- [redis持久化之RDB和AOF](https://www.cnblogs.com/itdragon/p/7906481.html)

### 5.1RDB

1. 缺省情况下redis将数据快照存放在磁盘的二进制文件上中（dump.rdb）
2. 可以配置其持久化策略定期或者超过M次更新时将数据写入磁盘，或者`手动调用SAVE或者BGSAVE`
3. 适合大规模数据恢复，`对数据的完整性和一致性要求不高的场景`，当系统停止或者redis被杀死数据就会丢失

### 5.2AOF

1. 采用日志的方式记录每一个写操作，并追加到文件
2. redis重启会根据日志文件的内容将`写指令从前至后执行一次`以完成数据的恢复工作
3. `数据的完整性和一致性更高`，但是记录的内容多，文件越来越大，数据恢复也会越来越慢

### 5.3虚拟内存方式

1. 当key很小而value很大时，使用效果会很好

```sh
# 创建当前数据库的备份，会在安装的目录创建dump.rdb文件
# 在生产环境很少执行 SAVE 操作，因为它会阻塞所有客户端，保存数据库的任务通常由 BGSAVE 命令异步地执行
save

# 恢复数据，只需要将备份文件`dump.rdb`移动到redis的安装目录

config get dir  # 查看备份文件的位置
bgsave  # 在后台异步的保存数据库
lastsave  # 返回最近一次Redis成功将数据保存到磁盘的时间，Unix时间戳形式
```

## 6.数据回收

### 6.1数据淘汰(回收)策略

- [redis数据淘汰策略](https://www.cnblogs.com/mysql-hang/articles/10532720.html)
- [redis数据淘汰策略及其相关注意事项](https://blog.csdn.net/qq_22860341/article/details/80681373)
- 比如保证`数据都是热点数据`

1. allkeys-lru, 尝试回收使用最少的键
2. allkeys-random, 回收随机的键
3. volatile-lru,尝试回收使用最少的键，但仅限于已经过期的
4. volatile-random, 回收随机的键，仅限于已经过期的
5. volatile-ttl, 回收过期的键，优先回收存活时间短的键
6. no-enviction, 驱逐，禁止驱逐数据

### 6.2回收进程工作

- 内存使用达到`maxmemory`后，使用设置的策略回收
- 删除过期时间的键对象(惰性删除-用户访问的时候删除，定时任务删除)

## 7.redis集群

### 7.1集群方案

- [redis模式集群原理与搭建](https://www.jianshu.com/p/84dbb25cc8dc)
- [redis集群详细搭建过程](https://blog.csdn.net/qq_42815754/article/details/82912130)

1. **Codis**，使用最多，分布式算法是`一致性hash`，支持在节点数量变化的情况下，将旧节点的数据恢复到新节点上
2. **redis cluster3.0**，分布式算法是`hash槽`，自身节点支持设置从节点
3. **业务层面**，起几个无关联的redis实例，对不同的key进行hash计算，去对应的redis实例操作，对hash层代码要求较高

### 7.2导致集群方案不可用的情况

- 若有A B C三个节点，但是没有复制模型的情况下，B失效，会导致集群缺失一部分数据。

### 7.3redis哈希槽

- [redis一致性hash与hash槽](https://www.jianshu.com/p/6ad87a1f070e)

**一致性hash对于容错性和扩展性比较好，但是容易出现数据倾斜，对数据控制，节点位置控制不友好。**

redis哈希槽(`hash算法+槽位`)，使用的hash算法是`crc16校验算法`，槽位的概念则是对于空间分配的规则。

- redis哈希槽包含16384个槽位
- 每个key计算后落到一个槽位
- 槽位由用户分配，内存大的可以分配多个槽位

## a.其他

### a.1客户端连接

```sh
config get maxclients  # 获取最大连接数量
redis-server --maxclients 10000  # 服务端启动时候设置最大连接数
```

### a.2安全

设置密码，客户端连接的时候就需要验证。

```sh
config get requirepass  # 查看是否设置了密码
config set requirepass "123456"  # 设置密码

config get requirepass  # 获取密码
auth 123456  # 验证密码
```

### a.3性能测试

```sh
redis-benchmark -n 1000  # 模拟同时执行1000个请求来检测性能
```

### a.4发布-订阅

发布-订阅(pub/sub)是一种消息通信模式。

```sh
subscribe channel1  # 在客户端1订阅channel1频道的消息
psubscribe news.*channel  # 订阅多个符合条件的频道

unsubscribe  # 退订频道

publish channel1 hello  # 在客户端2发送消息到channel1,返回结果会显示订阅该频道的数量

pubsub channels  # 查看当前的活跃频道(即至少有一个订阅者的频道)
```

### a.5面试

- [redis面试三十问](http://blog.itpub.net/31545684/viewspace-2213990/)
- [漫画:redis面试常见问题1](https://mp.weixin.qq.com/s?__biz=MzI4Njc5NjM1NQ==&mid=2247486641&idx=2&sn=16594b5394e52a5b0884156c271e58cf&chksm=ebd6339ddca1ba8b85df41d508434c2e727ed31736cc353d376e200e62932180f978d7f763a9&scene=21#wechat_redirect)
- [漫画:redis面试常见问题1](https://mp.weixin.qq.com/s?__biz=MzI4Njc5NjM1NQ==&mid=2247486734&idx=2&sn=7ebb4e8d86ddae67522244c8e8584ef0&chksm=ebd63222dca1bb34515cfadd321e3d82bcbeb6210812af087ae254181067cc45cb5f740602b4&scene=21#wechat_redirect)

### a.6内存优化

- 尽量使用散列表(hashes),将数据模型抽象到一个散列表格中，如将人的姓名，邮箱，年龄等存储到一张表。
