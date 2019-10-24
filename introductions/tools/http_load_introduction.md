# http_load压测工具

<!-- TOC -->

- [http_load压测工具](#httpload%e5%8e%8b%e6%b5%8b%e5%b7%a5%e5%85%b7)
  - [1.介绍](#1%e4%bb%8b%e7%bb%8d)
  - [2.使用](#2%e4%bd%bf%e7%94%a8)
    - [2.1安装](#21%e5%ae%89%e8%a3%85)
    - [2.2命令](#22%e5%91%bd%e4%bb%a4)

<!-- /TOC -->

## 1.介绍

[参考文档](https://www.cnblogs.com/shijingjing07/p/6539179.html)

基于linux的web服务器性能测试工具，用于测试服务器的吞吐量和负载以及web页面的性能。

## 2.使用

### 2.1安装

```shell
wget http://www.acme.com/software/http_load/http_load-12mar2006.tar.gz
tar -xzvf http_load-12mar2006.tar.gz
make && make install
```

### 2.2命令

1. 创建一个包含要测的url或者域名的文件
2. 使用命令测试

```shell
# -parallel 简写-p ：含义是并发的用户进程数。
# -fetches 简写-f ：含义是总计的访问次数
# -rate 简写-p ：含义是每秒的访问频率
# -seconds简写-s ：含义是总计的访问时间

http_load -rate 5 -seconds 10 url.txt  # 每秒访问5次，持续10秒
```
