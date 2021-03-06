# 操作系统介绍

<!-- vim-markdown-toc Marked -->

* [1.操作系统介绍](#1.操作系统介绍)
        - [1.1CPU](#1.1cpu)
        - [1.2主存](#1.2主存)
        - [1.3I/O设备](#1.3i/o设备)
        - [1.4文件](#1.4文件)
        - [1.5操作系统结构](#1.5操作系统结构)
* [2.进程,线程和协程](#2.进程,线程和协程)
        - [2.1进程](#2.1进程)
                + [2.1.1进程的概念](#2.1.1进程的概念)
                + [2.1.2进程创建](#2.1.2进程创建)
                + [2.1.3进程终止](#2.1.3进程终止)
                + [2.1.4进程层次机构](#2.1.4进程层次机构)
                + [2.1.5进程的状态](#2.1.5进程的状态)
                + [2.1.6进程的实现](#2.1.6进程的实现)
                + [2.1.7进程间通信(IPC)](#2.1.7进程间通信(ipc))
        - [2.2线程](#2.2线程)
                + [2.2.1线程介绍](#2.2.1线程介绍)
                + [2.2.2线程模型](#2.2.2线程模型)
                + [2.2.3线程实现](#2.2.3线程实现)
                + [2.2.4线程安全](#2.2.4线程安全)
        - [2.3协程](#2.3协程)
        - [2.4调度](#2.4调度)
                + [2.4.1什么时候需要调度](#2.4.1什么时候需要调度)
                + [2.4.2调度系统的目标](#2.4.2调度系统的目标)
                + [2.4.2常用的调度算法](#2.4.2常用的调度算法)
* [3.内存](#3.内存)
        - [3.1地址空间](#3.1地址空间)
        - [3.2空闲内存管理](#3.2空闲内存管理)
        - [3.3栈](#3.3栈)
        - [3.4堆](#3.4堆)
        - [3.5内存抖动](#3.5内存抖动)
        - [3.6虚拟内存](#3.6虚拟内存)
* [4.文件系统](#4.文件系统)
        - [4.1文件](#4.1文件)
        - [4.2文件结构](#4.2文件结构)
        - [4.3文件类型](#4.3文件类型)
        - [4.4文件系统实现和管理](#4.4文件系统实现和管理)
        - [4.5目录](#4.5目录)
        - [4.6.磁盘](#4.6.磁盘)
* [5.I/O](#5.i/o)
        - [5.1I/O设备](#5.1i/o设备)
* [6.死锁](#6.死锁)
        - [6.1介绍](#6.1介绍)
        - [6.2死锁产生的条件](#6.2死锁产生的条件)
        - [6.3解决死锁的方式](#6.3解决死锁的方式)
* [x.其他](#x.其他)

<!-- vim-markdown-toc -->

## 1.操作系统介绍

计算机的两种运行状态: `内核态(操作系统的运行状态)`, `用户态(其他软件的运行状态)`

### 1.1CPU

- 主要和内存交互，从内存中读指令
- 一个CPU的执行指令周期是cpu从内存中读取一条指令，然后解码并决定其类型和操作数
- 不同类型cpu的`指令集`不同，常用两种指令集
    1. `CISC(Complex Instruction Set Computers，复杂指令集)`
    2. `RISC(Reduced Instruction Set Computers，精简指令集)`
- `寄存器`，用来保存一些关键的临时变量和结果，几个比较通用的寄存器有:
    - `程序计数器(program counter)`,指示下一条从内存中提取的指令的地址
    - `堆栈指针(stack pointer)`,指向内存中当前栈的顶端
    - `程序状态字寄存器`，操作系统维护的跟踪当前系统的状态

### 1.2主存

- RAM
- ROM，非易失性
- EEPROM
- 闪存

`虚拟内存机制`：使期望的内存空间大于实际的物理存储空间，方法是将部分程序放到磁盘，将主存作为部分缓存，保存最频繁使用的部分程序。由内存管理单元来完成将这部分需要缓存的程序转换为相关的地址字节码。

### 1.3I/O设备

- 包含`设备控制器`和`设备`两部分
- `设备驱动程序`，需要安装到os，三种方式：
    1. unix: 内核和设备重新连接，重启系统
    2. windows: 操作系统设置入口，重启系统之后根据入口找驱动程序
    3. 操作系统在运行时候可以直接接收新的驱动程序并安装，`动态可装载的设备驱动程序`，如:usb, ieee1394

**实现输入输出的方式:**

- `忙等待`，用户调用-->内核程序转换-->设备驱动程序启动I/O循环-->完成工作将数据返回，缺点是一直占据CPU
- `中断`，用户调用-->内核程序转换-->设备驱动程序让设备完成工作时发生中断,然后立即返回

### 1.4文件

- 两种特殊文件：`块特殊文件(指可随机存取的块组成的设备)`和`字符特殊文件(打印机等接收输出字符流的设备)`

### 1.5操作系统结构

- `单体系统`，整个操作系统在内核态以单一程序运行，程序集合链接到一起形成单一的二进制文件,调用程序比较高效，但是也比较臃肿，且只要系统发生故障，所有的应用均不可用，包含主程序，服务程序，实体程序，还有额外的扩展，如unix中的`共享库`和windows中的`动态连接库`
- `分层系统`，使用分层来分隔不同的功能单元，每一层只与该层的上层和下层通信
- `微内核`，尽可能减少内核态的程序
- `客户-服务端系统`
- `虚拟机和内核`

## 2.进程,线程和协程

### 2.1进程

#### 2.1.1进程的概念

- 进程是一个实体，`执行中的程序`,每一个进程有自己的地址空间（`文本区域(text region)`，`数据区域(data region)`，`堆栈(stack region)`）
  - 文本区域：存储处理器执行的代码
  - 数据区域：存储变量和动态分配的内存
  - 堆栈区域：存储活动过程调用的指令和本地变量

#### 2.1.2进程创建

1. 方式一：系统初始化
2. 方式二：运行的程序执行创建进程的系统调用
3. 方式三：用户请求创建一个新的进程
4. 方式四：初始化一个批处理工作

#### 2.1.3进程终止

1. 正常退出(自愿退出, unix调用`exit`, windows调用`ExitProcess`)
2. 错误退出(自愿退出)
3. 严重错误(自愿退出)
4. 被其他进程杀死(非自愿退出, unix执行`kill`, windows调用`TerminateProcess`)

#### 2.1.4进程层次机构

- unix, 父进程，子进程和子进程的字进程构成一个进程组，
- windows，无进程层次的概念，类似的是父进程创建子进程的时候会得到一个特别的令牌--`句柄`，来控制子进程

#### 2.1.5进程的状态

- `运行态`, 需要占用cpu时间片
- `阻塞态`，不需要占用cpu时间片
- `就绪态`，除非某种外部事件发生，否则不运行

`调度程序`： 决定不同程序的优先执行顺序以及运行的时间。

#### 2.1.6进程的实现

操作系统维护一张`进程表`来储存所有运行的进程的关键信息。

*进程切换*（或上下文切换）就是`从正在运行的进程中收回处理器，用新的进程塞进处理器，同时切换虚拟内存空间`;
*线程切换*与进程切换的区别就是线程切换不会切换虚拟内存空间。

#### 2.1.7进程间通信(IPC)

1. 消息传递（`管道`，`FI    FO`，`消息队列(MQ)`）
2. 同步(`互斥量`，`条件变量`，`读写锁`，`文件和写记录锁`，`信号量`)
3. 共享内存(`匿名的`，`具名的`)
4. 远程过程调用(`RPC`)

### 2.2线程

#### 2.2.1线程介绍

- 轻量级线程，程序执行流的最小单位，创建速度是进程的10-100倍
- 可以并发执行
- 共享进程资源，所有的线程享有所属进程的共同地址空间

#### 2.2.2线程模型

`轻量的进程`，cpu上调度执行的实体，同一个进程中的线程共享地址空间，全局变量，打开的文件，账号信息等。

#### 2.2.3线程实现

1. 用户空间中实现, 内核不知道线程的存在，每个进程有其专用的`线程表`来跟踪进程中的线程
    - 优点：线程保存和调度都是本地过程，启动效率更高，不需要切换到内核，不需要上下文切换，调度快，效率高，还允许每个进程有自己的调度算法
    - 缺点：`阻塞调用问题`，`缺页故障问题`
2. 内核空间中实现，不需要运行时环境，每个进程中没有线程表，内核中有记录所有线程的线程表
    - 缺点：创建和销毁的开销比较大
3. 用户和内核空间中混合实现

#### 2.2.4线程安全

- 含义：本质是`内存安全`，即多线程访问时，无论调用方式或线程的顺序等，主程序中不需要做任何同步，获得的结果都是设想的正确行为，即为`线程安全`
- 保证方式
  - 无状态，即执行的作用范围只在它这条线程的局部变量中并且只能由正在运行的线程访问；
  - 加锁，对能够同时被多个线程访问和修改的数据加锁

### 2.3协程

- 微线程，或者用户级线程，是一个执行单元，自带CPU上下文
- 与线程的区别就是`线程是抢占式调用，协程是调度式调用(用户控制)`
- 没有线程的使用多CPU的能力

一个线程中的某个函数，可以在任何地方保存当前函数的一些临时变量等信息，然后切换到另外的一个函数。

### 2.4调度

- 调度程序和调度算法

#### 2.4.1什么时候需要调度

1. 创建一个新的进程的时候，决定是父进程还是子进程需要运行
2. 进程退出时候需要决定
3. 进程阻塞在I/O，信号量或者其他情况时候，需要选择其他进程运行
4. I/O中断发生的时候

#### 2.4.2调度系统的目标

- 给每个进程公平的cpu份额
- 策略强制执行：保证规定的策略被执行
- 平衡，保证系统的各个部分都忙碌
- 响应要相对迅速

#### 2.4.2常用的调度算法

- `FIFO`,先到先执行算法
- `最短作业优先算法`，当有若干个同等重要的作业时候，优先选择需要作业时间短的
- `最短剩余时间优先算法`，调度程序选择剩余运行之间最短的进程运行
- `轮询算法`，古老，公平，使用广泛，每个进程被分配一个`时间片`，这个时间段内进程允许运行。如果时间片没结束，进程运行完毕，则立即切换到下一个进程；如果时间片结束，进程没有完成，则cpu会被抢占并被分配给另外一个进程，`时间片太短，上下文切换会浪费效率，太长，会导致短请求长时间不能处理，一般设置为20-50ms较好`
- `优先级调度算法`
- `多级队列调度算法`

## 3.内存

### 3.1地址空间

- 类似于进程的概念，是对物理内存的一种抽象
- 是进程可以用来寻址内存的地址集，每个进程的地址空间相对独立，但是某些进程会希望共享

### 3.2空闲内存管理

**两种监控内存的方式：**

- `位图`，将内存分割成为几个字节到几千字节的分配单元
- `链表`，维护一个记录已分配内存和空闲内存段的链表，段会包含进程或者两个进程的空闲区域

### 3.3栈

- 连续的一块内存区域
- 用于存放本地变量，内部临时变量以及与上下文有关的内容
- 机器系统提供，有底层的支持，效率较高

### 3.4堆

- 存放不在栈里的数据，coder控制，容易产生`内存泄漏(Memory Leak)，内存的使用超过分配的最大值`[面试内存泄露问题](https://blog.csdn.net/zy_jibai/article/details/80957169)

### 3.5内存抖动

内存频繁的分配和回收导致卡顿，甚至会发生内存泄漏。

### 3.6虚拟内存

- 每个程序都有自己的地址空间，每个地址空间被划分为多个`页面`的块，每一个页面都是一块连续的地址
- 这些页被映射到物理内存

## 4.文件系统

### 4.1文件

- 提供一种对信息存储和读取的`抽象机制`
- `文件系统`对文件的构造，命名，访问，使用，保护，实现和管理机制进行控制，如：`fat-32, ntfs`

### 4.2文件结构

文件的构造方式：

1. `字节序列`，将文件看作无结构的字节序列，文件的任何含义只在用户程序中解释，`unix和windows使用`
2. `记录序列`，将文件看作固定长度记录的序列，每个记录内部都有其内部结构
3. `树`，将文件看作一棵记录树

### 4.3文件类型

1. 常规文件：`ascii文件`和`二进制文件`
2. 特殊文件：`字符特殊文件`，`块特殊文件`
    - 块设备：块特殊文件，相应的硬件可以一次性读取或者写入整个块
    - 字符设备：行为类似于管道或者串行端口，字节写入可能会在屏幕展示

### 4.4文件系统实现和管理

- `磁盘分区`：每个分区都有独立的文件系统，磁盘的0号分区称为`主引导记录(MBR)`，用来引导计算机。
- 同一台计算机使用多个不同的文件系统，unix通过`虚拟文件系统(vfs)`将多种文件系统整合，通过`POSIX`接口统一调用

**磁盘空间管理：**

1. `分段管理`
2. `分页管理`
3. 块管理方式，文件被分成一个个块，

### 4.5目录

- 将文件的ascii码的名称映射到定位数据所需的信息上

### 4.6.磁盘

**磁盘调度：**

磁盘访问延迟 = 队列时间 + 控制器时间 + `寻道时间(主要耗时)` + 旋转时间 + 传输时间

## 5.I/O

### 5.1I/O设备

- 操作系统控制所有的I/O设备，`发送命令`，`捕捉中断`，`接收错误`
- I/O可以指硬件设备，也可以指`硬件提供给软件的接口`

**分类：**

1. `块设备`，能存储固定块信息的设备，每个块有自己的物理地址，如`硬盘`，`光盘`等
    - 缺点：寻址较慢，因为每次要从头读取整个块
2. `字符设备`，以字符为单位发送或接收一个字符流
    - 不可寻址，也没有寻道操作

**设备控制器：**

- 处理cpu传入和穿出信号的系统
- 设备控制器从连接的设备处接收数据，然后将其首先存储到控制器内部的`特殊目的寄存器(仅为一项任务工作的寄存器)，即本地缓冲区`

## 6.死锁

### 6.1介绍

- `死锁`，两个进程独占性的访问某个资源，从而等待另外一个资源的访问结果，会导致两个进程阻塞，并且两个资源都不会释放各自的资源
- 死锁通常发生在`不可抢占资源(如磁盘)`中

### 6.2死锁产生的条件

- `互斥`，资源不可以被多个进程同时占用
- `保持和等待`，进程没有完成任务就一直等待
- `不可抢占`
- `循环等待`

### 6.3解决死锁的方式

1. `鸵鸟算法`，忽略死锁带来的影响，如果发生的频率较低的话
2. `死锁检测和恢复`，抢占，回滚，杀死进程恢复
3. `仔细分配资源避免死锁`，当个资源的银行家算法，核心是检查每个请求是否会使系统不安全
4. `破坏死锁的产生条件避免死锁`，资源不被进程独占，死锁肯定不会产生

## x.其他

os_Kernel的特征:

1. 并发，多应用并存
2. 共享，资源共享
3. 虚拟，多通道程序设计技术
4. 异步，程序执行异步

