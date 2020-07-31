# GStreamer使用介绍

<!-- vim-markdown-toc Marked -->

* [1.概念](#1.概念)
        - [1.1管道pipeline](#1.1管道pipeline)
        - [1.2元素element](#1.2元素element)
        - [1.3属性](#1.3属性)
        - [1.4插头pad](#1.4插头pad)
        - [1.5cap](#1.5cap)
        - [1.6bin](#1.6bin)
        - [1.7ghost pad](#1.7ghost-pad)
* [2.常用命令](#2.常用命令)
* [3.示例](#3.示例)

<!-- vim-markdown-toc -->

## 1.概念

Gstreamer是一款功能强大、易扩展、可复用的、跨平台的用流媒体应用程序的框架，该框架大致包含了`应用层接口`、`主核心框架`以及`扩展插件`三个部分。
主核心框架就是流媒体的实际运行框架，其包含了媒体处理、内部消息处理、数据的网络传输、以及插件系统实现的功能等；主核心框架又包含了一系列的子模块称之为`element`，每个element完成一项单一的功能，通过`Pipeline`把其串联起来实现一条媒体流的实现。

参考资料：

- [big doc gstreamer基础介绍](https://thebigdoc.readthedocs.io/en/latest/gstreamer/gst-concept.html)

### 1.1管道pipeline

gst-launch-1.0用来运行管道，将元素一个个串起来。这里的管道符号为`!`

### 1.2元素element

对输入的数据做处理的黑盒。

常见元素：

`filesrc`：从本地加载文件
`decodebin`：从filesrc解码，会自动检测文件类型并在后台构建元素来解码
`audioconvert`：将声音文件中的各种不同的信息进行转换
`alsasink`：将音频使用`ALSA`传递给声卡

### 1.3属性

`location`：指定具体的文件路径

### 1.4插头pad

- 每一个元素的虚拟的供数据流入流出的插头
- 绝大多数元素有两个pad，输入pad(`sink`)和输出pad(`src`)
- 最左边的元素有1个src来提供信息，最后一个元素只接收信息

### 1.5cap

- 标识每一个元素可以接收的信息的范围

### 1.6bin

- 便捷方式，可以将多个元素放进一个容器中
- bin就像是一个组合的元素

### 1.7ghost pad

- 对于bin的插头

## 2.常用命令

```shell
# 查看有哪些元素可以使用
gst-inspect-1.0

# 查看某一个元素的具体信息
gst-inspect-1.0 filesrc
```

## 3.示例

```shell
# 直接播放音乐
gst-launch-1.0 filesrc location=越单纯越幸福.mp3 ! decodebin ! audioconvert ! alsasink
```
