# 正则表达式

<!-- TOC -->

- [正则表达式](#正则表达式)
    - [1.介绍](#1介绍)
    - [2.规则](#2规则)
    - [3.常用正则匹配示例](#3常用正则匹配示例)

<!-- /TOC -->

## 1.介绍

- 可以用来匹配处理字符串，通常用来检索，替换那些符合某个模式(规则)的文本
- 正则表达式测试工具：[正则表达式测试工具](http://tool.oschina.net/regex)

## 2.规则

|模式   |描述   |
|:---:|:---|
|.   |表示匹配除了换行符之外的任意字符   |
|^   |（脱字符）匹配输入字符串的起始位置   |
|$   |（美元符号）匹配输入字符串的结束位置   |
|\|  |a\|b，表示匹配a或b   |
|\   |将普通字符转为特殊字符，如\d表示任意十进制数字，\\.表示匹配点号本身  |
|*   |匹配前面的子表达式零次或多次，等价于{0,}   |
|+   |匹配前面的子表达式一次或多次，等价于{1,}   |
|?   |匹配前面的子表达式零次或一次，等价于{0,1}   |
|{m,n}   |m<=n，且均为非负整数，表示前面的RE表达式匹配m~n次，{m}表示匹配m次，{m,}表示至少匹配m次，{,n}表示需要匹配最多匹配n次   |
|()   |匹配括号内的表达式，也表示一个组   |
|[ ]   |匹配括号内包含的任意一个字符，出现连字符-在中间则表示字符范围描述，首位出现^表示不匹配不包含其中的任意字符   |
|\n   |匹配一个换行符   |
|\t   |匹配一个制表符   |
|\d   |匹配任意十进制数字，等价于[0-9]   |
|\D   |匹配任意非数字的字符   |
|\w   |匹配字母，数字，下划线   |
|\W   |匹配不是字母，数字，下划线的字符  |
|\s   |匹配任意空白字符，等价于[\t\n\r\f]   |
|\S   |匹配任意非空字符   |
|\z   |匹配字符串结尾，如果存在换行，同时还会匹配换行符   |
|\Z   |匹配字符串结尾，如果存在换行，只匹配换行符前的结束字符串   |
|\A   |匹配字符串开头   |

**常用修饰符:**

|修饰符   |描述   |
|:---:|:---|
|re.S（常用）   |使.匹配包括换行在内的所有字符   |
|re.X（常用）   |该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解   |
|re.I   |使匹配对大小写不敏感   |
|re.L   |做本地化识别（locale-aware）匹配   |
|re.M   |多行匹配，影响^和$   |
|re.U   |根据Unicode字符集解析字符。这个标志影响\w、\W、 \b和\B   |

## 3.常用正则匹配示例

```shell

```