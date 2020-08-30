# javascript介绍

<!-- vim-markdown-toc Marked -->

* [1.javascript基础](#1.javascript基础)
        - [1.1词法结构](#1.1词法结构)
        - [1.2注释](#1.2注释)
        - [1.3关键字](#1.3关键字)
        - [1.x其他](#1.x其他)
* [2.类型,值和变量](#2.类型,值和变量)
        - [2.1数值](#2.1数值)
        - [2.2字符串值](#2.2字符串值)
        - [2.3数组](#2.3数组)
        - [2.4布尔型](#2.4布尔型)
        - [2.4对象](#2.4对象)
* [3.js函数](#3.js函数)
        - [3.1函数定义](#3.1函数定义)
        - [3.2函数参数](#3.2函数参数)
        - [3.3函数调用](#3.3函数调用)
        - [3.4函数call](#3.4函数call)
* [4.js事件](#4.js事件)
* [5.关键字](#5.关键字)
        - [5.1this](#5.1this)
        - [5.2let](#5.2let)
* [6.javascript调试](#6.javascript调试)
* [7.javascript最佳实践](#7.javascript最佳实践)
* [8.JS HTML DOM](#8.js-html-dom)
* [9.JS BROWSER BOM](#9.js-browser-bom)
* [10.ajax](#10.ajax)
        - [10.1功能](#10.1功能)
        - [10.2XMLHttpRequest对象](#10.2xmlhttprequest对象)
        - [10.3解决ajax跨域问题](#10.3解决ajax跨域问题)
        - [11.js JSON](#11.js-json)
        - [12.jquery](#12.jquery)

<!-- vim-markdown-toc -->

## 1.javascript基础

### 1.1介绍

- 使用Unicode字符集编写
- 区分大小写
- 忽略大小写，空格
- 语句结尾分号可选
- 没有整数型，只有浮点型
- 单线程

**JavaScript分为三个部分:**

- **ECMAScript**：JavaScript 的**语法标准**。包括变量、表达式、运算符、函数、if语句、for语句等。
- **DOM**：Document Object Model（文档对象模型），操作**页面上的元素**的API。比如让盒子移动、变色、改变大小、轮播图等等。
- **BOM**：Browser Object Model（浏览器对象模型），操作**浏览器部分功能**的API。通过BOM可以操作浏览器窗口，比如弹框、控制浏览器跳转、获取浏览器分辨率等等。

通俗理解就是：ECMAScript 是 JS 的语法；DOM 和 BOM 浏览器运行环境为 JS提供的API。

### 1.2注释

```javascript
// js单行注释

/*
js多行注释
*/
```

### 1.3关键字

- break
- continue
- debugger
- do...while
- for
- function
- if...else
- return
- switch
- try...catch
- let

### 1.4输入输出的三种方式

```javascript
// 1.弹出警告框
alert('warning');

// 2.控制台输出
console.log('hello');

// 3.弹出输入框
let a = prompt('input: ');
```

### 1.x其他

- [W3school js教程](https://www.w3school.com.cn/js/js_arithmetic.asp)
- [var和let的区别](https://blog.csdn.net/xingjia001/article/details/84560872)

## 2.类型,值和变量

注意点：

- 当数值和字符串相加时，JavaScript 将`把数值视作字符串`
- JavaScript `从左向右`计算表达式。不同的次序会产生不同的结果
- 拥有`动态类型`，这意味着相同变量可用作不同类型
- 没有值的变量，其值是`undefined`，可以通过设置值为 null 清空对象
- `null`的数据类型是对象，也可以通过设置值为 undefined 清空对象
- Undefined 与 null 的值相等，但类型不相等

一共6种数据类型：

- *基本数据类型（值类型）*：String 字符串、Number 数值、Boolean 布尔值、Null 空值、Undefined 未定义, `参数赋值的时候，传数值`。
- *引用数据类型（引用类型）*：Object 对象, 内置对象 Function、Array、Date、RegExp、Error等都是属于 Object 类型, `参数赋值的时候，传地址（修改的同一片内存空间）`。

```javascript
// 使用typeof确定变量的类型
a = 1;
typeof a;
```

### 2.1数值型(Number)

- 只有一种数值类型, 无论整数还是浮点数
- 由于内存限制不能保存所有数值，最大值`Number.MAX_VALUE`和最小值为`Number.MIN_VALUE`
- 超过最大值或者最小值，返回无穷(`Infinity`和`-Infinity`)

```javascript
let a = 12;
let b = 12.001;
let c = 11e4;  // 110000
let d = 21e-3;  // 0.021
```

### 2.2字符串型(String)

```javascript
// 字符串拼接语法，拼接前，会把与字符串相加的这个数据类型转成字符串，然后再拼接成一个新的字符串
字符串 + 任意数据类型 = 拼接之后的新字符串;

let str1 = "hello" + 1;
let str1 = "hello" + true;

// 模板字符串的输出
console.log("str1:" + str1 + ", str2:" + str2);  // 传统写法
console.log(`str1: ${str1}, str2: ${str2}`);  // ES6新写法

// 模板字符串中带有表达式
console.log("str1 + str2: " + (str1 + str2));  // 传统写法
console.log(`str1 + str2: ${str1 + str2}`);  // ES6新写法
```

### 2.3数组

- 数组索引基于零

```javascript
let fruits = ["apple", "banana"];
```

### 2.4布尔型

```javascript
let a = true;
let b = false;
```

### 2.4对象

```javascript
let person = {"name": "tony", "age": 12};
```

## 3.js函数

### 3.1函数定义

```javascript
// 基础
function x() {
  console.log("hello");
}

// 匿名函数
let y = function(a, b) { return a + b};
let z = y(4, 3);

// 函数构造器,少用
let myFunc = new Function("a", "b", "return a + b");
let a = myFunc(3, 4);

// 自调用函数,函数表达式自动执行
(function() {
  let b = "hello";
})();
```

### 3.2函数参数

```javascript
// 参数默认,没有传参数的时候会默认传递undefined,最好指定默认值
function x(a) {
    if (a === undefined) {
        a =  0;
    }
}

// 调用的参数太多（超过声明），则可以使用 arguments 对象来达到这些参数
function y(a, b, c) {
    // arguments是函数的内置对象，包含函数调用时候使用的参数数组
    let i = 0;
    for (; i < arguments.length; i++) {
        console.log(i);
    }
}
```

### 3.3函数调用

### 3.4函数call

## 4.js事件

- 网页完成加载
- 输入字段修改
- 用户点击

## 5.关键字

### 5.1this

指代它所属的对象。

- 方法中，this指的是所有者对象
- 单独情况下，指的是全局对象
- 函数中，指的是全局对象
- 函数中，严格模式下，指的是undefined
- 事件中，指的是接收事件的元素

### 5.2let

## 6.javascript调试

1. console.log()方法
2. 设置断点
3. debugger关键字

```javascript
let x = 15 * 5;
debugger;
```

## 7.javascript最佳实践

1. 避免使用全局变量
2. 始终申明局部变量
3. 将声明放在顶部
4. 声明变量的时候初始化
5. 不要声明数值，字符串或者布尔值
6. 不要使用new object()，即不要使用`new String`,使用`let x = ""`
7. 意识到自动类型转换，数值会被意外的转换为字符串或者NaN
8. 使用`===`进行比较，**==在比较之前会进行类型转换，===比较的时候会比较类型和值**
9. 为函数的参数值设置默认值
10. 使用default来结束switch

## 8.JS HTML DOM

- 文档对象模型(document object model)，js通过该模型来操纵Html元素
- [JavaScript HTML DOM 文档](https://www.w3school.com.cn/js/js_htmldom_document.asp)

**document对象:**

```javascript
// 常用操作
document.getElementById("id1").innerHTML = "a";
document.createElement("a");
document.write("a");
document.getElementById("id2").onclick = function() {};

// 常用属性
document.cookie;
document.domain;
document.URL;
```

**常用DOM事件：**

- 当用户点击鼠标时(onclick())
- 当网页加载后(onload(), onunload())
- 当图像加载后
- 当鼠标移至元素上或移出时(onmouseup(), onmousedown())
- 当输入字段被改变时(onchange())
- 当 HTML 表单被提交时
- 当用户敲击按键时

dom事件监听器:

- `addEventListener("click", displayDate, useCapture)`为指定元素增加事件处理程序,useCapture为布尔值，表示是否使用事件冒泡顺序
- `removeEventListener("mousemove", myfunction)`删除元素指定额事件处理程序

**DOM事件传播顺序:**

1. `事件冒泡`,最内侧的元素的事件最先被处理
2. `事件捕获`,最外侧的元素的事件最先被处理

**DOM导航:**

| 节点属性 | 解释 |
|  :---  | :--- |
| parentNode | 该节点的父节点 |
| childNode[2] | 该节点的第2个子节点 |
| firstChild | 首个子节点 |
| lastChild | 最后一个子节点 |
| nextSibling | 下一个兄弟节点 |
| previousSibling | 前一个兄弟节点 |

**DOM节点增删:**

```javascript
// 创建一个p标签节点
let p_node = document.createElement("p");
// 创建一个文本内容节点
let text_node = document.createTextNode("this is text.");
// 将文本节点作为p节点的子节点
p_node.appendChild(text_node);

// p节点删除文本子节点
p_node.removeChild(text_node);

// 替换节点
p_node.replaceChild(new_node, old_node);
```

**DOM数组:**

```javascript
// 该方法为获取所有的节点元素
let p_nodes = document.getElementsByTagName("p");
// 可以通过索引获取元素
p_node = p_nodes[1];
```

## 9.JS BROWSER BOM

- 浏览器对象模型

**window对象:**

- `window`对象代表浏览器窗口

**screen对象:**

- 或者`window.screen`对象
- 表示用户屏幕的信息
- screen.width
- screen.height
- screen.availWidth, 减去诸如窗口工具条之类的界面特征
- screen.availHeight
- screen.colorDepth, 色深
- screen.pixelDepth, 像素深度，对于现代计算机，颜色深度和像素深度是相等的

**location对象:**

- window.location.href 返回当前页面的 href (URL)
- window.location.hostname 返回 web 主机的域名
- window.location.pathname 返回当前页面的路径或文件名
- window.location.protocol 返回使用的 web 协议（http: 或 https:）
- window.location.assign 加载新文档

**history对象:**

window.history 对象可不带 window 书写。

- history.back() - 等同于在浏览器点击后退按钮
- history.forward() - 等同于在浏览器中点击前进按钮

**弹出框:**

- `alert("")`,警告框
- `cnfirm("")`,确认框,点击确认返回true,点击取消返回false
- `prompt("", default)`，提示框,点击确认返回输入值，点击取消返回NULL

**定时事件:**

- `setTimeout(function, milliseconds)`, 在等待指定的毫秒数后执行函数,只会执行一次
- `setInterval(function, milliseconds)`,等同于 setTimeout()，但`持续重复执行`该函数
- `clearTimeout(timeoutVariable)`方法停止执行 setTimeout() 中规定的函数
- `clearInterval(timerVariable)`方法停止 setInterval() 方法中指定的函数的执行

**cookie:**

*document.cookie属性看起来是普通字符串，但不是，读取时候只会得到其键值对、*

- 当浏览器从服务器请求一个网页时，将属于该页的 cookie 添加到该请求中,这样服务器就获得了必要的数据来“记住”用户的信息
- 如果浏览器已关闭本地 cookie 支持,则该功能不能工作
- 默认情况下，在`浏览器关闭时会删除 cookie`
- 通过 path 参数，您可以告诉浏览器 cookie 属于什么路径。`默认情况下，cookie 属于当前页`

## 10.ajax

### 10.1功能

- 不刷新页面更新网页
- 页面加载后向后台服务器请求数据
- 页面加载后向后台服务器接收数据
- 在后台向服务器发送数据

**js创建XMLHttpRequest对象向后台发送web请求。**

### 10.2XMLHttpRequest对象

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

### 10.3解决ajax跨域问题

- [解决ajax跨域问题【5种解决方案】](https://blog.csdn.net/itcats_cn/article/details/82318092)

1. 响应头添加header允许访问
2. jsonp只支持get请求，不支持post请求
3. httpClient内部转发
4. 使用接口网关——`nginx`,`springcloud`,`zuul`(互联网公司常规解决方案)

### 11.js JSON

- `JSON.parse(string)`解析字符串至json对象
- `JSON.stringify()`将js对象转换为字符串

### 12.jquery

**js的库，用于处理浏览器不兼容以及简化html的dom操作，事件处理等。**

```javascript
// 查找id为id1的元素
let ele1 = $("#id1");

// 查找<p>标签的元素
let ele2 = $("p");

// 查找类为intro的元素
let ele3 = $(".intro");

// css选择器,选择所有类为intro，标签为p的元素
let ele4 = $("p.intro");
```
