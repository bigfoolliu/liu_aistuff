# mongo db介绍以及使用

<!-- TOC -->

- [mongo db介绍以及使用](#mongo-db%e4%bb%8b%e7%bb%8d%e4%bb%a5%e5%8f%8a%e4%bd%bf%e7%94%a8)
  - [a.mongodb数据类型](#amongodb%e6%95%b0%e6%8d%ae%e7%b1%bb%e5%9e%8b)
    - [a.1](#a1)
  - [索引](#%e7%b4%a2%e5%bc%95)

<!-- /TOC -->

## 基础增删改查

### 查询

```shell
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

```

## a.mongodb数据类型

### a.1

## 索引

- 提高查询效率

```shell
# 创建索引
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
