# python介绍

<!-- vim-markdown-toc Marked -->

* [a.教程](#a.教程)
* [1.python魔法方法](#1.python魔法方法)
* [2.python内置函数](#2.python内置函数)

<!-- vim-markdown-toc -->

## a.教程

- [python教程，知识回顾](http://c.biancheng.net/python/)

## 1.python魔法方法

| 属性 | 说明 |
| :--: | :--- |
| __doc__ | 说明文档(模块, 类, 函数, 方法等) |
| __module__ | 查看当前对象是属于哪一个模块 |
| __class__ | 查看当前对象是属于哪一个类 |
| __bases__ | 查看本类的父类有哪些 |
| __mro__ | 查看类中方法的查找顺序,同时也是类继承的顺序 |
| __new__ | 创建对象需要首先由__new__方法在内存中申请实例存储空间,因此__new__方法先于__init__()执行 |
| __init__ | 初始化方法 |
| __call__ | 可以将对象当做函数一样去使用,称为仿函数或函数对象,可以保存函数的状态,比如可以访问函数被调用的次数 |
| __str__ | 用于对象的格式化输出 |
| __dict__ | 类的静态函数、类函数、普通函数、全局变量以及一些内置的属性都是放在类__dict__里的；对象的__dict__中存储了一些self.xxx的一些东西 |

## 2.python内置函数

| 函数 | 说明 |
| :---: | :--- |
| abs() | |
| all() | |
| any() | |
| basestring() | |
| bin() | |
| bool() | |
| bytearray() | |
| callable() | |
| chr() | |
| classmethod() | |
| cmp() | |
| compile() | |
| complex() | |
| delattr() | |
| dict() | |
| dir() | |
| divmod() | |
| enumerate() | |
| eval() | |
| execfile() | |
| file() | |
| filter() | |
| float() | |
| format() | |
| frozenset() | |
| getattr() | |
| globals() | |
| hasattr() | |
| hash() | |
| help() | |
| hex() | |
| id() | |
| input() | |
| int() | |
| isinstance() | |
| issubclass() | |
| iter() | |
| len() | |
| list() | |
| locals() | |
| long() | |
| map() | |
| max() | |
| memoryview() | |
| min() | |
| next() | |
| object() | |
| oct() | |
| open() | |
| ord() | |
| pow() | |
| print() | |
| property() | |
| raw_input() | |
| reduce() | |
| reload() | |
| repr() | |
| reverse() | |
| round() | |
| set() | |
| setattr() | |
| slice() | |
| sorted() | |
| staticmethod() | |
| str() | |
| sum() | |
| super() | |
| sum() | |
| tuple() | |
| type() | |
| unichr() | |
| unicode() | |
| vars() | |
| xrange() | |
| zip() | |
| __import__() | |
|exec | |
