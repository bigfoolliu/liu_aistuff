# redis数据库

<!-- TOC -->

- [redis数据库](#redis%e6%95%b0%e6%8d%ae%e5%ba%93)
  - [1.安装使用](#1%e5%ae%89%e8%a3%85%e4%bd%bf%e7%94%a8)
  - [2.五大数据类型](#2%e4%ba%94%e5%a4%a7%e6%95%b0%e6%8d%ae%e7%b1%bb%e5%9e%8b)
    - [2.1字符串(string)](#21%e5%ad%97%e7%ac%a6%e4%b8%b2string)
    - [2.2哈希(Hash)](#22%e5%93%88%e5%b8%8chash)
    - [2.3列表(List)](#23%e5%88%97%e8%a1%a8list)
    - [2.4集合(Set)](#24%e9%9b%86%e5%90%88set)
    - [2.5有序集合(Sorted List)](#25%e6%9c%89%e5%ba%8f%e9%9b%86%e5%90%88sorted-list)
  - [3.常用命令](#3%e5%b8%b8%e7%94%a8%e5%91%bd%e4%bb%a4)
  - [4.发布-订阅](#4%e5%8f%91%e5%b8%83-%e8%ae%a2%e9%98%85)
  - [5.redis事务](#5redis%e4%ba%8b%e5%8a%a1)
  - [6.数据备份和恢复](#6%e6%95%b0%e6%8d%ae%e5%a4%87%e4%bb%bd%e5%92%8c%e6%81%a2%e5%a4%8d)
  - [7.redis安全](#7redis%e5%ae%89%e5%85%a8)
  - [7.redis性能测试](#7redis%e6%80%a7%e8%83%bd%e6%b5%8b%e8%af%95)
  - [8.redis客户端连接](#8redis%e5%ae%a2%e6%88%b7%e7%ab%af%e8%bf%9e%e6%8e%a5)
  - [9.redis管道](#9redis%e7%ae%a1%e9%81%93)
  - [10.redis分区](#10redis%e5%88%86%e5%8c%ba)
  - [11.应用场景](#11%e5%ba%94%e7%94%a8%e5%9c%ba%e6%99%af)
    - [11.1缓存数据](#111%e7%bc%93%e5%ad%98%e6%95%b0%e6%8d%ae)
    - [11.2消息队列](#112%e6%b6%88%e6%81%af%e9%98%9f%e5%88%97)
    - [11.3计数器](#113%e8%ae%a1%e6%95%b0%e5%99%a8)
    - [11.4电商网站信息](#114%e7%94%b5%e5%95%86%e7%bd%91%e7%ab%99%e4%bf%a1%e6%81%af)
    - [11.5热点数据](#115%e7%83%ad%e7%82%b9%e6%95%b0%e6%8d%ae)

<!-- /TOC -->

## 1.安装使用

- [redis中文网以及教程](https://www.redis.net.cn/tutorial/3501.html)
- [redis配置详解](https://www.redis.net.cn/tutorial/3504.html)

```shell
# 安装
sudo apt-get install redis-server

# 可以配置redis的绑定ip为0.0.0.0
vim /etc/redis/redis.conf

# 启动redis
sudo service redis-server restart

# 进入redis服务端
redis-server

# 进入redis客户端，输入ping来判断是否可以连接
redis-cli

# 在远程的服务器上执行 
redis-cli -h host -p port -a password
```

## 2.五大数据类型

redis的命令不区分大小写。

### 2.1字符串(string)

- 最基本的数据类型
- 二级制安全，即string可以包含任何数据，如jpg图片或者序列化的对象
- `一个键最多存储512MB`

```shell
# 设置键值
set name "tony"

# 取值
get name
```

### 2.2哈希(Hash)

- 一个键值对集合
- 适合存储对象
- 每个hash可以存储$2^{32 - 1}$（40多亿）键值对

```shell
# 设置hash键值对
hmset user:1 name tony pwd 123456

# 取得hash键值对
hgetall user:1
```

### 2.3列表(List)

- 简单的字符串列表
- 每个列表最多可以存储$2^{32-1}$键值对

```shell
# 添加一个元素到列表的头部
lpush names tony
lpush names tom

# 获取列表的内容
lrange names 0 10
```

### 2.4集合(Set)

- string的无序集合
- 通过哈希表实现
- 每个集合最多可以存储$2^{32-1}$成员

```shell
# 添加一个string元素到key对应的set集合中，成功返回1
# 再次添加相同的元素会因为唯一性被忽略,返回0
sadd names tony

# 获取集合中的元素
smembers names
```

### 2.5有序集合(Sorted List)

- 类似集合，不同的是每个元素都会关联一个double类型的分数，通过该分数对成员进行从小到大的排列
- 成员唯一，但是分数却可以重复

```shell
# 添加元素到有序集合
zadd names 0 tony
zadd names 10 jim

# 取有序集合中的元素
zrangebyscore names 0 100
```

## 3.常用命令

```shell
# 删除键
del key

# 序列化给定key，并返回序列化的值
dump key

# 判断给定的key是否存在
exists key

# 给key设置过期时间（s）
expire key

# 将key移动到新的数据库db
move key db

# 查看key所存储的值的类型
type key

# 修改key的名称
rename key newkey

# 查看redis服务器的信息
info
```

## 4.发布-订阅

发布-订阅(pub/sub)是一种消息通信模式。

```shell
# 在客户端1订阅channel1频道的消息
subscribe channel1

# 在客户端2发送消息到channel1
publish channel1 hello
```

## 5.redis事务

- 一次执行多个命令
- 事务是一个单独的隔离操作：事务中的所有命令都会序列化，按顺序的执行,事务执行的过程中不会被其他命令打断
- 事务是原子操作，要么全部执行，要么全部不执行

```shell
# 开始事务。
# 命令入队。
# 执行事务。

# 一下为一个事务的全过程

multi
set name tony
get name tony
exec
```

## 6.数据备份和恢复

```shell
# 创建当前数据库的备份，会在安装的目录创建dump.rdb文件
save

# 恢复数据，只需要将备份文件`dump.rdb`移动到redis的安装目录

# 查看备份文件的位置
config get dir
```

## 7.redis安全

设置密码，客户端连接的时候就需要验证。

```shell
# 查看是否设置了密码
config get requirepass

# 设置密码
config set requirepass "123456"

# 获取密码
config get requirepass

# 验证密码
auth 123456
```

## 7.redis性能测试

```shell
# 模拟同时执行1000个请求来检测性能
redis-benchmark -n 1000
```

## 8.redis客户端连接

```shell
# 获取最大连接数量
config get maxclients

# 服务端启动时候设置最大连接数
redis-server --maxclients 10000
```

## 9.redis管道

TODO:

## 10.redis分区

- 分割数据到多个redis实例，每个实例保存key的一个子集

## 11.应用场景

### 11.1缓存数据

### 11.2消息队列

### 11.3计数器

### 11.4电商网站信息

### 11.5热点数据
