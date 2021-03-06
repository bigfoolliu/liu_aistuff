# 设计模式介绍

<!-- vim-markdown-toc Marked -->

* [1.设计模式简介](#1.设计模式简介)
* [2.常用设计模式](#2.常用设计模式)
        - [2.1创建型模式](#2.1创建型模式)
                + [2.1.1工厂模式](#2.1.1工厂模式)
                + [2.1.2建造者模式](#2.1.2建造者模式)
                + [2.1.3原型模式](#2.1.3原型模式)
        - [2.2结构型模式](#2.2结构型模式)
                + [2.2.1适配器模式](#2.2.1适配器模式)
                + [2.2.2修饰器模式](#2.2.2修饰器模式)
                + [2.2.3外观模式](#2.2.3外观模式)
                + [2.2.4享元模式](#2.2.4享元模式)
                + [2.2.5模型-视图-控制器模式(MVC)](#2.2.5模型-视图-控制器模式(mvc))
                + [2.2.6代理模式](#2.2.6代理模式)
        - [2.3分型模式](#2.3分型模式)
                + [2.3.1责任链模式](#2.3.1责任链模式)
                + [2.3.2命令模式](#2.3.2命令模式)
                + [2.3.3解释器模式](#2.3.3解释器模式)
                + [2.3.4观察者模式](#2.3.4观察者模式)
                + [2.3.5状态模式](#2.3.5状态模式)
                + [2.3.6策略模式](#2.3.6策略模式)
                + [2.3.7模板模式](#2.3.7模板模式)

<!-- vim-markdown-toc -->

## 1.设计模式简介

- [设计模式菜鸟教程](https://www.runoob.com/design-pattern/design-pattern-intro.html)
- 书籍：<<精通Python设计模式>>

**设计模式特点和目的:**

- 设计模式是代表一种软件开发的最佳实践
- 一个在软件开发过程中面临的一般问题的解决方案
- 目的是`重用代码，代码更容易被理解，保证代码的可靠性`

**设计模式六大原则:**

1. `开闭原则`，对扩展开放 ，对修改关闭，即程序进行修改的时候不能修改原有的代码，实现热插拔的效果，关键是`抽象化`
2. `里氏代换原则`，任何基类出现的地方，子类一定可以出现
3. `依赖倒转原则`，针对接口编程，依赖于抽象而不依赖于具体
4. `接口隔离原则`，降低类之间的耦合度
5. `迪米特原则`，一个实体应尽量少的与其他实体之间发生相互作用
6. `合成复用原则`，尽量使用合成/聚合的方式，而不是使用继承

## 2.常用设计模式

### 2.1创建型模式

用来处理对象创建相关的问题。

#### 2.1.1工厂模式

使用场景：

- 对象的创建过程/实例化准备工作复杂，需要初始化很多参数
- 在一个集中的地方创建对象，便于跟踪对象

- [python实现工厂模式](https://www.cnblogs.com/llbky/p/11322246.html)
- [工厂模式Python实现](./design_patterns/factory_pattern.py)

`抽象工厂`设计模式是抽象方法的一种泛化，即为逻辑上的一组抽象方法。

#### 2.1.2建造者模式

- 一个复杂的需要多个过程构建的对象，建造者模式可以让其构造过程和表现分离
- 当我们知道一个对象必须经过多个步骤构建，并且要求同一个构建过程可以有不同的表现就可以使用建造者模式
- 该模式有两个参与者: `建造者`和`指挥者`，建造者负责创建复杂对象的各个组成部分，指挥者使用建造者实例控制建造的过程

- [建造者模式Python实现](./design_patterns/builder_pattern.py)

#### 2.1.3原型模式

- 帮助创建对象的完整副本
- python中的`copy.deepcopy()`

### 2.2结构型模式

用来处理系统中不同实体之间的关系，关注提供一种简单的对象组合方式来创造新功能。

#### 2.2.1适配器模式

- 实现两个不兼容接口的兼容

#### 2.2.2修饰器模式

- 扩展已有对象的功能(其他扩展功能的方法还有：直接添加到原有对象中；继承；组合)
- 使用场景有：数据校验，日志，事务处理，缓存，监控，调试，压缩，加密

#### 2.2.3外观模式

- 已有复杂系统的抽象层
- 隐藏系统的复杂性，并通过一个简化的接口暴露给客户端

#### 2.2.4享元模式

- 通过相似对象的数据共享来`最小化内存使用，提升性能`
- 一个享元(Flyweight)就是一个包含状态独立的不可变数据的共享对象
- 重点在于将可变属性和不可变的属性分开

#### 2.2.5模型-视图-控制器模式(MVC)

- `模型`是核心，代表信息本源，包含和管理业务逻辑，数据，状态以及应用的规则
- `视图`是模型的可视化表现，仅展示数据，不处理数据
- `控制器`连接模型和视图，模型和视图的通信通过控制器完成

对比于`MVT`,模板T表明的意思是将内容和展现分开，描述的是用户看到数据的方式。

#### 2.2.6代理模式

- 将计算成本较高的对象的创建延迟到用户首次用到它时才进行
- 使用代理对象在访问实际对象之前执行重要的操作

类型：

1. 远程代理，存在于不同地址空间的网络对象(比如远程服务器)在本地的代理
2. 虚拟代理，用于懒初始化，将一个大计算量对象的创建延迟至真正需要的时候执行,可以提高性能
3. 保护/防护代理，控制对敏感对象的访问
4. 智能(引用)代理，对象被引用之后执行操作，用于引用计数和线程执行安全

### 2.3分型模式

#### 2.3.1责任链模式

- 用于多个对象处理一个请求或者预先不知道由哪个对象来处理请求

步骤：

1. 存在一个对象链(链表，树或者其他)
2. 将请求发送给第一个对象
3. 对象决定是否处理该请求
4. 对象将请求发送给下一个对象
5. 重复该过程至链尾

#### 2.3.2命令模式

- 帮助将一个操(**撤销**，复制，删除等)封装为一个对象，即创建一个包含所有该操作和逻辑的类
- 使用场景有：GUI按钮和菜单项，事务型行为和日志记录，宏(动作序列)

#### 2.3.3解释器模式

- 使用DSL（领域特定语言）
- DSL分为内部DSL和外部DSL

#### 2.3.4观察者模式

- 用于描述单个对象（发布者/支持者）与多个对象（订阅者/观察者）之间的发布-订阅关系
- 事件驱动系统，事件监听者正在监听的事情被创建，就触发
- 用于降低发布者和订阅者之间的耦合度

使用场景：事件驱动系统

#### 2.3.5状态模式

- 本质上就是实现一个状态机（状态+转换）来解决特定领域的问题

#### 2.3.6策略模式

- 运行时候能够根据场景透明切换算法

#### 2.3.7模板模式

- 旨在消除代码冗余和重复
