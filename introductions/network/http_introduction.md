# http

<!-- vim-markdown-toc Marked -->

* [1.概述](#1.概述)
    - [1.1http基础](#1.1http基础)
    - [1.2GET和POST](#1.2get和post)
    - [1.3Keep-Alive模式](#1.3keep-alive模式)
    - [1.5同源策略及跨域解决方案](#1.5同源策略及跨域解决方案)
        + [1.5.1同源策略](#1.5.1同源策略)
        + [1.5.2跨域限制](#1.5.2跨域限制)
    - [1.6http1.0,http1.1与http2.0之间的区别](#1.6http1.0,http1.1与http2.0之间的区别)
    - [1.7HTTP优化](#1.7http优化)
    - [1.8SSL连接](#1.8ssl连接)
* [2.HTTPS](#2.https)
    - [2.1https介绍](#2.1https介绍)
    - [2.2SSL证书](#2.2ssl证书)

<!-- vim-markdown-toc -->

## 1.概述

- [github后端面试网络相关](https://github.com/yongxinz/back-end-interview/tree/master/%E7%BD%91%E7%BB%9C#1%e4%b8%89%e6%ac%a1%e6%8f%a1%e6%89%8b%e5%92%8c%e5%9b%9b%e6%ac%a1%e6%8c%a5%e6%89%8b)
- [100个网络基础知识普及](https://blog.csdn.net/devcloud/article/details/101199255)

### 1.1http基础

- 基于TCP/IP，应用层协议，默认端口为`80`
- `无状态`(对于交互式场景没有记忆)，`无连接`(限制每次连接只处理一个请求，且请求完成断开连接)

**一次完整的HTTP请求的七个步骤：**

1. 建立TCP连接
2. web浏览器向服务器发出请求行
3. web浏览器发送请求头
4. web服务器应答
5. web服务器发送应答头
6. web服务器向浏览器发送数据
7. web服务器关闭TCP连接

### 1.2GET和POST

**条件GET：**

- 如果客户端重新请求的这段时间内，服务端的页面没有改变，则应该使用浏览器缓存的数据。
- 服务端根据该字段的时间，如果当前的响应内容没有改变，则返回`304 Not Modified`,客户端使用缓存内容

根据客户端的请求头如下：

```text
If-Modified-Since:Thu, 4 Feb 2010 20:39:13 GMT
```

**GET和POST的区别：**

- [知乎:GET和POST的区别](https://www.zhihu.com/question/31640769?rf=37401322)

1. get传送的数据量较小，受url限制不能大于2Kb，但是效率较高；post传送默认不受限制
2. get因为url可见，安全性低；post安全性较高
3. get只能支持ASCII字符，传送中文可能会乱码；post支持标准字符集，可以正确传送中文
4. get请求会保留在浏览器的历史记录中，post不会

### 1.3Keep-Alive模式

非该模式下的时候，每一次请求都要建立一次连接；该模式(持久连接)下，可以使连接持续有效，避免下次请求的时候需要重新建立连接。

### 1.5同源策略及跨域解决方案

- [同源策略及跨域解决方案](https://www.cnblogs.com/rain-chenwei/p/9520240.html)
- [浏览器同源策略及跨域的解决方法](https://www.cnblogs.com/laixiangran/p/9064769.html)

#### 1.5.1同源策略

- web构建于同源策略，是最基本最核心的浏览器安全功能，即执行web页面脚本的时候会检查脚本是属于哪个页面(协议，域名，端口)
- 分类:`DOM同源策略`，`XMLHttpRequest同源策略`

#### 1.5.2跨域限制

- 浏览器同源策略的存在导致跨域限制，为了保证用户网络安全

**跨域问题解决**：

1. CORS(跨域资源共享)，W3C的标准，基本思想是 `使用自定义的HTTP头部决定浏览器与服务器沟通`，简单请求需要origin字段
   1. 优点：通信与同源ajax相同，代码相同易维护
   2. 缺点：存在一定的兼容性问题，非简单请求首次请求需要两次请求
2. JSONP跨域，基本思想是`script标签不受浏览器同源策略影响`
   1. 优点：最流行，使用方便，没有兼容性问题
   2. 缺点：只适用GET方法，安全性有一定问题
3. 图像Ping跨域，基本思想是`img标签不受同源策略影响`
   1. 优点：实现跟踪用户点击
   2. 缺点：只适用GET，只能浏览器与服务器的单向通信
4. 服务器代理，基本思想是`服务器不存在跨域问题`
   1. document.domain跨域
   2. window.name跨域
   3. location.hash跨域
   4. postMessage跨域

### 1.6http1.0,http1.1与http2.0之间的区别

- [http1.0,http1.1与http2.0之间的区别](https://blog.csdn.net/qq_36183935/article/details/81156225)
- [http1.0,http1.1与http2.0之间的区别2](https://blog.csdn.net/linsongbin1/article/details/54980801)
- [http2.0新特性总结](https://www.jianshu.com/p/67c541a421f9)

| 协议 | 特点 |
| ---- | --- |
| http1.0 | 1、无状态；<br>2、无连接 |
| http1.1 | 1、持久连接；<br>2、请求管道化，响应必须按照请求的顺序；<br>3、增加缓存处理；<br>4、增加host字段，支持断点续传 |
| http2.0 | 1、二进制分帧(对数据标识，不会乱序)；<br>2、多路复用(一个tcp连接建立无数个http请求)；<br>3、请求头头部压缩减少带宽消耗；<br>4、服务器可以在无明确请求的时候推送数据到客户端 |

### 1.7HTTP优化

1. `TCP复用`，tcp复用指多个客户端的http请求复用到一个服务器TCP连接上（负载均衡设备的功能）；http复用指一个客户端的多个http请求通过一个tcp连接处理（http 1.1协议支持）
2. `内容缓存`，将经常用的内容缓存
3. `压缩`，将文本数据进行压缩，减少带宽
4. `SSL加密`，使用ssl协议对HTTP协议加密，在通道内加密并加速
5. `TCP缓冲`，该技术可以提高服务器端响应时间，减少由于数据链路问题造成的服务器负担

### 1.8SSL连接

- [SSL连接了解](https://blog.csdn.net/wang_gongzi/article/details/82853060)

**介绍：**

- 一种协议，用于浏览器和服务器之间`身份认证和加密数据传输`
- 位于tcp/ip协议与各种应用层协议之间
- 分为两层：
  1. SSL记录协议，建议于如TCP之上，提供`数据封装，压缩，加密`等基础功能
  2. SSL握手协议，建议于SSL记录协议之上，提供数据传输双方`身份认证，协商加密算法，交换加密密钥`

## 2.HTTPS

### 2.1https介绍

- [HTTPS基础介绍](https://blog.51cto.com/11883699/2160032)
- [白话https加密机制](https://www.cnblogs.com/jymblog/p/11646766.html)
- 默认工作端口`443`

基于`TLS`或者`SSL`提供加密处理数据，在加密信道进行HTTP内容传输的协议。

- `通信`的过程：采用对称加密进行通信
- `协商通信`的过程：采用非对称加密解决对协商过程的加密（应为相对而言，非对称加密的耗时较长）
  - 非对称加密使用的公钥获取依赖`SSL证书(需要购买)`和`CA机构`

### 2.2SSL证书

包括颁发机构，有效期，公钥，证书持有者，签名。

1. 浏览器校验证书中的颁发者，有效期等
2. 浏览器查找本地内置的受信任的证书颁发机构，与之对比，校验是否合法
3. 不合法说明证书不可信；合法则使用相同的hash算法进行解密签名
4. 读取证书中的公钥，进行后续加密

**证书获取:**

- 向一些云服务商申请，获取得到该CA机构的文件(`.CSR`)
- 其中KEY文件，为对应的server端的私钥（`丢失无法找回`）

**配置https:**

- [阿里云SSL配置Apache,nginx等](https://help.aliyun.com/video_detail/54216.html?spm=a2c4g.11186623.4.1.WbwjQN)

```sh
"nginx新增配置项"
listen 443 ssl;
ssl_certificate     /iyunwen/server/ssl/20180731.cer;
ssl_certificate_key /iyunwen/server/ssl/20180731.key;
ssl_prefer_server_ciphers on;
ssl_session_timeout 10m;
ssl_session_cache shared:SSL:10m;
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
ssl_ciphers "EECDH+ECDSA+AESGCM EECDH+aRSA+AESGCM EECDH+ECDSA+SHA384 EECDH+ECDSA+SHA256 EECDH+aRSA+SHA384 EECDH+aRSA+SHA256 EECDH+aRSA+RC4 EECDH EDH+aRSA !aNULL !eNULL !LOW !3DES !MD5 !EXP !PSK !SRP !DSS !RC4";
```
