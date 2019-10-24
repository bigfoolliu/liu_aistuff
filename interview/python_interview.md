# python面试

<!-- TOC -->

- [python面试](#python%e9%9d%a2%e8%af%95)
  - [1.语言特性](#1%e8%af%ad%e8%a8%80%e7%89%b9%e6%80%a7)
    - [1.1元类(metaclass)](#11%e5%85%83%e7%b1%bbmetaclass)
    - [1.2python自省](#12python%e8%87%aa%e7%9c%81)
    - [1.3面向切面编程(AOP)和装饰器](#13%e9%9d%a2%e5%90%91%e5%88%87%e9%9d%a2%e7%bc%96%e7%a8%8baop%e5%92%8c%e8%a3%85%e9%a5%b0%e5%99%a8)
    - [1.4python函数重载](#14python%e5%87%bd%e6%95%b0%e9%87%8d%e8%bd%bd)
    - [1.5python单例模式](#15python%e5%8d%95%e4%be%8b%e6%a8%a1%e5%bc%8f)
    - [1.6GIL全局解释性锁](#16gil%e5%85%a8%e5%b1%80%e8%a7%a3%e9%87%8a%e6%80%a7%e9%94%81)
    - [1.7python协程](#17python%e5%8d%8f%e7%a8%8b)
    - [1.8python函数式编程](#18python%e5%87%bd%e6%95%b0%e5%bc%8f%e7%bc%96%e7%a8%8b)
    - [1.9python垃圾回收机制](#19python%e5%9e%83%e5%9c%be%e5%9b%9e%e6%94%b6%e6%9c%ba%e5%88%b6)
  - [2.重点算法](#2%e9%87%8d%e7%82%b9%e7%ae%97%e6%b3%95)
    - [2.1快速排序](#21%e5%bf%ab%e9%80%9f%e6%8e%92%e5%ba%8f)
    - [2.2二分搜索](#22%e4%ba%8c%e5%88%86%e6%90%9c%e7%b4%a2)
    - [2.3二叉树相关](#23%e4%ba%8c%e5%8f%89%e6%a0%91%e7%9b%b8%e5%85%b3)
    - [2.4KMP算法](#24kmp%e7%ae%97%e6%b3%95)

<!-- /TOC -->

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
Python有鸭子类型，对象的特征不是由类型决定，而是由方法决定，函数重载没什么意义。

### 1.5python单例模式

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
- `python的多线程对IO密集型起作用，对于CPU密集型任务则几乎没有任何优势反而会应为资源争夺而变慢`

### 1.7python协程

协程，进程的升级版，用户自己控制内核态用户态的切换，不需要陷入系统的内核态，加快速度。

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

### 1.9python垃圾回收机制

1. `引用计数`,每个对象都有对其引用的计数，当没有引用时候，就会销毁
2. `标记-清除机制`
3. `分代技术`

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

### 2.3二叉树相关

[二叉树相关算法](../data_structure/binary_tree/basic_binary_tree.py)

### 2.4KMP算法
