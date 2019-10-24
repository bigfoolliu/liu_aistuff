# RabbitMQ扫盲

<!-- TOC -->

- [RabbitMQ扫盲](#rabbitmq%e6%89%ab%e7%9b%b2)
  - [概念](#%e6%a6%82%e5%bf%b5)

<!-- /TOC -->

[介绍](http://www.belonk.com/c/rabbitmq_intro_helloworld.html)
[官网](https://www.rabbitmq.com/)

主要思想非常简单:它接受并转发消息。

## 概念

- `Broker`：中间件。接收和分发消息的应用，RabbitMQ Server就是Message Broker。
- `Virtual host`: 虚拟主机。出于多租户和安全因素设计的，把AMQP的基本组件划分到一个虚拟的分组中，类似于网络中的namespace概念。当多个不同的用户使用同一个RabbitMQ server提供的服务时，可以划分出多个vhost，每个用户在自己的vhost创建exchange／queue等。
- `Connection`: 连接。publisher／consumer和broker之间的TCP连接。断开连接的操作只会在client端进行，Broker不会断开连接，除非出现网络故障或broker服务出现问题。
- `Channel`: 渠道。如果每一次访问RabbitMQ都建立一个Connection，在消息量大的时候建立TCP Connection的开销将是巨大的，效率也较低。Channel是在connection内部建立的逻辑连接，如果应用程序支持多线程，通常每个thread创建单独的channel进行通讯，AMQP method包含了channel id帮助客户端和message broker识别channel，所以channel之间是完全隔离的。Channel作为轻量级的Connection极大减少了操作系统建立TCP connection的开销
- `Exchange`: 路由。message到达broker的第一站，根据分发规则，匹配查询表中的routing key，分发消息到queue中去。常用的类型有：direct (point-to-point), topic (publish-subscribe) and fanout (multicast)。
  - `direct`：bindingKey和routingKey进行精确匹配，适用于精确将消息发送给指定队列
  - `topic`：bindingKey和routingKey可以进行模糊匹配，通过使用通配符"*"和"#"分别来模糊匹配一个单词和多个单词；适用于将消息按照一定的规则发送到匹配的一个或多个队列
  - `fanout`：广播，这种交换器可以将消息广播给所有订阅的交换器
  - `header`：不常用
- `Queue`: 队列。消息最终被送到这里等待consumer取走。一个message可以被同时拷贝到多个queue中。
- `Binding`: 绑定。exchange和queue之间的虚拟连接，binding中可以包含routing key。Binding信息被保存到exchange中的查询表中，用于message的分发依据。
- `Producter`: 发送消息的程序是生产者。
- `Consumer`：通常为等待接收消息的应用程序  。注意，生产者、消费者和消息代理不需要处于同一台主机上，事实上，在大多数应用场景都是如此。
