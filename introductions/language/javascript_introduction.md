# javascript介绍

<!-- TOC -->

- [javascript介绍](#javascript%e4%bb%8b%e7%bb%8d)
  - [1.javascript基础](#1javascript%e5%9f%ba%e7%a1%80)

<!-- /TOC -->

## 1.javascript基础

- [W3school js教程](https://www.w3school.com.cn/js/js_arithmetic.asp)
- [var和let的区别](https://blog.csdn.net/xingjia001/article/details/84560872)

js关键字：

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

js注释：

```javascript
// js单行注释

/*
js多行注释
*/
```

js特点：

1. 对大小写敏感
2. 尽量使用驼峰命名法则
3. 使用Unicode字符集

## 2. js数据类型

注意点：

- 当数值和字符串相加时，JavaScript 将`把数值视作字符串`
- JavaScript `从左向右`计算表达式。不同的次序会产生不同的结果
- 拥有`动态类型`，这意味着相同变量可用作不同类型
- 没有值的变量，其值是`undefined`，可以通过设置值为 null 清空对象
- `null`的数据类型是对象，也可以通过设置值为 undefined 清空对象
- Undefined 与 null 的值相等，但类型不相等

```javascript
// 使用typeof确定变量的类型
a = 1;
typeof a;
```

### 2.1数值

- 只有一种数值类型
- 写数值时用不用小数点均可

```javascript
let a = 12;
let b = 12.001;
let c = 11e4;  // 110000
let d = 21e-3;  // 0.021
```

### 2.2字符串值

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
