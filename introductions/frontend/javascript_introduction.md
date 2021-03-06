# javascript介绍

<!-- vim-markdown-toc Marked -->

* [1.概述](#1.概述)
    - [1.1介绍](#1.1介绍)
    - [1.2注释](#1.2注释)
    - [1.3关键字](#1.3关键字)
    - [1.4输入输出的三种方式](#1.4输入输出的三种方式)
    - [1.x其他](#1.x其他)
* [2.类型，变量和运算](#2.类型，变量和运算)
    - [2.1数值型(Number)](#2.1数值型(number))
    - [2.2字符串型(String)](#2.2字符串型(string))
    - [2.3数组](#2.3数组)
    - [2.4布尔型](#2.4布尔型)
    - [2.5对象](#2.5对象)
    - [2.6null和undefined](#2.6null和undefined)
    - [2.7变量类型转换](#2.7变量类型转换)
    - [2.8运算](#2.8运算)
    - [2.9条件和循环](#2.9条件和循环)
    - [2.10深浅拷贝](#2.10深浅拷贝)
    - [2.11正则表达式](#2.11正则表达式)
* [3.js函数](#3.js函数)
    - [3.1函数定义](#3.1函数定义)
    - [3.2函数参数](#3.2函数参数)
    - [3.3函数调用](#3.3函数调用)
    - [3.4this介绍](#3.4this介绍)
    - [3.5高阶函数](#3.5高阶函数)
* [4.js事件](#4.js事件)
    - [4.1基础介绍](#4.1基础介绍)
    - [4.2使用](#4.2使用)
* [5.关键字](#5.关键字)
    - [5.1this](#5.1this)
    - [5.2let](#5.2let)
* [6.javascript调试](#6.javascript调试)
* [7.javascript最佳实践](#7.javascript最佳实践)
* [8.JS HTML DOM](#8.js-html-dom)
    - [8.1基础介绍](#8.1基础介绍)
    - [8.2document对象](#8.2document对象)
    - [8.3常用DOM事件](#8.3常用dom事件)
    - [8.4DOM事件传播顺序](#8.4dom事件传播顺序)
    - [8.5DOM导航](#8.5dom导航)
    - [8.6DOM节点操作](#8.6dom节点操作)
        + [8.6.1访问元素](#8.6.1访问元素)
        + [8.6.2操作元素](#8.6.2操作元素)
        + [8.6.3事件处理](#8.6.3事件处理)
    - [8.7DOM数组](#8.7dom数组)
* [9.JS BROWSER对象](#9.js-browser对象)
    - [9.1window对象](#9.1window对象)
    - [9.2screen对象](#9.2screen对象)
    - [9.3location对象](#9.3location对象)
    - [9.4history对象](#9.4history对象)
    - [9.5navigator对象](#9.5navigator对象)
    - [9.6document对象](#9.6document对象)
    - [9.7console对象](#9.7console对象)
* [11.js JSON](#11.js-json)
* [12.jquery](#12.jquery)
* [13.js其他](#13.js其他)
    - [13.1js动画](#13.1js动画)
    - [13.2client（可视区）属性](#13.2client（可视区）属性)
    - [13.3事件和event对象](#13.3事件和event对象)
    - [13.4事件委托](#13.4事件委托)

<!-- vim-markdown-toc -->

## 1.概述

### 1.1介绍

- 使用Unicode字符集编写
- 区分大小写
- 忽略大小写，空格
- 语句结尾分号可选
- 没有整数型，只有浮点型
- 单线程
- `以事件驱动为核心`

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
- 任何变量，如果没有声明直接赋值则该变量是window的属性，如`a = 100;`, 引用时候为`window.a` ;一切声明的全局变量，全是window的属性

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
nums.every(function(item){
    return item > 0;  // 所有元素大于0返回true,否则返回false
});

nums.some(function(item){
    return item > 0;  // 主要有一个元素大于0,就返回true
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

// 其他函数
// reduce();
// splice();
```

### 2.4布尔型

```javascript
let a = true;
let b = false;
```

### 2.5对象

***对象类别:***

- `内置对象`，ES标准的，Object、Math、Date、String、Array、Number、Boolean、Function等
- `宿主对象`，JS的运行环境提供的对象，目前来讲主要指由浏览器提供的对象；BOM DOM，比如console、document
- `自定义对象`，new 关键字创建出来的对象实例，都是属于对象类型，比如Object、Array、Date等

```javascript
// 创建对象方式1
let person = {};
person.name = "tom";
person.age = 12;

// 创建对象方式2
let p = new Object();
p.gender = "男";
p['score'] = 100;  // 注意此种调用方式需要加引号

// 复杂对象与输出
const a = {
    name: 'tony',
    age: 20,
    skills: {
        language: 'javascript',
        db: 'mysql'
    }
}
console.log(JSON.stringify(a));

// 使用构造函数创建对象
function Student(name) {
    this.name = name;
    this.sayHi = function() {
        console.log('hi' + this.name);
    }
}
var stu1 = new Student();
stu1.sayHi();

// 删除对象的属性
delete stu1.name;

'name' in stu1;  // 判断属性是否在对象中

// 遍历对象的属性
for (var x in stu1) {
    return;
}

// 对象的冻结:
// 一个被冻结的对象再也不能被修改；冻结了一个对象则不能向这个对象添加新的属性，不能删除已有属性，不能修改该对象已有属性的可枚举性、可配置性、可写性，以及不能修改已有属性的值
Object.freeze(stu1);
```

### 2.6null和undefined

- `null`用来定义一个空的对象，用于定义一个变量用来保存引用类型，但是还没想好放什么内容的场景，参与数值元算当作0
- `undefined`: 声明但是没有赋值的变量；typeof(未定义的变量)；函数定义返回值时的返回值；调用参数时没有传参的参数，参与数值运算当作NaN

### 2.7变量类型转换

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

### 2.8运算

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

### 2.9条件和循环

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

### 2.10深浅拷贝

```javascript
// 浅拷贝
Object.assign(目标对象, 源对象1, 源对象2...);  // 用源对象的值追加到目标对象，如果属性值相同会更新，且可以有多个源对象

// 深拷贝: https://blog.csdn.net/chentony123/article/details/81428803
```

### 2.11正则表达式

```javascript
```

## 3.js函数

### 3.1函数定义

- 全局作用域：script标签内或者独立的js文件中
- 函数作用域：单个函数内部

```javascript
// 方法一：利用关键字，即命名函数
function x() {
    console.log("hello");
}

// 方法二：匿名函数
let y = function(a, b) { return a + b};
let z = y(4, 3);

// 方法三：使用构造函数
let myFunc = new Function("a", "b", "return a + b");
let a = myFunc(3, 4);

// 自调用函数,函数表达式自动执行
(function() {
    let b = "hello";
})();
```

### 3.2函数参数

- 调用函数的时候，每次浏览器会自动传递两个参数`函数的上下文对象this`和`封装实参的对象arguments，一个类数组对象，它可以通过索引来操作数据，也可以获取长度`

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

```javascript
// 方法一：普通调用
func1();
func1.all();

// 方法二：通过对象的方法调用
let obj = {
    func1: function(){console.log(1)}
}
obj.func1();

// 方法三：立即执行函数
(function(){
    console.log(1);
})();

// 方法四：通过构造函数调用
function func1(){};
new func1();

// 方法五：绑定时间函数
btn.onclick = function(){};

// 方法六：定时器函数
setInterval(func1(){}, 1000);
```

### 3.4this介绍

- 解析器在调用函数每次都会向函数内部传递进一个隐含的参数，这个隐含的参数就是 this，`this 指向的是一个对象`，这个对象我们称为`函数执行的上下文对象`

**函数内this的指向：**

1. 以函数的形式（包括普通函数、定时器函数、立即执行函数）调用时，`this 的指向永远都是 window`, 比如fun();相当于window.fun()
2. 以方法的形式调用时，`this 指向调用方法的那个对象`
3. 以构造函数的形式调用时，`this 指向实例对象`
4. 以事件绑定函数的形式调用时，`this 指向绑定事件的对象`
5. 使用 call 和 apply 调用时，`this 指向指定的那个对象`

```javascript
// 示例一：使用call函数可以改变函数内部的this指向
var obj1 = {
    nickName: 'hello',
    age: 10,
};

function fn1(a, b) {
    console.log(this);
    console.log(this.nickName);
    console.log(a + b);
}

fn1.call(obj1, 2, 4); // 先将 this 指向 obj1，然后执行 fn1() 函数
```

### 3.5高阶函数

- 一个函数接受函数作为参数或者输出结果为函数则为`高阶函数`

```javascript
// 函数将其他函数作为回调函数
function A(a, call_back) {
    console.log(a);
    call_back();
}

// 将其他函数作为返回值
function B() {
    return function() {
        console.log('');
    }
}
```

## 4.js事件

### 4.1基础介绍

- 网页完成加载
- 输入字段修改
- 用户点击
-[js中的常用事件](https://www.w3school.com.cn/jsref/jsref_events.asp)

### 4.2使用

```javascript
// 1.获取事件源
var div1 = document.getElementById('box1');  // id单个获取
var div_s = document.getElementByName('box');  // 通过标签名批量获取
var div_s = document.getElementByClassName('box');  // 通过类名批量获取

// 2.绑定事件
div.onclick = function(){alert('hello!')};  // 直接绑定匿名函数

function fn() {alert('hello')}; div.onclick = fn;  // 先定义再绑定

<div id="box1" onclick="fn()"></div>  // 行内绑定

```

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

### 8.1基础介绍

- `文档对象模型(document object model)`，js通过该模型来操纵Html元素, dom由节点组成，一切都是节点
- html加载完毕，在内存中生成一个dom树，整个html就是一个文档节点，`所有的节点都是对象（object)`
- [JavaScript HTML DOM 文档](https://www.w3school.com.cn/js/js_htmldom_document.asp)
- 浏览器在加载一个页面时，是按照自上向下的顺序加载的，读取到一行就运行一行。如果将script标签写到页面的上边，在代码执行时，页面还没有加载，页面没有加载DOM对象也没有加载，会导致无法获取到DOM对象。
- `onload事件`会在整个页面加载完成之后才触发。为window绑定一个onload事件，该事件对应的响应函数将会在页面加载完成之后执行

### 8.2document对象

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

### 8.3常用DOM事件

- 当用户点击鼠标时(onclick())
- 当网页加载后(onload(), onunload())
- 当图像加载后
- 当鼠标移至元素上或移出时(onmouseup(), onmousedown())
- 当输入字段被改变时(onchange())
- 当 HTML 表单被提交时
- 当用户敲击按键时

dom事件监听器:

- `addEventListener("click", displayDate, useCapture)`为指定元素增加事件处理程序,useCapture为布尔值，表示是否使用事件冒泡顺序
- `removeEventListener("mousemove", my_function)`删除元素指定额事件处理程序

### 8.4DOM事件传播顺序

1. `事件冒泡`,最内侧的元素的事件最先被处理
2. `事件捕获`,最外侧的元素的事件最先被处理

### 8.5DOM导航

```javascript
node.parentNode  // 该节点的父节点

node.childNode[2]  // 该节点的第2个子节点
node.firstChild  // 首个子节点
node.lastChild  // 最后一个子节点
node.childNodes  // 所有的子节点数组

node.nextSibling  // 下一个兄弟节点
node.previousSibling  //前一个兄弟节点
```

### 8.6DOM节点操作

DOM
DOM树

#### 8.6.1访问元素

getElementById() / querySelector()
getElementsByClassName() / getElementsByTagName() / querySelectorAll()
parentNode / previousSibling / nextSibling / children / firstChild / lastChild

#### 8.6.2操作元素

nodeValue
innerHTML / textContent / createElement() / createTextNode() / appendChild() / insertBefore() / removeChild()
className / id / hasAttribute() / getAttribute() / setAttribute() / removeAttribute()

#### 8.6.3事件处理

事件类型
UI事件：load / unload / error / resize / scroll
`键盘事件`：keydown / keyup / keypress
`鼠标事件`：click / dbclick / mousedown / mouseup / mousemove / mouseover / mouseout
`焦点事件`：focus / blur
`表单事件`：input / change / submit / reset / cut / copy / paste / select

事件绑定
HTML事件处理程序（不推荐使用，因为要做到标签与代码分离）
传统的DOM事件处理程序（只能附加一个回调函数）
事件监听器（旧的浏览器中不被支持）
事件流：事件捕获 / 事件冒泡
事件对象（低版本IE中的window.event）
target（有些浏览器使用srcElement）
type
cancelable
preventDefault()
stopPropagation()（低版本IE中的cancelBubble）
鼠标事件 - 事件发生的位置
屏幕位置：screenX和screenY
页面位置：pageX和pageY
客户端位置：clientX和clientY
键盘事件 - 哪个键被按下了
keyCode属性（有些浏览器使用which）
String.fromCharCode(event.keyCode)
HTML5事件
DOMContentLoaded
hashchange
beforeunload

```javascript
// 1.创建节点,
// 创建一个p标签节点
let p_node = document.createElement("p");
// 创建一个文本内容节点
let text_node = document.createTextNode("this is text.");

// 2.插入节点
// 父节点的最后插入一个新的子节点
父节点.appendChild(子节点);
// 在参考节点前插入一个新的节点，如果参考节点为null，那么他将在父节点里面的最后插入一个子节点
父节点.insertBefore(新的子节点, 作为参考的子节点);

// 3.删除节点
// 用父节点删除子节点。必须要指定是删除哪个子节点
父节点.removeChild(子节点);

// 4.复制节点
要复制的节点.cloneNode();  // 不带参数/false, 只复制节点自身，不复制子节点
要复制的节点.cloneNode(true);  // 复制自身和子节点

// 5.替换节点
p_node.replaceChild(new_node, old_node);


// 节点属性操作

// 1.获取节点的属性
节点.属性;
节点[属性];
节点.getAttribute('属性名称');

// 2.设置节点的属性
节点.属性 = 新值;
节点.setAttribute('属性名称', '新的属性值');

// 3.删除节点的属性值
节点.removeAttribute('属性名称');
```

### 8.7DOM数组

```javascript
// 该方法为获取所有的节点元素
let p_nodes = document.getElementsByTagName("p");
// 可以通过索引获取元素
p_node = p_nodes[1];
```

## 9.JS BROWSER对象

- 浏览器对象模型

### 9.1window对象

- `window`对象代表浏览器窗口
- [window对象介绍](https://www.runoob.com/jsref/obj-window.html)

常用属性和方法：

```javascript
// window对象常用属性
window.closed;  // 返回窗口是否关闭
window.document;  // 对Document对象的只读引用
window.history;  // 对History对象的只读引用

window.innerWidth;  // 窗口文档显示区的宽度，高度
window.innerHeight;
window.outerHeight;  // 窗口的外部宽度和高度（包含工具条和滚动条）
window.outerWidth;

window.localStorage;  // 浏览器中存储的key/value对，没有过期时间

window.name;  // 设置或者获取窗口的名称
window.sessionStorage;  // 在浏览器中存储 key/value 对。 在关闭窗口或标签页之后将会删除这些数据

// window对象常用方法
window.alert('alert');  // 警告框
window.confirm('confirm?');  // 确认框,点击确认返回true,点击取消返回false
window.prompt('input name:', 'tony');  // 提示框,点击确认返回输入值，点击取消返回NULL

window.atob('aGVsbG8=');  // 解码一个base64编码的字符串
window.btoa('hello');  // 编码一个字符串至一个base64

window.open();  // 打开一个空白窗口或者已经命名的窗口：https://www.runoob.com/jsref/met-win-open.html
window.print();  // 打印当前窗口的内容
window.stop();  // 停止页面载入

window.close();  // 关闭浏览器窗口

window.onblur();  // 当失去对在窗口失焦时候
```

### 9.2screen对象

- 或者`window.screen`对象
- 表示用户屏幕的信息
- screen.width
- screen.height
- screen.availWidth, 减去诸如窗口工具条之类的界面特征
- screen.availHeight
- screen.colorDepth, 色深
- screen.pixelDepth, 像素深度，对于现代计算机，颜色深度和像素深度是相等的

### 9.3location对象

- window.location.href 返回当前页面的 href (URL)
- window.location.hostname 返回 web 主机的域名
- window.location.pathname 返回当前页面的路径或文件名
- window.location.protocol 返回使用的 web 协议（http: 或 https:）
- window.location.assign 加载新文档

### 9.4history对象

window.history 对象可不带 window 书写。

- history.back() - 等同于在浏览器点击后退按钮
- history.forward() - 等同于在浏览器中点击前进按钮

### 9.5navigator对象

- 包含浏览器的信息

```javascript
// navigator对象常用属性
navigator.appCodeName;  // 浏览器的代码名
navigator.appName;  // 浏览器的名称

navigator.appVersion;  // 浏览器的平台和版本信息
navigator.cookieEnabled;  // 浏览器是否启用cookie

navigator.userAgent;  // 头部用户代理信息
navigator.platform;  // 浏览器的操作系统平台
```

### 9.6document对象

- document对象是html文档的根节点
- [document对象属性和方法](https://www.runoob.com/jsref/dom-obj-document.html)

```javascript
// document文档对象的常用属性
document.title  // 标题
document.head  // 头标签
document.body  // body标签
document.documentElement  // 整个html标签
```

### 9.7console对象

- 用于访问调试控制台, 在不同的浏览器里效果可能不同

```javascript
// 输出信息
console.log('hello');
console.info('信息');
console.error('错误');
console.warn('警告');

console.assert(false, '我错了');  // 断言，当前面的表达式为false的时候终止程序并报错

console.clear();  // 清除当前控制台的所有内容,js中调用，如果是在console中，可以直接使用clear()

console.dir(obj);  // 查看对象的信息, eg:console.log(console)

// 输出表格
var obj= {
     a:{ num: "1"},
     b:{ num: "2"},
     c:{ num: "3" }
};
console.table(obj);
```

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

## 11.js JSON

- `JSON.parse(string)`解析字符串至json对象
- `JSON.stringify()`将js对象转换为字符串

## 12.jquery

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

## 13.js其他

### 13.1js动画

- 三大家族：`offset/scroll/client`
- 事件对象：事件被触动时候鼠标和键盘的状态
- 动画：`闪现(少用)，匀速，缓动`

**offset家族与匀速运动:**

```javascript
// js中有一套方便的获取元素尺寸的办法就是offset家族。offset家族包括：
// offsetWidth， 获取元素节点的宽度，offsetWidth = width + padding + border
node.offsetWidth

// offsetHight，获取元素节点的高度，offsetHeight = height + padding + border
node.offsetHeight

// offsetLeft, 当前元素相对于其定位父元素的水平偏移量
// offsetTop, 当前元素相对于其定位父元素的垂直偏移量
// offsetParent, 获取当前元素的定位父元素


// 匀速运动
//2、匀速运动
btn.onclick = function () {
    //定时器，每隔一定的时间向右走一些
    setInterval(function () {
        //动画原理： 盒子未来的位置 = 盒子现在的位置 + 步长；
        //方法1：用offsetLeft获取值，用style.left赋值。
        div.style.left = div.offsetLeft + 100 + 'px';
        // 方法2：必须一开始就在DOM节点上添加 style="left: 0px;"属性，才能用方法2。否则， div.style.left 的值为 NaN
        // div.style.left = parseInt(div.style.left)+100+"px";  //方法2：
    }, 500);
};


//【重要】方法的封装：每间隔30ms，将盒子向右移动10px
function animate(ele, target) {
    //要用定时器，先清除定时器
    //一个盒子只能有一个定时器，这样的话，不会和其他盒子出现定时器冲突
    //我们可以把定时器本身，当成为盒子的一个属性
    clearInterval(ele.timer);
    //我们要求盒子既能向前又能向后，那么我们的步长就得有正有负
    //目标值如果大于当前值取正，目标值如果小于当前值取负
    var speed = target > ele.offsetLeft ? 10 : -10;  //speed指的是步长
    ele.timer = setInterval(function () {
        //在执行之前就获取当前值和目标值之差
        var val = target - ele.offsetLeft;

        //移动的过程中，如果目标值和当前值之差如果小于步长，那么就不能在前进了
        //因为步长有正有负，所有转换成绝对值来比较
        if (Math.abs(val) < Math.abs(speed)) {  //如果val小于步长，则直接到达目的地；否则，每次移动一个步长
            ele.style.left = target + "px";
            clearInterval(ele.timer);
        } else {
            ele.style.left = ele.offsetLeft + speed + "px";
        }
    }, 30)
}
```

**scroll与缓动动画：**

- `window.scroll()`：在网页向下滚动的时候触发
- `window.scrollTo(x, y)`：浏览器显示区域跳转到指定的坐标
- `scrollWidth`：获取元素整个滚动区域的宽，不包括 border和margin，内容超出盒子，为内容的宽（包括内容），不超出盒子，为盒子的宽度
- `scrollHeight`：获取元素整个滚动区域的高，不包括 border和margin，内容超出盒子，为内容的高（包括内容），不超出盒子，为盒子的高度
- `scrollLeft`：获取水平滚动条滚动的距离, 当某个元素满足`scrollWidth - scrollLeft == clientWidth`时，说明水平滚动条滚动到底了
- `scrollTop`：获取垂直滚动条滚动的距离, 当某个元素满足`scrollHeight - scrollTop == clientHeight`时，说明垂直滚动条滚动到底了

```javascript
// 文档DTD声明: https://www.w3school.com.cn/dtd/dtd_intro.asp
// 判断文档是否有DTD声明
document.compatMode === "CSS1Compat"   // 已声明
document.compatMode === "BackCompat"   // 未声明

// 文档没有DTD声明写法
document.body.scrollTop
// 文档有DTD声明写法
document.documentElement.scrollTop

// 兼容写法
document.body.scrollTop || document.documentElement.scrollTop  //方式一
document.body.scrollTop + document.documentElement.scrollTop  //方式二

// 函数封装（简单封装，实际工作使用），返回对象，实际使用为: scroll().left 或scroll().right
function scroll() {
    return { //此函数的返回值是对象
        left: window.pageYOffset || document.body.scrollTop || document.documentElement.scrollTop,
        right: window.pageXOffset || document.body.scrollLeft || document.documentElement.scrollLeft
    }
}


// 缓动动画
// 缓动动画封装
function animate(ele, target) {
    //要用定时器，先清定时器
    clearInterval(ele.timer);
    //定义定时器
    ele.timer = setInterval(function () {
        //获取步长
        //步长应该是越来越小的，缓动的算法。
        var step = (target - ele.offsetLeft) / 10;
        //对步长进行二次加工(大于0向上取整,小于0向下取整)
        //达到的效果是：最后10像素的时候都是1像素1像素的向目标位置移动，就能够到达指定位置。
        step = step > 0 ? Math.ceil(step) : Math.floor(step);
        //动画原理： 目标位置 = 当前位置 + 步长
        ele.style.left = ele.offsetLeft + step + "px";
        //检测缓动动画有没有停止
        if (Math.abs(target - ele.offsetLeft) <= Math.abs(step)) {
            //处理小数赋值
            ele.style.left = target + "px";
            clearInterval(ele.timer);
        }
    }, 30);
}
// 调用
btn.onclick = function() {
    animate(div, 400);
}
```

### 13.2client（可视区）属性

```javascript
// 获取元素的可见宽度（width + padding)
node.clientWidth
// 获取元素的可见高度（width + padding)
node.clientHeight

// body/html调用的时候,获取的是网页可视区域宽度和高度
```

### 13.3事件和event对象

- [介绍](https://github.com/qianguyihao/Web/blob/master/04-JavaScript%E5%9F%BA%E7%A1%80/45-%E4%BA%8B%E4%BB%B6%E7%9A%84%E7%BB%91%E5%AE%9A%E5%92%8C%E4%BA%8B%E4%BB%B6%E5%AF%B9%E8%B1%A1Event.md)

```javascript
// 事件的两种绑定方式
// 1.DOM写法，一个元素的一个事件只能绑定一个响应函数。如果绑定了多个响应函数，则后者会覆盖前者
element.onclick = function(){};

// 2.DOM2写法(高版本浏览器)，事件监听器，前后事件不影响
// 参数1：事件名的字符串(注意，没有on)
// 参数2：回调函数：当事件触发时，该函数会被执行
// 参数3：true表示捕获阶段触发，false表示冒泡阶段触发（默认）。如果不写，则默认为false。【重要】
// addEventListener()中的this，是绑定事件的对象
element.addEventListener('click', function (
    this.style.color = 'red';
    console.log(event);  // 当事件的响应函数被触发时，会产生一个事件对象event。浏览器每次都会将这个事件event作为实参传进之前的响应函数
) {}, false);

```

### 13.4事件委托

- 通俗地来讲，就是把一个元素响应事件（click、keydown......）的函数委托到另一个元素
- 事件委托是利用了冒泡机制，减少了事件绑定的次数，减少内存消耗，提高性能
