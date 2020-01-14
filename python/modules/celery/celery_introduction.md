# celery使用

<!-- TOC -->

- [celery使用](#celery%e4%bd%bf%e7%94%a8)
  - [1.基本概念](#1%e5%9f%ba%e6%9c%ac%e6%a6%82%e5%bf%b5)
    - [1.1常见耗时任务](#11%e5%b8%b8%e8%a7%81%e8%80%97%e6%97%b6%e4%bb%bb%e5%8a%a1)
  - [2.Broker](#2broker)
    - [2.1RabbitMQ](#21rabbitmq)
    - [2.2Redis](#22redis)
  - [3.Backend](#3backend)
  - [a.参考资料](#a%e5%8f%82%e8%80%83%e8%b5%84%e6%96%99)

<!-- /TOC -->

## 1.基本概念

### 1.1常见耗时任务

- 发送邮件
- 图形处理
- 上传文件

## 2.Broker

用来存储消息的中间装置。

### 2.1RabbitMQ

- 功能完备，稳定的并且易于安装的broker. 它是生产环境中最优的选择
- [使用rabbitmq作为celery的broker](http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html#broker-rabbitmq)

### 2.2Redis

- 功能完备的broker可选项，但是其更可能因意外中断或者电源故障导致数据丢失的情况
- [使用redis作为celery的broker](http://docs.celeryproject.org/en/latest/getting-started/brokers/redis.html#broker-redis)

## 3.Backend

Celery需要将结果保存到某个地方

有几种保存的方案可选:

- SQLAlchemy
- Django ORM
- Memcached
- Redis
- RPC (RabbitMQ/AMQP)

## a.参考资料

- [celery初级教程(一)](https://blog.csdn.net/mbl114/article/details/78046694)
- [celery初级教程(二)](https://blog.csdn.net/mbl114/article/details/78046825)
- [celery初级教程(三)](https://blog.csdn.net/mbl114/article/details/78046888)
- [celery初级教程(四)](https://blog.csdn.net/mbl114/article/details/78046937)
- [celery初级教程(五)](https://blog.csdn.net/mbl114/article/details/78046961)
- [celery初级教程(六)](https://blog.csdn.net/mbl114/article/details/78047001)
- [celery初级教程(七)](https://blog.csdn.net/mbl114/article/details/78047032)
- [python之celery使用详解(一)](https://www.cnblogs.com/cwp-bg/p/8759638.html)
- [python之celery使用详解(二)](https://www.cnblogs.com/cwp-bg/p/10575688.html)
