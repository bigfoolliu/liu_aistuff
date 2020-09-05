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

## 2.类型，变量和运算

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
- 由于内存限制不能保存所有数值，最大值`Number.MAX_VALUE (约1.79e308)`和最小值为`Number.MIN_VALUE(约5-e324)`
- 超过最大值或者最小值，返回无穷(`Infinity`和`-Infinity`)
- `NaN`，特殊数字，表示非数值，与任何值都不相等，包括 NaN 本身。

```javascript
let a = 12;
let b = 12.001;
let c = 11e4;  // 110000
let d = 21e-3;  // 0.021

// 判断是否为整数
布尔值 = Number.isInteger(数字);
a.isInteger();

// 小数点后面保留指定位数,返回值是一个字符串,不会改变原值，会四舍五入取结果
字符串 = b.toFixed(num);

// 内置对象Math的常用用法
// Math.PI 圆周率
// Math.abs() 返回绝对值
// Math.random() 生成0-1之间的随机浮点数,取值范围是 [0，1)
// Math.floor() 向下取整（往小取值）
// Math.ceil() 向上取整（往大取值）
// Math.round() 四舍五入取整（正数四舍五入，负数五舍六入）
// Math.max(x, y, z) 返回多个数中的最大值
// Math.min(x, y, z) 返回多个数中的最小值
// Math.pow(x,y) 乘方：返回 x 的 y 次幂
// Math.sqrt() 开方：对一个数进行开方运算

// 生成 [0, x) 之间的随机数
Math.round(Math.random()*x)
// 生成 [x, y) 之间的随机数
Math.round(Math.random()*(y-x)+x)

// 数值的隐式转换，当有符号 + - * / 的时候,注意要提前转换好类型
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

// 常用方法
// 检索一个字符串中是否含有指定内容。如果字符串中含有该内容，则会返回其第一次出现的索引；如果没有找到指定的内容，则返回 -1。
索引值 = str.indexOf(想要查询的字符串);
索引值 = str.indexOf(想要查询的字符串, [起始位置]);  // 第二个参数指定查找的起始位置
str1.indexOf("e");

// 获取字符串中指定内容的索引
索引值 = str.search(想要查找的字符串);
索引值 = str.search(正则表达式);
str1.search("ll");

// 字符串中是否包含指定的内容,position默认为0,规定查找起始位置
布尔值 = str.includes(想要查找的字符串, [position]);

// 是否以指定的字符串开始或结尾
str1.startsWith("he");
str1.endsWith("lo");

// 获取指定位置的字符
str1.charAt(2);
str1[2];

// 字符串截取,slice(开始索引，结束索引)，包含左边的，不包含右边的
str1.slice(1, 4);

// 通过分隔符将字符串转换为数组
str1.split(".");

// 字符串的替换,默认只会替换第一个被匹配到的字符
新的字符串 = str.replace(被替换的字符，新的字符);
str2 = str1.replace("ll", "ee");

// 重复字符串
"*".repeat(4); // ****

// 去除字符串前后的空白
str1.trim();

// 大小写转换
str1.toLowerCase();
str1.toUpperCase();

// 相关的html方法
str1.anchor();  // <a name="undefined">hello</a>
str1.big();  // <big>hello</big>
str1.sub();  // <sub>hello</sub>
str1.sup();  // <sup>hello</sup>
str1.link('http://www.baidu.com');  // <a href="http://www.baidu.com">hello</a>
str1.bold();  // <b>hello</b>

// url编解码
encodeURIComponent(str1);  // 把字符串作为 URI 组件进行编码
decodeURIComponent(str1);  // 把字符串作为 URI 组件进行解码
```

### 2.3数组

- 数组索引基于零
- 数组的类型实际上也是对象
- `伪数组`: 包含 length 属性的对象或可迭代的对象

```javascript
// 普通方式
let fruits = ["apple", "banana"];

// 构造函数方式
let names = new Array();
let nums = new Array(2, 3)

// 数组中添加元素,获取不存在的索引时候返回undefined
nums[4] = 12;

// 获取数组的长度
len = nums.length;

// 数组的常用方法
nums.isArray();  // 判断是否为数组
nums.toString(); // 数组转换为字符串

nums.push(2);  // 末尾添加元素
nums.pop();  // 删除末尾元素
nums.fill();  // 固定的数值填充数组

nums.concat(nums);  // 数组合并
nums.join();  // 数组转换为字符串

nums.reverse();  // 数组翻转
nums.sort();  // 数组元素按照Unicode从小到大排列

// 伪数组转换为真数组
realArray = Array.from(fakeArray);

索引值 = 数组.indexOf(想要查询的元素);

// 判断数组是否包含某个元素
nums.includes(1);

// find函数, 找出第一个满足「指定条件返回 true」的元素；如果没找到，则返回 undefined。
nums.find((item, index) => {
    return item > 2; // 找到第一个元素大于2的元素，找到了则返回该元素
});

// 找到第一个满足条件的index
nums.findIndex((item, index) => {
    return item > 2;
});


// every()：全部真，才为真。当你需要让数组中的每一个元素都满足指定条件时，那就使用 every()。
// some()：一个真，则为真，点到为止。数组中只要有一个元素满足指定条件时，就停止遍历。那就使用 some()。
nums.every(function(item, index, array){
    if (item > 2) {return false};  // 所有的元素大于2才返回true
    return true
});

nums.some(function(item, index, array){
    if (item > 2){return true};  // 只要有一个元素大于2则返回true
    return false
});


// 数组的遍历
// 如果纯粹只是遍历数组，那么，可以用 forEach() 方法; 如果你想在遍历数组的同时，去改变数组里的元素内容，那么，最好是用 map() 方法来做，不要用 forEach()方法
nums.forEach((item, index, array) => {
    console.log(item);
});

nums.map((item, index, array) => {
    return item + 1;
});

// 数组过滤
nums.filter((item) => {
    if(item > 2){return true};  // 过滤出所有的大于2的元素，组成新元素
    return false;
});
```

### 2.4布尔型

```javascript
let a = true;
let b = false;
```

### 2.4对象

***对象类别:**

- `内置对象`，ES标准的，Object、Math、Date、String、Array、Number、Boolean、Function等
- `宿主对象`，JS的运行环境提供的对象，目前来讲主要指由浏览器提供的对象；BOM DOM，比如console、document
- `自定义对象`，new 关键字创建出来的对象实例，都是属于对象类型，比如Object、Array、Date等

```javascript
// 方式1
let person = {};
person.name = "tom";
person.age = 12;

// 方式2
let p = new Object();
p.gender = "男";
```

### 2.5null和undefined

- `null`用来定义一个空的对象，用于定义一个变量用来保存引用类型，但是还没想好放什么内容的场景，参与数值元算当作0
- `undefined`: 声明但是没有赋值的变量；typeof(未定义的变量)；函数定义返回值时的返回值；调用参数时没有传参的参数，参与数值运算当作NaN

### 2.6变量类型转换

```javascript
// 1.其他数据类型-->字符串
let a = 1;
a.toString();  // toString()不会改变原来变量的值
console.log(a + "");  // 隐式的类型转换
String(a);  // 强制的类型转换，也不会影响到原来的变量

// 2.其他数据类型-->Number
// 字符串-->Number,纯数字直接转；空格或空为0；含非数字内容的转为NaN;
// 布尔-->Number, true为1，false为0;
// null为0，undefined为NaN
Number(true);
Number("12.1");

let b = "12.ab";
parseInt(b);  // 数字开头自动取前，否则报错
parseInt(b, 16);  // 以16进制转换

// 3.转换为Boolean
// 数字 --> 布尔。除了 0 和 NaN，其余的都是 true。也就是说，Boolean(NaN)的结果是 false。
// 字符串 ---> 布尔。除了空串，其余的都是 true。全是空格的字符串，转换结果也是 true。字符串'0'的转换结果也是 true。
// null 和 undefined 都会转换为 false。
// `引用数据类型会转换为 true。注意，空数组[]和空对象{}，转换结果也是 true

// 使用运算符号的时候也会隐式的调用类型转换
```

### 2.7运算

- 算数运算符：`+ - * / %(取余) ++(自增) --(自减)`
- 逻辑运算符：`&&(与) ||(或) !(非)`
- 逻辑运算符：`> < >= <= == ===(全等于) !=(不等于) !==(不全等于)`

**短路运算:**

```javascript
// 短路运算&&
// 如果第一个值为false，则不会执行后面的内容。
// 如果第一个值为 true，则继续执行第二条语句，并返回第二个值。
let a = 1;
a && alert("hello");  // 会执行alert

// 短路运算||
// 如果第一个值为true，则不会执行后面的内容。
// 如果第一个值为 false，则继续执行第二条语句，并返回第二个值。
a || alert("hello");  // 不会执行alert


// 非数值的比较会将其转换为数值比较
1 > "0";  // true

// 如果两侧都是字符串比较则比较字符串的Unicode编码
"22" > "100"; // true

// == 会做隐式转换，不严谨，而 === 则会严格比较
1 == "1";  // true
1 === "1"; // false
"1" == true;  // true

// 三元运算符
// 条件表达式 ? 语句1 : 语句2;
```

### 2.8条件和循环

```javascript
// 条件语句推荐写法
function handleCode(code) {
    if (code == 200) {
        return "success";
    }
    if (code == 400) {
        return "bad request"
    }
}


// 循环写法
for (let i = 0; i < 12; i++) {
    console.log(i);
}
// 循环推荐写法
items.map(function(item){
    console.log(item);
})
// while循环
let a = 1；
while (a < 10) {
    a ++;
}
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

**document.cookie属性看起来是普通字符串，但不是，读取时候只会得到其键值对:**

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
