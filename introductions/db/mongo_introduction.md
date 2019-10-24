# mongo db介绍以及使用

<!-- TOC -->

- [mongo db介绍以及使用](#mongo-db%e4%bb%8b%e7%bb%8d%e4%bb%a5%e5%8f%8a%e4%bd%bf%e7%94%a8)
  - [索引](#%e7%b4%a2%e5%bc%95)

<!-- /TOC -->

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