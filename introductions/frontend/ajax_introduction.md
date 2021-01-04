# ajax使用

<!-- vim-markdown-toc Marked -->

* [1.概述](#1.概述)
* [2.功能](#2.功能)
    - [2.1XMLHttpRequest对象](#2.1xmlhttprequest对象)
    - [2.2解决ajax跨域问题](#2.2解决ajax跨域问题)

<!-- vim-markdown-toc -->

## 1.概述

- 异步js和xml，由js编写，程序异步执行，用xml来存储和传输数据
- 核心是`XMLHttpRequest`,为运行于浏览器的js脚本在页面内与服务器通信的手段

## 2.功能

- 不刷新页面更新网页
- 页面加载后向后台服务器请求数据
- 页面加载后向后台服务器接收数据
- 在后台向服务器发送数据

**js创建XMLHttpRequest对象向后台发送web请求。**

### 2.1XMLHttpRequest对象

- [XMLHttpRequest对象介绍](https://www.w3school.com.cn/js/js_ajax_http.asp)

常用方法：

| 方法 | 描述 |
| :---: | :--- |
| new XMLHttpRequest | 创建新的请求 |
| open(method, url, async, user, psw) | 构造请求 |
| abort() | 取消请求 |
| getAllResponseHeaders() | 获取所有的头部信息 |
| getResponseHeader() | 获取指定的头部信息 |
| send() | 发送GET请求 |
| send() | 发送POST请求 |
| setRequestHeader() | 向要发送的报头添加标签/值对 |

常用属性:

| 属性 | 描述 |
| :--- | ：---： |
| readState | 保存 XMLHttpRequest 的状态。0：请求未初始化;1：服务器连接已建立;2：请求已收到;3：正在处理请求;4：请求已完成且响应已就绪; |
| onreadystatechange | 定义当readState属性发生变化时调用的函数 |
| responseText | 以字符串返回响应数据 |
| responseXML | 以XML格式返回的数据 |
| status | 返回请求的状态号.200: "OK";403: "Forbidden";404: "Not Found" |
| statusText | 返回状态文本（比如 "OK" 或 "Not Found"） |

### 2.2解决ajax跨域问题

- [解决ajax跨域问题【5种解决方案】](https://blog.csdn.net/itcats_cn/article/details/82318092)

1. 响应头添加header允许访问
2. jsonp只支持get请求，不支持post请求
3. httpClient内部转发
4. 使用接口网关——`nginx`,`springcloud`,`zuul`(互联网公司常规解决方案)
