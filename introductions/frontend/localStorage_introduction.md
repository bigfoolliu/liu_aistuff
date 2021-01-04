# localStorage介绍

<!-- vim-markdown-toc Marked -->

* [1.localStorage和sessionStorage基本介绍](#1.localstorage和sessionstorage基本介绍)
    - [1.1localStorage](#1.1localstorage)
    - [1.2sessionStorage](#1.2sessionstorage)
* [2.操作](#2.操作)
    - [2.1localStorage操作](#2.1localstorage操作)
    - [2.2sessionStorage的操作](#2.2sessionstorage的操作)

<!-- vim-markdown-toc -->

## 1.localStorage和sessionStorage基本介绍

### 1.1localStorage

- 本地存储，扩展了cookie的4k的限制
- 用于长久保存整个网站的数据，保存的数据`没有过期时间`，直到手动去除
- 属性是`只读`的，不可修改
- 目前限定其`值类型为字符`，相对于json格式需要转换
- 浏览器的`隐私模式下不可读`, 不能被爬虫爬取到
- 遵循`同源策略`

### 1.2sessionStorage

- 会话存储
- 临时保存同一窗口(或标签页)的数据，在关闭窗口或标签页之后将会删除这些数据，也是和localStorage的唯一一点区别

## 2.操作

### 2.1localStorage操作

```javascript
// 设置键值对
// 方式一
localStorage.setItem("key", "value");

// 方式二
var storage = window.localStorage;
storate["key"] = "value";


var value = localStorage.getItem("key");  // 获取键值

localStorage.setItem("key", "value");  // 修改键值对

localStorage.removeItem("key");  // 删除键值对

localStorage.clear();  // 清空localStorage
```

### 2.2sessionStorage的操作

```javascript
/ / 设置键值对
// 方式一
sessionStorage.setItem("key", "value");

// 方式二
var storage = window.sessionStorage;
storage["key"] = "value";


var value = sessionStorage.getItem("key");  // 获取键值

sessionStorage.setItem("key", "value");  // 修改键值对

sessionStorage.removeItem("key");  // 删除键值对

sessionStorage.clear();  // 清空sessionStorage
```

