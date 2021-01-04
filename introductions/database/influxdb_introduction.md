# influxdb时序数据库介绍

<!-- vim-markdown-toc Marked -->

* [1.概述](#1.概述)
* [2.基础命令](#2.基础命令)

<!-- vim-markdown-toc -->

时序数据库，Time Series Database，最大的特点就是每个条数据都带有Time列。

## 1.概述

1. 支持类似SQL的查询语法
2. 提供了Http Api直接访问
3. 存储超过10亿级别的时间序列数据
4. 灵活的数据保留策略，可以定义到Database级别（只保留最热的数据）
5. 内置管理接口和CMD
6. 飞一般速度的聚合查询
7. 按不同时间段进行聚合查询
8. 内置持续查询功能，定时计算指定时间段的数据，插入到指定表中，可以理解为定时归集数据
9. 水平扩展，支持集群模式

- [基础概念介绍](https://www.cnblogs.com/zouhao/p/9862229.html)
- database：数据库
- measurement：数据库中的表
- point：表里面的一行数据
  time: 每个数据记录时间，数据库中的主索引
  fields: 各种记录值（没有索引的属性）也就是记录的值：温度， 湿度
  tags: 各种有索引的属性：地区，海拔

InfluxDB提供三种操作方式：

1. 客户端命令行方式
2. HTTP API接口
3. 各语言API库

## 2.基础命令

```sh
# 查看所有的数据库
show databases

# 使用某个数据库
use database1

# 查看某个“表”的所有数据
show series from measurement1

# 查看所有的“表”
show measurements
```
