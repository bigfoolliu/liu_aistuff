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
- var

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
var a = 12;
var b = 12.001;
var c = 11e4;  // 110000
var d = 21e-3;  // 0.021
```

### 2.2字符串值

### 2.3数组

- 数组索引基于零

```javascript
var fruits = ["apple", "banana"];
```

### 2.4布尔型

```javascript
var a = true;
var b = false;
```

### 2.4对象

```javascript
var person = {"name": "tony", "age": 12};
```

## 3.js函数

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
var x = 15 * 5;
debugger;
```

## 7.javascript最佳实践

1. 避免使用全局变量
2. 始终申明局部变量
3. 将声明放在顶部
4. 声明变量的时候初始化
5. 不要声明数值，字符串或者布尔值
6. 不要使用new object()，即不要使用`new String`,使用`var x = ""`
7. 意识到自动类型转换，数值会被意外的转换为字符串或者NaN
8. 使用`===`进行比较，**==在比较之前会进行类型转换，===比较的时候会比较类型和值**
9. 为函数的参数值设置默认值
10. 使用default来结束switch
