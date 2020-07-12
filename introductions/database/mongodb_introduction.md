# mongo db介绍以及使用

<!-- vim-markdown-toc Marked -->

* [1. 介绍](#1.-介绍)
        * [1.1特点](#1.1特点)
        * [1.2优点](#1.2优点)
        * [1.3使用场景](#1.3使用场景)
* [2.常用命令](#2.常用命令)

<!-- vim-markdown-toc -->

## 1. 介绍

### 1.1特点

- 文档型数据库
- 非关系型数据库(NoSQL)
- 不支持事务和锁

### 1.2优点

- 面向文档存储，能够更便捷的获取数
- 高性能，高可用，易扩展
- 对数据存储友好

### 1.3使用场景

- `处理非结构化/半结构化的大数据`时
- 在水平方向上进行扩展时
- 随时应对动态增加的数据项时可以优先考虑使用NoSQL数据库

## 2.常用命令

```sh
# 基础查询
# 查询指定集合的所有文档
db.user.find()

# 根据条件查询
db.user.find({"name": "tony", "age": 10})

# 模糊查询，使用正则表达式
db.user.find({"name": *ony})

# 范围查询，大于$gt，大于等于$gte，小于$lt，小于等于$lte, 不等于$ne
db.user.find({"age": {"$gt": 10}})

# 多值匹配$in,与多值不匹配$nin
db.user.find({"age": {$in: [10, 20]}})

# null值,$exists：true，确定存在该键。$in:[null]，值为null

# 查询数组
db.user.find({"like": {$all: ["a", "b"]}})


# 建索引
# 按照id,升序创建索引，降序则为-1
db.collection.createIndex({"id": 1})
# 设置id升序索引，并且建立的索引是唯一的
db.collection.createIndex({"id": 1}, {unique: true})

# 查看索引集合
db.collection.getIndexes()

# 查看集合索引大小
db.collection.totalIndexSize()

# 删除集合所有索引
db.collection.dropIndexes()

# 删除集合指定索引
db.collection.dropIndex("索引名称")
```
