# elastic search 全文搜索引擎

<!-- TOC -->

- [elastic search 全文搜索引擎](#elastic-search-%e5%85%a8%e6%96%87%e6%90%9c%e7%b4%a2%e5%bc%95%e6%93%8e)
  - [elasticsearch项目以及介绍](#elasticsearch%e9%a1%b9%e7%9b%ae%e4%bb%a5%e5%8f%8a%e4%bb%8b%e7%bb%8d)
    - [全文搜索引擎介绍](#%e5%85%a8%e6%96%87%e6%90%9c%e7%b4%a2%e5%bc%95%e6%93%8e%e4%bb%8b%e7%bb%8d)
    - [elasticsearch介绍](#elasticsearch%e4%bb%8b%e7%bb%8d)

<!-- /TOC -->

## elasticsearch项目以及介绍

- [elasticsearch项目地址](https://github.com/elastic/elasticsearch)
- [elasticsearch权威指南](https://es.xiaoleilu.com/)

### 全文搜索引擎介绍

计算机索引程序扫描文章中的每一个词，为每一个词建立索引，便于之后的查询。

**使用原因**：

1. 支持非结构化的数据的搜索，更好的搜索存在的任何单词或单词组的非结构化的文本
2. 传统的数据库的全文检索实现比较鸡肋

**使用场景**：

1. 搜索的对象是大量的非结构化的文本数据
2. 文件数量记录众多，百万级甚至更多
3. 支持大量的基于交互式文本的查询
4. 需求灵活的全文搜索查询
5. 高度相关的搜索结果有特殊需求
6. 对不同记录类型，非文本数据操作或安全事务处理的需求较少

### elasticsearch介绍

- 分布式实时文件存储，每个字段都被索引并可被搜索
- 分布式的实时分析搜索引擎
- 可扩展，处理PB级别的机构化或者非结构化的数据
