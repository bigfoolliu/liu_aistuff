# 设计模式介绍

<!-- TOC -->

- [设计模式介绍](#设计模式介绍)
    - [1.设计模式简介](#1设计模式简介)
        - [1.1设计模式特点和目的](#11设计模式特点和目的)
        - [1.2设计模式六大原则](#12设计模式六大原则)
    - [2.常用设计模式](#2常用设计模式)
        - [2.1工厂模式](#21工厂模式)
        - [2.2抽象工厂模式](#22抽象工厂模式)
        - [2.3单例模式](#23单例模式)
        - [2.4建造者模式](#24建造者模式)
        - [2.5原型模式](#25原型模式)
        - [2.6适配器模式](#26适配器模式)
        - [2.7桥接模式](#27桥接模式)
        - [2.8过滤器模式](#28过滤器模式)
        - [2.9组合模式](#29组合模式)
        - [2.10装饰器模式](#210装饰器模式)
        - [2.11外观模式](#211外观模式)
        - [2.12享元模式](#212享元模式)
        - [2.13代理模式](#213代理模式)
        - [2.14责任链模式](#214责任链模式)
        - [2.15命令模式](#215命令模式)
        - [2.16迭代器模式](#216迭代器模式)
        - [2.17中介者模式](#217中介者模式)
        - [2.18备忘录模式](#218备忘录模式)
        - [2.19观察者模式](#219观察者模式)
        - [2.20状态模式](#220状态模式)
        - [2.21空对象模式](#221空对象模式)
        - [2.22策略模式](#222策略模式)
        - [2.23模板模式](#223模板模式)
        - [2.24访问者模式](#224访问者模式)
        - [2.25MVC模式](#225mvc模式)
        - [2.26业务代表模式](#226业务代表模式)
        - [2.27组合实体模式](#227组合实体模式)
        - [2.28数据访问对象模式](#228数据访问对象模式)
        - [2.29前端控制器模式](#229前端控制器模式)
        - [2.30拦截过滤器模式](#230拦截过滤器模式)
        - [2.31服务定位器模式](#231服务定位器模式)
        - [2.32传输对象模式](#232传输对象模式)

<!-- /TOC -->

## 1.设计模式简介

- [设计模式菜鸟教程](https://www.runoob.com/design-pattern/design-pattern-intro.html)

### 1.1设计模式特点和目的

- 设计模式是代表一种软件开发的最佳实践
- 一个在软件开发过程中面临的一般问题的解决方案
- 目的是`重用代码，代码更容易被理解，保证代码的可靠性`

### 1.2设计模式六大原则

1. `开闭原则`，对扩展开放 ，对修改关闭，即程序进行修改的时候不能修改原有的代码，实现热插拔的效果，关键是`抽象化`
2. `里氏代换原则`，任何基类出现的地方，子类一定可以出现
3. `依赖倒转原则`，针对接口编程，依赖于抽象而不依赖于具体
4. `接口隔离原则`，降低类之间的耦合度
5. `迪米特原则`，一个实体应尽量少的与其他实体之间发生相互作用
6. `合成复用原则`，尽量使用合成/聚合的方式，而不是使用继承

## 2.常用设计模式

### 2.1工厂模式

**基本概念：**

- [python实现工厂模式](https://www.cnblogs.com/llbky/p/11322246.html)

**使用场景：**

- 对象的创建过程/实例化准备工作复杂，需要初始化很多参数
- 类本身有很多子类，这些类的创建过程在业务中容易发生改变，或者对类的调用容易发生改变

**实现方式：**

- [工厂模式Python实现](./design_patterns/factory_pattern.py)

### 2.2抽象工厂模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.3单例模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.4建造者模式

**基本概念：**

- 使用多个简单对象的一步一步构建一个复杂的对象
- 将一个复杂的构建，将其与表示相分离，使得同样的构建过程可以有不同的表示

**使用场景：**

- 一些基本部件不变，但是其组合经常变化

**实现方式：**

- [python实现建造者模式](./design_patterns/builder_pattern.py)

### 2.5原型模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.6适配器模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.7桥接模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.8过滤器模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.9组合模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.10装饰器模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.11外观模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.12享元模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.13代理模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.14责任链模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.15命令模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.16迭代器模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.17中介者模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.18备忘录模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.19观察者模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.20状态模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.21空对象模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.22策略模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.23模板模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.24访问者模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.25MVC模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.26业务代表模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.27组合实体模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.28数据访问对象模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.29前端控制器模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.30拦截过滤器模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.31服务定位器模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```

### 2.32传输对象模式

**基本概念：**

**使用场景：**

**实现方式：**

```python
```