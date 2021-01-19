# elastic search 全文搜索引擎

<!-- vim-markdown-toc Marked -->

* [1.概述](#1.概述)
    - [1.1全文搜索引擎介绍](#1.1全文搜索引擎介绍)
    - [1.2使用场景](#1.2使用场景)
    - [1.3特点](#1.3特点)
* [2.安装使用](#2.安装使用)
    - [2.1mac安装](#2.1mac安装)
* [3.基本概念](#3.基本概念)
    - [3.1索引(index)](#3.1索引(index))
    - [3.2类型(type)](#3.2类型(type))
    - [3.3字段(field)](#3.3字段(field))
    - [3.4映射(mapping)](#3.4映射(mapping))
    - [3.5文档(document)](#3.5文档(document))
    - [3.6集群(cluster)](#3.6集群(cluster))
    - [3.7节点(node)](#3.7节点(node))
    - [3.8分片和复制(shards&replicas)](#3.8分片和复制(shards&replicas))

<!-- vim-markdown-toc -->

## 1.概述

- [elasticsearch项目地址](https://github.com/elastic/elasticsearch)
- [elasticsearch权威指南](https://es.xiaoleilu.com/)
- [保姆级教程](https://www.cnblogs.com/coderxz/p/13268417.html)

### 1.1全文搜索引擎介绍

- 计算机索引程序扫描文章中的每一个词，为每一个词建立索引，便于之后的查询
- 支持`非结构化的数据的搜索`，更好的搜索存在的任何单词或单词组的非结构化的文本, 传统的数据库的全文检索实现比较鸡肋

### 1.2使用场景

1. 搜索的对象是大量的非结构化的文本数据
2. 文件数量记录众多，百万级甚至更多
3. 支持大量的基于交互式文本的查询
4. 需求灵活的全文搜索查询
5. 高度相关的搜索结果有特殊需求
6. 对不同记录类型，非文本数据操作或安全事务处理的需求较少

### 1.3特点

- `分布式实时文件存储`，每个字段都被索引并可被搜索
- 分布式的实时分析搜索引擎
- 可扩展，处理`PB级别`的结构化或者非结构化的数据

## 2.安装使用

### 2.1mac安装

```sh
# ma安装
brew install elasticsearch

# 通过安装head插件来实现图形化效果
# 1.下载head插件：https://github.com/mobz/elasticsearch-head
# 2.解压文件
# 3.安装grunt构建工具
cnpm install grunt-cli

# 4.进入head插件目录安装依赖
npm install
# 5.启动
grunt server
```


## 3.基本概念

### 3.1索引(index)

### 3.2类型(type)

### 3.3字段(field)

### 3.4映射(mapping)

### 3.5文档(document)

### 3.6集群(cluster)

### 3.7节点(node)

### 3.8分片和复制(shards&replicas)

