# cookie

<!-- vim-markdown-toc Marked -->

* [1.概述](#1.概述)
    - [1.1介绍](#1.1介绍)
    - [1.2使用场景](#1.2使用场景)
* [2.基本属性](#2.基本属性)
* [3.操作](#3.操作)

<!-- vim-markdown-toc -->


## 1.概述

### 1.1介绍

- 保存在浏览器的一小段文本信息
- 一般单个域名的cookie数量不超过30个，每个cookie大小不超过4k，超过的则忽略
- 每次向服务器请求都会带上cookie
- 键值对存储
- 服务器接收到cookie的时候：`1.不知道cookie的过期时间；2.不知道是哪个域名设置的cookie`

### 1.2使用场景

- `会话管理`，保存用户登陆，购物车等信息
- `个性化`，保存用户偏好，如网页字体大小，背景色等
- `追踪`，记录和分析用户的行为

## 2.基本属性

- `name`, cookie的键
- `value`，cookie的值
- `domain`，所属域名，默认为当前域名
- `path`，生效路径，默认为当前网址, `/`根路径则在所有路径有效
- `expires`，过期时间, UTC格式,浏览器根据本地时间决定 Cookie 是否过期,本地时间是不精确的，`不能保证 Cookie 一定在服务器指定的时间过期`
- `max-age`，指定从现在开始cookie存在的秒数，过了时间则失效，`指定了Expires和Max-Age，那么Max-Age的值将优先生效`
- `size`，
- `http-only`，指定该cookie不能被脚本拿到，只有浏览器发送http请求时候才会带上该cookie
- `secure`，指定浏览器只有在加密协议 HTTPS 下，才能将这个 Cookie 发送到服务器
- `samesite`
- `priority`

## 3.操作

- 可以一次读出所有的cookie，但是一次只能写入一个cookie

```javascript
// 创建cookie, 日期格式可以使用Date.prototype.toUTCString()进行日期格式转换
document.cookie = "username=tony;expires=Fri, 31 Dec 2020 23:59:59 GMT";

// 读取cookie
document.cookie

// 删除一个cookie的方法，将其过期时间设置为过去的时间
document.cookie = "username=;expires=Thu, 01-Jan-1970 00:00:01 GMT";
```
`
