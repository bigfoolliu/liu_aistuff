# http_load压测工具

<!-- vim-markdown-toc Marked -->

* [1.介绍](#1.介绍)
* [2.使用](#2.使用)
        - [2.1安装](#2.1安装)
        - [2.2命令](#2.2命令)
        - [2.3结果解析](#2.3结果解析)

<!-- vim-markdown-toc -->

## 1.介绍

- [http_load使用详解](https://www.cnblogs.com/shijingjing07/p/6539179.html)
- 基于linux的web服务器性能测试工具，用于测试服务器的吞吐量和负载以及web页面的性能
- 只支持get方法，并且是乱序执行的

## 2.使用

### 2.1安装

```shell
wget http://www.acme.com/software/http_load/http_load-12mar2006.tar.gz
tar -xzvf http_load-12mar2006.tar.gz
make && make install
```

### 2.2命令

1. 创建一个包含要测的url或者域名的文件(注意文件中不能有多余的空行)
2. 使用命令测试

```shell
# -parallel 简写-p ：含义是并发的用户进程数。
# -fetches 简写-f ：含义是总计的访问次数
# -rate 简写-p ：含义是每秒的访问频率
# -seconds简写-s ：含义是总计的访问时间

http_load -rate 5 -seconds 10 url.txt  # 每秒访问5次，持续10秒
http_load -rate 5 -seconds 10 url.txt 2>2.log 1>1.log  # 每秒访问5次，持续10秒，将错误日志(2)输出到2.log，将结果(1)输出到1.log
http_load -parallel 1000 -fetches 1000 url.txt  # 模拟1000个用户，共访问1000次
```

### 2.3结果解析

```shell
# 3352个请求，最大并发进程数是10，10.0001秒内传输数据量为1.1732e+06字节
3352 fetches, 10 max parallel, 1.1732e+06 bytes, in 10.0001 seconds

# 每个连接平均传输数据量1.1732e+06/3352=350
350 mean bytes/connection
335.197 fetches/sec, 117319 bytes/sec

# 每个连接的平均响应时间为0.243539ms，最大和最小响应时间为1.158和0.114ms
msecs/connect: 0.243539 mean, 1.158 max, 0.114 min
msecs/first-response: 28.2572 mean, 238.049 max, 11.271 min

# 如果403的类型过多，那可能要注意是否系统遇到了瓶颈
HTTP response codes:
  code 200 -- 3352
```

