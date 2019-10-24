# RESTful API实践

<!-- TOC -->

- [RESTful API实践](#restful-api%e5%ae%9e%e8%b7%b5)
  - [1.url设计](#1url%e8%ae%be%e8%ae%a1)
    - [1.1动词即对应的5种HTTP方法](#11%e5%8a%a8%e8%af%8d%e5%8d%b3%e5%af%b9%e5%ba%94%e7%9a%845%e7%a7%8dhttp%e6%96%b9%e6%b3%95)
    - [1.2宾语则必须是名词](#12%e5%ae%be%e8%af%ad%e5%88%99%e5%bf%85%e9%a1%bb%e6%98%af%e5%90%8d%e8%af%8d)
    - [1.3动词的覆盖](#13%e5%8a%a8%e8%af%8d%e7%9a%84%e8%a6%86%e7%9b%96)
    - [1.4复数url](#14%e5%a4%8d%e6%95%b0url)
    - [1.5避免多级url](#15%e9%81%bf%e5%85%8d%e5%a4%9a%e7%ba%a7url)
  - [2.状态码](#2%e7%8a%b6%e6%80%81%e7%a0%81)
    - [2.1状态码必须明确](#21%e7%8a%b6%e6%80%81%e7%a0%81%e5%bf%85%e9%a1%bb%e6%98%8e%e7%a1%ae)

<!-- /TOC -->

***核心思想：客户端发出的数据操作指令都是"动词 + 宾语"结构。***

## 1.url设计

### 1.1动词即对应的5种HTTP方法

- GET：读取（Read）
- POST：新建（Create）
- PUT：更新（Update）
- PATCH：更新（Update），通常是部分更新
- DELETE：删除（Delete）

### 1.2宾语则必须是名词

### 1.3动词的覆盖

有些客户端只能使用GET和POST这两种方法。服务器必须接受POST模拟其他三个方法（PUT、PATCH、DELETE）。

这时，客户端发出的 HTTP 请求，要加上X-HTTP-Method-Override属性，告诉服务器应该使用哪一个动词，覆盖POST方法。

```text
POST /api/Person/4 HTTP/1.1  
X-HTTP-Method-Override: PUT
```

上面代码中，X-HTTP-Method-Override指定本次请求的方法是PUT，而不是POST。

### 1.4复数url

无统一规定，因为常见的操作都是读取一个集合，所有使用复数。如：GET /books。

### 1.5避免多级url

- 多级url不利于扩展
- 语义不明确

***尽量使用查询字符串。***

## 2.状态码

### 2.1状态码必须明确

***每一次的请求,服务器都必须做出回应，包括状态码和数据两部分。***

HTTP状态码[常用HTTP状态码](https://www.runoob.com/http/http-status-codes.html)：

- 1xx：相关信息
- 2xx：操作成功
- 3xx：重定向
- 4xx：客户端错误
- 5xx：服务器错误

| 状态码 | 英文名称 | 中文描述 |
| :------: | :------ | :------ |
| 100 | Continue | 继续，客户端应该继续请求 |
| 200 | OK | 请求成功，一般用于GET和POST请求 |
| 201 | Created | 已创建，成功请求并创建了新的资源 |
| 202 | Accepted | 已接受，接受请求但未处理完成 |
| 203 | None-Authoritative Information | 非授权信息，请求成功，但返回的meta信息不在原始的服务，而是一个副本 |
| 204 | No Content | 无内容，服务器处理成功，但是未返回内容 |
| 205 | Reset Content | 重置内容，服务器处理成功 |
| 206 | Partical Content | 部分内容，服务器成功处理了部分Get请求 |
| 300 | Multiple Choices | 多种选择，请求的资源包含多个位置，相应可以返回一个资源特征与地址的列表用于用户终端 |
| 301 | Moved Permanently | 永久移动，请求的资源永久移动到新的URI，返回信息会包括新的URI |
