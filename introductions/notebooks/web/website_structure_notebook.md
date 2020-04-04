# 大型网站架构核心原理和案例分析读书笔记

<!-- TOC -->

- [大型网站架构核心原理和案例分析读书笔记](#大型网站架构核心原理和案例分析读书笔记)
    - [1.大型网站架构演化](#1大型网站架构演化)
    - [2.大型网站架构模式](#2大型网站架构模式)
        - [2.1网站架构模式](#21网站架构模式)
        - [2.2新浪微博架构分析](#22新浪微博架构分析)
    - [3.大型网站核心架构要素](#3大型网站核心架构要素)
        - [3.1性能](#31性能)
        - [3.2可用性](#32可用性)
        - [3.3伸缩性](#33伸缩性)
        - [3.4扩展性](#34扩展性)
        - [3.5安全性](#35安全性)
    - [4.瞬时响应:网站的高性能架构](#4瞬时响应网站的高性能架构)
        - [4.1性能测试指标](#41性能测试指标)
        - [4.2前端性能优化](#42前端性能优化)
        - [4.3应用服务器性能优化](#43应用服务器性能优化)
        - [4.4存储性能优化](#44存储性能优化)
    - [5.万无一失：网站的高可用架构](#5万无一失网站的高可用架构)
        - [5.1网站的可用性度量与考核](#51网站的可用性度量与考核)
        - [5.2高可用的网站架构](#52高可用的网站架构)
        - [5.3高可用的应用](#53高可用的应用)
        - [5.4高可用的服务](#54高可用的服务)
        - [5.5高可用的数据](#55高可用的数据)
        - [5.6高可用网站的软件质量保证](#56高可用网站的软件质量保证)
        - [5.7网站运行监控](#57网站运行监控)
    - [6.永无止境：网站的伸缩性架构](#6永无止境网站的伸缩性架构)
        - [6.1网站架构的伸缩性设计](#61网站架构的伸缩性设计)
        - [6.2应用服务器集群的伸缩性设计](#62应用服务器集群的伸缩性设计)
        - [6.3分布式缓存集群的伸缩性设计](#63分布式缓存集群的伸缩性设计)
        - [6.4数据存储服务器集群的伸缩性设计](#64数据存储服务器集群的伸缩性设计)
    - [7.随需应变：网站的可扩展架构](#7随需应变网站的可扩展架构)
        - [7.1构建可扩展的网站架构](#71构建可扩展的网站架构)
        - [7.2利用分布式消息队列降低系统耦合性](#72利用分布式消息队列降低系统耦合性)
    - [8.固若金汤：网站的安全架构](#8固若金汤网站的安全架构)
        - [8.1网站应用攻击和防御](#81网站应用攻击和防御)
        - [8.2信息加密技术及密钥安全管理](#82信息加密技术及密钥安全管理)
        - [8.3信息过滤与反垃圾](#83信息过滤与反垃圾)
    - [附录](#附录)

<!-- /TOC -->

## 1.大型网站架构演化

大型网站特点：

- `高并发，大流量`
- `高可用`
- `海量数据`
- `用户分布广泛，网络复杂`
- `安全环境恶劣`
- `需求快速变更，发布频繁`
- `渐进式发展`

基本发展路径：

1. 应用程序，数据库，文件部署在同一台服务器上
2. 应用服务和数据服务分离，使用三台服务器：`应用服务器(更快的cpu)`，`文件服务器(更大的硬盘)`，`数据库服务器(快速磁盘检索和数据缓存)`
3. 增加多台缓存服务器，(缓存在应用服务器的`本地缓存`和缓存在专门的分布式缓存服务器的`远程缓存`)
4. 构建应用服务器集群，改善网站并发能力，同时需要部署`负载均衡`服务器来进行调度
5. 利用数据库的`主从热备`功能，配置主从数据库服务器，将一台数据库的数据更新到另一台数据库上，实现`数据库读写分离`
6. 使用`反向代理`和`CDN加速`网站响应，其基本原理都是缓存，区别在于CDN部署在网络提供商的机房，用户请求时可以从距离自己最近的网络提供商机房获取数据，反向代理则部署在网站的中心机房
7. 使用`分布式文件系统`和`分布式数据库系统`
8. 使用NoSQL和搜索引擎
9. `业务拆分`，将网站拆分为不同的应用，每个应用独立部署维护，应用之间通过一个超链接建立关系
10. `分布式服务`，将共用业务提取出来，独立部署，通过分布式服务调用共用业务服务完成具体业务操作

## 2.大型网站架构模式

`架构模式`即架构通常解决问题的方案。

### 2.1网站架构模式

1. 分层，将大的软件系统横向切分为不同的部分
2. 分割，将不同的功能和服务分割开为`高内聚低耦合`的模块单元
3. 分布式，分布式方案包括：`分布式应用和服务`，`分布式静态资源`，`分布式数据和存储`，`分布式计算`，`分布式配置`，`分布式锁`，`分布式文件`等
4. 集群，多台服务器部署相同应用构成一个集群，通过负载均衡设备共同对外提供服务
5. 缓存，`CDN`，`反向代理`，`本地缓存`，`分布式缓存`，使用缓存的前提条件：1.数据访问热点不均衡；2.数据在某个时间段内有效，不会很快过期
6. 异步，业务操作分成多个阶段，每个阶段之间通过数据共享的方式异步执行，单一服务器可通过多线程`共享内存队列`的方式实现；分布式系统中多个服务器集群通过`分布式消息队列`实现异步，可以`提高系统可用性`，`加快网站响应速度`，`消除并发访问高峰`
7. 冗余，服务器冗余运行，数据冗余备份(数据库定期存档`冷备份`，数据库主从分离，实时同步`热备份`)
8. 自动化，`自动化代码管理`，`自动化测试`，`自动化安全检测`，`自动化部署`，`自动化监控`, `自动化监控`，`自动化报警`,`自动化失效转移`，`自动化失效恢复`，`自动化降级`，`自动化分配资源`
9. 安全，密码和手机验证码身份验证，网络通信加密

### 2.2新浪微博架构分析

三个层次：

1. 底层为`基础服务层`，提供数据库，缓存，存储，搜索等数据服务
2. 中间层为`平台服务层`和`应用服务层`，维护微博，关系和用户，分割成独立的服务模块，用户，计数，图片池等
3. 上层为`API层`和`业务层`，客户端(web网站)和第三方应用，通过API调用集成到整个系统

其他相关技术：

- `异步推拉结合模式`，用户发表微博后系统将微博写入消息队列后立即返回，消息队列消费者任务将微博推送给所有当前在线粉丝列表，非在线用户登录之后再根据列表拉取订阅列表
- `多级缓存策略`，热门微博和明星用户微博缓存到所有的微博服务器，在线用户的微博和近期微缓存在分布式缓存集群中，`刷微博`几乎都是缓存访问操作

## 3.大型网站核心架构要素

需要考虑要素：

1. 性能
2. 可用性
3. 伸缩性
4. 扩展性
5. 安全性

### 3.1性能

- 浏览器端，`浏览器缓存`，`页面压缩`，`合理布局页面`，`减少cookie传输`等
- 应用服务器端，`服务器本地缓存`，`分布式缓存`，`异步操作`，`集群`等
- 代码层面，`多线程`，`内存管理`等
- 数据库服务器端，`索引`，`缓存`，`SQL优化`等

### 3.2可用性

即保证网站能够7x24可用。

- `冗余设计`，应用部署在多台服务器上同时提供访问；数据存储在多台服务器上互相备份
- 应用服务器，多台组成集群通过负载均衡设备组成一个集群对外服务，其中一台宕机只需把请求切换到其他一台即可,前提是`应用服务器上不能保存请求的会话信息，否则会话丢失，转发到其他服务器也无法完成业务处理`
- 存储服务器，多机器互相备份，可以进行数据恢复
- 其他：`预发布验证`，`自动化测试`，`自动化发布`，`灰度发布`等

### 3.3伸缩性

衡量架构伸缩性的标准为`是否可以用多台服务器构成集群，是否容易向集群添加新的服务器，加入的新机器是否能提供和原服务器无差别的服务，集群中容纳的总服务器数量是否有限制等`。

- 应用服务器集群，只要**服务器上不保存数据，所有服务器对等**，通过合适的负载均衡设备即可
- 缓存服务器集群，新加入的服务器会导致缓存路由失效
- 数据库层面，关系数据库可以`主从热备`，但难以做到大规模集群的可伸缩性，需从数据库层面外实现，通过路由分区等手段将部署有多个数据库的服务器组成一个集群；Nosql数据库因为先天就是为海量数据而生，因此对伸缩性的支持较好

### 3.4扩展性

衡量网站扩展性的标准是`在网站增加新的业务时，是否可以实现对现有产品透明无影响，不同产品之间是否很少耦合`。

- `事件驱动架构`，利用`消息队列`实现，将用户请求和其他业务事件构造成消息发布到消息队列，将消息的处理者作为消费者从消息队列中获取消息进行处理，将消息的产生和处理分离
- `分布式事务`，将`业务和可复用服务分离`开来，通过分布式服务框架调用，新增产品可以调用可复用的服务实现自身业务逻辑，而对现有产品没有影响

### 3.5安全性

针对现由和潜在的各种攻击手段原有应对策略。

## 4.瞬时响应:网站的高性能架构

### 4.1性能测试指标

网站性能的衡量指标主要有：`响应时间`，`并发数`，`吞吐量`，`性能计数器`等。

- 响应时间：测试时候可以通过一个请求执行10000次数得到总响应时间之和，然后平均得到单次响应时间。
- 并发数：系统能够同时处理的请求数，测试时通过多线程模拟并发用户，但不是启动多线程然后不停发送请求，而是在两次请求之间加入一个随机等待时间(`思考时间`)。
- 吞吐量：单位时间内内系统处理的请求数量。
- 性能计数器：描述服务器或操作系统性能的一些数据指标，包括`system load（系统负载）`,`对象`，`线程数`，`内存使用`，`CPU使用`，`磁盘`，`网络IO`等。

性能测试方法：

1. 性能测试，以设计性能指标为预期目标，对系统不断加压，验证系统在资源可接受的范围
2. 负载测试，对系统不断增加并发至系统的某项或多项性能指标达到安全临界值
3. 压力测试，超过安全负载的情况下，直到系统崩溃或不能再处理任何请求
4. 稳定性测试，特定软硬件以及网络环境下，给系统加载一定的业务压力，是系统运行一段较长时间

性能优化策略：

- 性能分析，检查请求处理的各个环节的日志，分析哪个环节响应时间不合理，检查监控数据，分析影响性能的主要因素是内存，磁盘，网络，cpu，是代码问题还是架构设计不合理，或者系统资源不足。
- 性能优化，根据网站分层架构，分为`前端性能优化`，`应用服务器性能优化`，`存储服务器性能优化`。

### 4.2前端性能优化

- 减少http请求，主要手段是`合并css`，`合并js`，`合并图片`
- 使用浏览器缓存，通过设置HTTP头中的`Cache-Control`和`Expires`属性，设置缓存时间为数天甚至数月
- 启用压缩，文本文件使用GZip压缩
- CSS放在页面最上方，JS放在页面最下方
- 减少cookie传输，太大的cookie会影响数据传输，静态资源使用独立域名访问
- CDN加速，本质还是缓存
- 反向代理

### 4.3应用服务器性能优化

- 缓存
- 集群
- 异步

缓存：

- 本质是一个内存Hash表
- 主要用来存放读写比较高很少变化的数据
- 应用读取数据时，先到缓存读取，读不到的时候访问数据库，并将数据写入缓存
- 缓存数据的读写比应该在2:1以上才有意义，即写入一次缓存之前，数据被读取两次
- 缓存需要设置失效时间，超过失效时间则从数据库中重新读取，因此需要容忍一段时间的`数据不一致`
- 需要预防`缓存雪崩`，即缓存服务器突然崩溃导致数据库访问剧增而崩溃，可以通过`缓存热备`等手段避免
- 分布式缓存：`Memcached`

异步操作：

- 使用消息队列，将短时间内高并发产生的事务消息存储在消息队列中
- 数据写入消息队列之后立即返回，但后续操作可能失败，因此需要适当修改业务流程进行配合，不能立即返回成功，后续可通过邮件或者sms消息通知用户订单成功

代码优化：

1. `多线程`
   - 启动线程数量应该与CPU内核数量成正比，与IO阻塞时间成反比
   - 如果任务都是CPU计算型任务，线程数不应该超过CPU内核数量，否则再多CPU也来不及调度
   - 需要解决`线程安全问题`(多线程并发对某个资源进行修改导致数据混乱)：
     - `将对象设计为无状态对象`，即对象本身不存储状态信息
     - `使用局部对象`，即在方法内创建对象
     - `并发访问资源时候使用锁`
2. `资源复用`
   - 尽量减少资源开销很大的系统资源的创建和销毁,如`数据库连接`，`网络通信过程`，`线程`，`复杂对象`等
   - 资源复用主要的两种方式
    1. `单例模式`
    2. `对象池`，包括`线程池`，`连接池`(减少频繁的连接数据库，数据库连接对象创建好了之后就将连接对象放入对象池容器，要连接的时候就从中取一个空闲的连接)
3. `数据结构`，不同场景使用恰当的数据结构，灵活组合各种数据结构改善数据读写和可计算性
4. `垃圾回收`，堆栈的更快速的释放

### 4.4存储性能优化

1. 使用大容量的SSD
2. `B+数`，改善数据访问特性，增删改查之后依然有序，传统关系数据库的做法就是B+树；NoSQL则是使用`LSM树`
3. `RAID`(廉价磁盘冗余阵列，实现数据在磁盘上的并发读写和数据备份)和`HDFS`(Hadoop分布式文件系统，系统在整个存储集群的多台服务器上进行数据并发读写和备份)

## 5.万无一失：网站的高可用架构

网站`可用性`描述网站可以有效访问的特性。

### 5.1网站的可用性度量与考核

可用性：99.99%等

### 5.2高可用的网站架构

一个典型的网站基本分层模型(各层具有相互独立性)：

- `应用层`
  - 负责具体的业务逻辑处理，如贴吧，百科等，也叫`业务逻辑层`
  - 通常面对高并发请求，通过负载均衡设备组成集群对外服务
- `服务层`
  - 提供可以复用的服务，如账户服务，登录服务等
  - 也是集群方式实现高可用，只是服务器被应用层通过分布式服务调用框架访问
- `数据层`
  - 负责数据的存储和访问，如文件服务，缓存服务，搜索服务等
  - 需要保证服务器宕机数据不丢失，需要将数据写入时候进行数据同步复制，将数据写入多台服务器，服务器宕机应用程序将访问切换到有备份数据的服务器

### 5.3高可用的应用

1. 应用服务器`不保存请求的状态`，所有服务器都是对等的
2. 使用`负载均衡`进行无状态服务的失效转移，当某台应用服务器宕机了，负载均衡服务器通过`心跳`检测机制发现该服务器失效，将其从服务器列表删除，将请求转移到另一台
3. 应用服务器集群的Session管理
   - `Session复制`,在集群中的几台服务器之间同步session对象，适合集群规模比较小的情况
   - `Session绑定`
   - `利用cookie记录session`
   - `Session服务器`，独立部署的Session服务器同一管理所有Session，应用服务器每次读写Session时候都访问Session服务器

### 5.4高可用的服务

可复用的服务模块提供基础公共服务。

1. `分级管理`
   - 核心应用和服务使用更好的硬件
   - 高优先级的部署在不同的物理机，低优先级的通过启动不同的线程或者虚拟机进行隔离，避免`故障连锁反应`
2. `超时设置`
   - 应用中设置服务调用的超时时间，超时就选择重试或者将请求转移到其他服务器上
3. `异步调用`
   - 对于获取用户信息这类调用使用异步会延长响应时间，得不偿失
   - 对于必须确认服务调用成功之后才能下一步操作的应用也不适合异步调用
4. `服务降级`
   - 当服务因高并发性能下降而避免宕机，保证核心应用和功能正常采取的措施,两种方式：
   - `拒绝服务`，拒绝低优先级的调用，确保核心功能正常
   - `关闭功能`，关闭部分不重要的功能，节约开销
5. `幂等性设计`
   - 服务处理成功，但是因为网络故障应用没有收到成功的响应，应用重新请求导致`服务重复调用`
   - 需要`服务层保证服务调用一次和调用多次的结果相同`

### 5.5高可用的数据

- 服务器宕机，数据访问不能随意迁移到集群其他的主机
- 保证数据存储高可用使用方式为：
  - `数据备份`，冷备份是定期备份，不能保证数据一致性，`热备份`（`异步热备方式`和`同步热备方式`）
  - `失效转移机制`（当一个数据副本不可用时候，可以快速访问数据的其他副本）
- 高可用数据包括：`数据持久性`，`数据可访问性`，`数据一致性`

### 5.6高可用网站的软件质量保证

1. 网站发布，通常使用发布脚本来发布，每次关闭集群中的一小部分服务器，并在发布后可以立即使用
2. 自动化测试
3. 预发布验证，预发布服务器和线上服务器唯一的区别就是没有配置在负载均衡服务器上，外部的用户不能访问
4. 代码控制
5. 自动化发布（可以周四作为发布日）
6. 灰度发布，将集群服务器分成若干部分，每天只发布一部分服务器，观察运行情况，没有问题则继续

### 5.7网站运行监控

1. 监控数据采集
   - 用户行为日志收集（服务器端日志收集，客户端浏览器日志收集）
   - 服务器性能监控（系统load，内存占用，磁盘IO，网络IO）
   - 运行数据报告(缓冲命中率，平均响应延迟时间，待处理任务数等)
2. 监控管理
   - 系统报警（某些指标超过阈值报告，邮件，语音，短信等）
   - 失效转移（访问失败进行失效转移或者发现故障时主动通知应用）
   - 自动优雅降级（应付突然爆发的访问主动关闭部分功能）

## 6.永无止境：网站的伸缩性架构

即仅仅通过改变部署的服务器的数量就可以扩大或者缩小网站的服务处理能力。

### 6.1网站架构的伸缩性设计

伸缩性设计种类：

1. `根据功能进行物理分离实现伸缩`，不同的服务器部署不同的服务
2. `单一功能通过集群实现伸缩`，集群内的多台服务器部署相同的服务，提供相同的功能

### 6.2应用服务器集群的伸缩性设计

实现负载均衡的几种方式：

1. `HTTP重定向负载均衡`，使用重定向服务器，优点是简单，缺点是浏览器需要两次请求服务器才能完成一次访问，性能较差
2. `DNS域名解析负载均衡`，优点是将负载均衡的工作转交了DNS,省掉了网站管理维护负载均衡服务器的麻烦，同时许多DNS支持基于地理位置的域名解析，将域名解析成距离用户最近的一个服务器地址，可加快用户访问速度，改善性能；缺点是目前的的DNS解析是多级解析，可能会将域名解析到即使已经下线的服务器，导致用户访问失败
3. `反向代理负载均衡`，优点是和反向代理服务器功能集成到一起，部署简单，缺点是反向代理服务器作为请求和响应的中转站，其性能可能会是瓶颈
4. `IP负载均衡`，网络层通过修改请求目标地址进行负载均衡，优点是有较好的处理性能，缺点是集群得的最大响应的吞吐量将受制于负载均衡服务器的网卡带宽、
5. `数据链路层负载均衡`，在通信协议的数据链路层修改mac地址进行负载均衡

常用负载均衡算法：

1. `轮询`，所有请求依次分发到每台应用服务器
2. `加权轮询`，根据应用服务器的性能加权轮询
3. `随机`，请求随机分配到每个应用服务器
4. `最少连接`，记录每个应用服务器的连接数量，将新的请求分发到最少连接的服务器
5. `源地址散列`，根据请求来源的IP地址进行HASH计算，得到应用服务器

### 6.3分布式缓存集群的伸缩性设计

`不同缓存服务器中缓存的数据各不相同，不能使用简单的负载均衡实现`，新加入缓存服务器后应使整个缓存服务器集群中已经缓存的数据尽可能的被访问到。

通过`路由算法`来决定来访问哪台服务器。

`分布式缓存的一致性Hash算法`：

通过一个叫做`一致性Hash环`(通常使用二叉查找树实现)的数据结构实现Key到缓存服务器的Hash映射。

### 6.4数据存储服务器集群的伸缩性设计

关系型数据库集群的伸缩性设计：

1. 数据库主从读写分离
2. 不同业务数据表部署在不同的数据库集群上，即`数据分库`
3. 目前支持数据分片的分布式关系型数据库产品有：`Amoeba`和`Cobar`

NoSQL数据库的伸缩性设计：

主要产品有`Apache HBase`，为可伸缩海量数据存储设计。

## 7.随需应变：网站的可扩展架构

### 7.1构建可扩展的网站架构

- 降低各个系统之间的耦合度
- 提高模块的复用性
- 模块分布式部署之后具体聚合方式主要有`分布式消息队列`和`分布式服务`

### 7.2利用分布式消息队列降低系统耦合性

`事件驱动架构`：在低耦合的模块之间传输事件消息，来保持模块的松散耦合。

分布式消息队列：

- Apache ActiveMQ
- 使用MySQL也可以

## 8.固若金汤：网站的安全架构

### 8.1网站应用攻击和防御

1. `XSS攻击`(cross site script, 跨站点脚本攻击)
   - 通过篡改网页，注入恶意HTML脚本，在用户浏览网页时控制用户浏览器进行恶意操作
   - 预防手段主要有：`消毒`（即对一些危险字符转义），`HttpOnly`（浏览器禁止页面JS访问带有HttpOnly属性的Cookie）
2. `注入攻击`
   - `SQL注入`，在请求中注入恶意SQL命令，服务器用请求参数构造数据库SQL命令时候，恶意SQL被一起构造在数据库中执行
     - 预防手段主要有：
     - `消毒`（通过正则匹配，过滤掉请求中可能注入的SQL）
     - `参数绑定`（使用预编译的手段绑定参数）
   - `OS注入`
3. `CSRF攻击`（跨站请求伪造）
   - 利用跨站请求，在用户不知情的情况下以用户的身份伪造请求，核心是利用浏览器的Cookie和Session策略
   - 预防手段主要有：
   - `表单Token`（通过在请求参数中添加随机数构造Token,正常响应页面会携带Token）
   - `验证码`，请求提交时需要用户输入验证码
   - `Referer Check`,请求头的Referer记录着请求来源，可以通过检查请求来源验证其是否合法
4. `Error Code`
   - 错误回显，即浏览器默认将服务端未处理的异常堆栈信息直接返回至客户端浏览器，可以故意制造非法输入得到异常信息，从而找到漏洞
5. `HTML注释`
6. `文件上传`
   - 有可能上传的是可执行程序
   - 预防手段：`设置上传文件白名单`，`只允许上传可靠的文件类型`等
7. `路径遍历`
   - 在请求的url中使用相对路径，遍历系统未开放的目录和文件
   - 预防手段：`将js，css资源文件部署在独立服务器`，`使用独立域名`，`动态参数不包含文件路径信息`等

开源Web应用防火墙：`ModSecurity`,可以探测攻击并保护Web应用程序。

### 8.2信息加密技术及密钥安全管理

几种加密方式：

1. 单向散列加密
2. 对称加密
3. 非对称加密

通常密钥是以明文的方式被保存。可以通过几种方式来改善其安全性：

1. 将密钥和算法放在独立的服务器，甚至做成一个专用的硬件设施，对外提供加密和解密服务
2. 将加解密算法放在应用系统中，密钥则放在独立服务器中

### 8.3信息过滤与反垃圾

1. 文本匹配，网站维护一份敏感词列表（`正则匹配`，`Trie树`，`双数组Trie树`，`多级Hash表`）
2. 分类算法，`贝叶斯算法`等
3. 黑名单，将被报告的垃圾邮箱地址放入黑名单

## 附录

大型网站架构技术一览：

前端技术：

1. 分布式消息
2. 分布式服务
3. 分布式缓存
4. 分布式配置

前端架构技术：

1. 浏览器优化，页面缓存，合并HTTP请求，使用页面压缩等
2. CDN内容分发网络
3. 动静分离，静态资源独立部署
4. 图片服务
5. 反向代理
6. DNS

应用层架构技术：

1. 开发框架
2. 页面渲染
3. 负载均衡
4. Session管理
5. 动态页面静态化
6. 业务拆分
7. 虚拟化服务器

服务层架构：

1. 分布式消息
2. 分布式服务
3. 分布式缓存
4. 分布式配置别1