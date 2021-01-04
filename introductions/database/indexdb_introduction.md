# indexdb介绍

<!-- vim-markdown-toc Marked -->

* [1.概述](#1.概述)
* [2.操作](#2.操作)
    - [2.1数据库：IDBDatabase对象](#2.1数据库：idbdatabase对象)
    - [2.2对象仓库：IDBObjectStore 对象](#2.2对象仓库：idbobjectstore-对象)
    - [2.3索引： IDBIndex 对象](#2.3索引：-idbindex-对象)
    - [2.4事务： IDBTransaction 对象](#2.4事务：-idbtransaction-对象)
    - [2.5操作请求：IDBRequest 对象](#2.5操作请求：idbrequest-对象)
    - [2.6指针： IDBCursor 对象](#2.6指针：-idbcursor-对象)
    - [2.7主键集合：IDBKeyRange 对象](#2.7主键集合：idbkeyrange-对象)

<!-- vim-markdown-toc -->

## 1.概述

- 浏览器的本地数据库，用来弥补localStorage和cookie的不足
- 不属于sql数据库,`接近Nosql数据库`，不支持sql查询
- 支持`大量数据存储`，能提供`查找接口`，还能`建立索引`
- 特点：
  1. 键值对存储，对象仓库存放数据，各种类型数据均可以存放数据，包括js对象
  2. 异步，操作时候不会锁死浏览器，异步设计是为了防止大量数据的读写，拖慢网页的表现
  3. 支持事务，事务要么全部执行，要么全部不执行
  4. 同源限制，每个数据库对应创建它的域名，网页只能访问本域名下的数据库，不能访问跨域的数据库
  5. 存储空间大，甚至没有上限
  6. 支持二进制存储

## 2.操作

- [掘金操作indexDB](https://juejin.cn/post/6844904113851875336)

### 2.1数据库：IDBDatabase对象

- 用来打开数据库

```javascript
// 创建一个IDBDatabase对象, open()会先去查找本地是否已有这个数据库，如果有则直接将这个数据库返回，如果没有，则先创建这个数据库，再返回
var request = window.indexedDB.open("db1", 1);  // 数据库名为db1，版本为1, 第一个参数为数据库名称，第二个数据库为版本号，返回一个IDBOpenDBRequest对象用于操作数据库

request.addEventListener('success', e => {
    console.log('连接数据库成功');
})
request.addEventListener('error', e => {
    console.log('连接数据库失败');
})

// 要创建一个对象仓库必须在upgradeneeded事件中，而upgradeneeded事件只会在版本号更新的时候触发
request.addEventListener('upgradeneeded', e => {
    const db = e.target.result;
})
```

### 2.2对象仓库：IDBObjectStore 对象

- 用来存储数据，类型mysql中的表
- 新建数据库与打开数据库是同一个操作，如果指定的数据库不存在，就会新建。不同之处在于，后续的操作主要在upgradeneeded事件的监听函数里面完成，因为这时版本从无到有，所以会触发这个事件。

```javascript
request.addEventListener('upgradeneeded', e => {
    const db = e.target.result
    const store = db.createObjectStore('User', {keyPath: 'userId', autoIncrement: false});
    console.log('创建对象仓库成功');
})
```

### 2.3索引： IDBIndex 对象

### 2.4事务： IDBTransaction 对象

### 2.5操作请求：IDBRequest 对象

### 2.6指针： IDBCursor 对象

### 2.7主键集合：IDBKeyRange 对象
