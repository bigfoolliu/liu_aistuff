# mqtt介绍

<!-- vim-markdown-toc Marked -->

* [1.概述](#1.概述)
    - [1.1Publish/Subscribe System](#1.1publish/subscribe-system)
    - [1.2Messages](#1.2messages)
    - [1.3Topics](#1.3topics)
    - [1.4Broker](#1.4broker)
* [2.使用](#2.使用)
    - [2.1安装python模块](#2.1安装python模块)
    - [2.2Publish](#2.2publish)

<!-- vim-markdown-toc -->

## 1.概述

一个轻量级的"发布/订阅"机器对机器的互联网消息传递协议，专为受限设备和低带宽，高延迟或不可靠的网络设计。

- [官网](http://mqtt.org/)
- [介绍](https://randomnerdtutorials.com/what-is-mqtt-and-how-it-works/)
- [paho-mqtt使用](https://pypi.org/project/paho-mqtt/)

- Publish/Subscribe
- Messages
- Topics
- Broker

### 1.1Publish/Subscribe System

在发布和订阅系统中，设备可以发布关于主题的消息，或者可以订阅特定主题以接收消息。

### 1.2Messages

消息是想要在设备中进行传输的内容，可以是命令或者具体的数据。

### 1.3Topics

主题是您对传入消息注册兴趣的方式，或者您指定要将邮件发布到何处的方式。 主题用正斜杠分隔的字符串表示。每个正斜杠表示主题级别。这是一个关于如何在家庭办公室为灯创建主题的示例：home/office/lamp

  1. 设备以"home/office/lamp"主题发布(Publish)"on/off"消息
  2. 另一个设备订阅了(Subscribe)这个主题"home/office/lamp"
  3. 这个设备接收到"on"或"off"消息执行命令

### 1.4Broker

代理主要负责接收所有消息，过滤消息，确定谁对它们感兴趣，然后将消息发布到所有订阅的客户端。

有多种代理可以使用，可以使用安装在Raspberry Pi中的Mosquitto代理。或者可以使用云MQTT代理。

- [安装Mosquitto代理](https://randomnerdtutorials.com/how-to-install-mosquitto-broker-on-raspberry-pi/)

## 2.使用

### 2.1安装python模块

```sh
pip install paho-mqtt
```

### 2.2Publish

本机上测试发布功能就是把自己作为一个发送信息的人，当所有发送过该主题(Topic)的对象都会收到自己发送的消息。

订阅一个主题的消息,终端执行: "mosquitto_sub -t (topic_name)"

```python
import paho.mqtt.client as mqtt

MQTTHOST = "101.200.46.138"
MQTTPORT = 1883
mqtt_client1 = mqtt.Client(client_id="1", clean_session=True)
mqtt_client2 = mqtt.Client(client_id="2", clean_session=True)

# subscribe callback
def on_subscribe(client, user_data, mid, granted_qos):
    print("[INFO]Subscribe succeed.")

# publish callback
def on_publish(client, user_data, mid):
    print("[INFO]Publish succeed.")

# subscribe
def subscribe_topic(mqtt_client, topic):
    mqtt_client.on_subscribe = on_subscribe
    mqtt_client.subscribe()

# publish
def publish_topic(mqtt_client, topic):
    mqtt_client.on_publish = on_publish
    msg = ""
    mqtt_client.publish(topic, msg)

mqtt_client1.connect(MQTTHOST, MQTTPORT)
subscribe_topic(mqtt_client1, "test1/")
mqtt_client1.loop_forever()

mqtt_client2.connect(MQTTHOST, MQTTPORT)
publish_topic(mqtt_client, "test2/")
```
