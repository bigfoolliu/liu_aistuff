# python面试

<!-- vim-markdown-toc Marked -->

* [1.语言特性](#1.语言特性)
        - [1.1元类(metaclass)](#1.1元类(metaclass))
        - [1.2python自省](#1.2python自省)
        - [1.3面向切面编程(AOP)和装饰器](#1.3面向切面编程(aop)和装饰器)
        - [1.4python函数重载](#1.4python函数重载)
        - [1.5单例模式](#1.5单例模式)
        - [1.6GIL全局解释性锁](#1.6gil全局解释性锁)
        - [1.7python协程](#1.7python协程)
        - [1.8python函数式编程](#1.8python函数式编程)
        - [1.9垃圾回收机制](#1.9垃圾回收机制)
        - [1.10python中变量的作用域](#1.10python中变量的作用域)
        - [1.11python解释器](#1.11python解释器)
        - [1.12闭包](#1.12闭包)
        - [1.13提高python代码效率的方式](#1.13提高python代码效率的方式)
        - [1.14python内存管理](#1.14python内存管理)
        - [1.15python多线程和多进程](#1.15python多线程和多进程)
* [2.重点算法](#2.重点算法)
        - [2.1快速排序](#2.1快速排序)
        - [2.2二分搜索](#2.2二分搜索)
        - [2.3二叉树相关算法](#2.3二叉树相关算法)
* [3.面试常见问题](#3.面试常见问题)
        - [3.1.pyc和PyCodeObject是什么（涉及python执行过程详解）](#3.1.pyc和pycodeobject是什么（涉及python执行过程详解）)
        - [3.2range和xrange的区别](#3.2range和xrange的区别)
        - [3.3python中下划线使用总结](#3.3python中下划线使用总结)

<!-- vim-markdown-toc -->

## 1.语言特性

### 1.1元类(metaclass)

- [python metaclass深入解析](https://www.cnblogs.com/yssjun/p/9832526.html)
- [python metaclass解析](https://www.liaoxuefeng.com/wiki/897692888725344/923030550637312)

简单来说就是元类是用来创建类的，是类的模板。

### 1.2python自省

即简单一句就能知道运行时获得对象的类型,如`type()`,`getattr()`,`hasattr()`,`isinstance()`。

### 1.3面向切面编程(AOP)和装饰器

**装饰器**:

- 本质是嵌套函数
- 用于抽离与函数本身无关的功能，增加函数的通用性，在`缓存`,`权限校验`，`性能测试`，`插入日志`等场景使用
- [python装饰器的一些用法](https://blog.csdn.net/qq_26886929/article/details/54091962)
- [python装饰器使用的具体代码](../python/python/decorator/cache_decorator.py)

### 1.4python函数重载

[知乎python函数重载](https://www.zhihu.com/question/20053359)

静态语言函数或者方法重载的目的是希望类可以处理不同的类型的数据，多个同名函数同时存在，具有不同的参数个数/类型，是类中多态性的一种体现。
Python有`鸭子类型，对象的特征不是由类型决定，而是由方法决定`，函数重载没什么意义。

### 1.5单例模式

```python
class SingleTon(object):

    """继承该父类的类都是单例类,即重写类的new方法"""

    _instance = {}  # 用来保存自己类的实例

    def __new__(cls, *args, **kwargs):
        # 如果没有创建过该实例则创建一个自身的实例
        if cls not in cls._instance:
            cls._instance[cls] = super().__new__(cls)
        return cls._instance[cls]
```

**单例模式使用场景**：

1. 任务管理器
2. 网站计数器
3. 应用程序的日志应用
4. web应用的配置对象
5. 数据库连接池
6. 多线程的线程池

即需要生成唯一序列的场景，需要频繁实例化然后销毁的对象的场景，创建对象很耗费资源但有经常用到的场景，方便资源相互通信的场景。

### 1.6GIL全局解释性锁

- 即一个核只能在同一时间运行一个线程
- 目的是为了保证线程安全而采取的独立线程运行的限制
- `python的多线程对IO密集型起作用(此时影响因素主要是网络延迟)`
- `python的多线程对计算密集型任务则几乎没有任何优势，反而会应为资源争夺而变慢`
- `python的多进程应用于计算密集型，每个进程独立，有独立的python解释器实例，没有GIL可以争夺`

### 1.7python协程

- 协程，进程的升级版，用户自己控制内核态用户态的切换，不需要陷入系统的内核态，加快速度
- python中的协程实现主要是用`yield`

### 1.8python函数式编程

```python
# filter过滤函数
a = [1, 2, 3]
ret = filter(lambda x: x > 2, a)

# map函数，对序列中的每个元素依次执行函数
ret = map(lambda x: x+1, a)

# reduce函数，对序列中的每个元素迭代调用函数,如取3的阶乘
ret = reduce(lambda x,y:x*y, range(1, 4))
```

### 1.9垃圾回收机制

1. `引用计数`,每个对象都有对其引用的计数，当没有引用时候，就会销毁
2. `标记-清除机制`
3. `分代技术`

### 1.10python中变量的作用域

变量查找顺序(LEGB)：

1. L:local，函数内部作用域
2. E:enclosing，函数内部与内嵌函数之间
3. G:global，全局作用域
4. B:build-in，内置作用域

### 1.11python解释器

- 由`编译器`和`虚拟机`构成
- 编译器将py文件编译为pyc字节码文件，虚拟机执行字节码
- 现有的python解释器主要有三类：`CPython`,`PyPy`,`JPython`
  - "cpython"使用最多,底层由c语言实现

### 1.12闭包

- 即当函数内部定义一个函数，内部的函数用到了外部的函数的一些变量
- 一般python定义的带参数的装饰器就会生成一个闭包
- [python闭包介绍](https://blog.csdn.net/bandaoyu/article/details/85655968)

### 1.13提高python代码效率的方式

- [python提高代码代码效率的方式](https://www.cnblogs.com/duaimili/p/10275728.html)

### 1.14python内存管理

使用`内存池`机制（即Pymalloc机制）来管理小块内存的申请和释放。

频繁的申请和创建小的内存空间会到导致大量的`内存碎片`，内存池首先在内存中申请一定数量的，大小相等的内存块留作备用；当有新的内存需求时，从内存池中分配内存给这个需求，不够了再申请新的内存。

**python中的内存池管理机制Pymalloc两套实现：**

1. 针对小对象(小于256bits)，pymalloc在内存池中申请空间
2. 其他则直接执行new/malloc的行为来申请内存空间

### 1.15python多线程和多进程

**传递参数的方式：**

- python多线程有GIL，属于并发，非并行
- python多进程将共享参数，可以使用`multiprocessing.Value`和`multiprocessing.Array`

**python多线程和多进程的区别：**

- 多进程的话，子进程结束需要join()，多线程则不需要
- 多线程容易共享资源，可以使用全局变量和参数，多进程有自己的内存空间，可以通过共享内存和Manager的方法

## 2.重点算法

### 2.1快速排序

```python
def quick_sort(array):
    """
    array: list
    return: list
    """
    if not array:
        return array

    def recrusive(begin, end):
        if begin >= end:
            return
        l, r = begin, end
        pivot = array[begin]
        while l < r:
            while l < r and array[r] >= pivot:
                r -= 1
            array[l] = array[r]
            while l < r and array[l] <= pivot:
                l += 1
            array[r] = array[l]
        array[l] = pivot

        recrusive(begin, l-1)
        recrusive(l+1, end)

    begin = 0
    end = len(array) - 1
    recrusive(begin, end)
    return array
```

### 2.2二分搜索

```python
def binary_search(array, target):
    """
    array: list
    target: numbers
    return: int
    """
    if not array:
        return array
    begin = 0
    end = len(array) - 1
    while begin <= end:
        mid = int((end-begin)/2 + begin)
        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            begin = mid + 1
        else:
            return mid
    return None
```

### 2.3二叉树相关算法

[二叉树相关算法](../data_structure/binary_tree/basic_binary_tree.py)

## 3.面试常见问题

### 3.1.pyc和PyCodeObject是什么（涉及python执行过程详解）

- [pyc文件](https://blog.csdn.net/huanhuanq1209/article/details/79724632)

- python先编译后解释，将.py编译为字节码，通过虚拟机执行
- PyCodeObject(内存中)是python编译器真正编译的结果
- .pyc文件是python程序执行完成之后python解释器将PyCodeObject写入的结果

### 3.2range和xrange的区别

- range根据范围生成一个序列，python3用
- xrange不生成一个序列，而是一个生成器，生成大的集合时候性能更好，python2用

### 3.3python中下划线使用总结

- 单下划线开头表示该方法不是API的一部分，不要直接访问
- 双下划线开头表示子类不能重写该方法
