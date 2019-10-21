# 后端面试

<!-- TOC -->

- [后端面试](#%e5%90%8e%e7%ab%af%e9%9d%a2%e8%af%95)
  - [1.HTTP](#1http)
    - [1.1介绍](#11%e4%bb%8b%e7%bb%8d)
    - [1.2GET](#12get)
    - [1.3Keep-Alive模式](#13keep-alive%e6%a8%a1%e5%bc%8f)
    - [1.4Token](#14token)
  - [2.HTTPS](#2https)
    - [2.1介绍](#21%e4%bb%8b%e7%bb%8d)
    - [2.2SSL证书](#22ssl%e8%af%81%e4%b9%a6)

<!-- /TOC -->

## 1.HTTP

### 1.1介绍

- 基于TCP/IP，应用层协议，默认端口为80
- `无状态`(对于交互式场景没有记忆)，`无连接`(限制每次连接只处理一个请求，且请求完成断开连接)

### 1.2GET

条件GET：

如果客户端重新请求的这段时间内，服务端的页面没有改变，则应该使用浏览器缓存的数据。根据客户端的请求头：

```text
If-Modified-Since:Thu, 4 Feb 2010 20:39:13 GMT
```

服务端根据该字段的时间，如果当前的响应内容没有改变，则返回`304 Not Modified`,客户端使用缓存内容。

### 1.3Keep-Alive模式

非该模式下的时候，每一次请求都要建立一次连接；该模式(持久连接)下，可以使连接持续有效，避免下次请求的时候需要重新建立连接。

### 1.4Token

含义：为`令牌`，服务端生成的一串字符串，作为客户端请求的标识，比如登录一次后生成，下次请求只需携带该Token即可。

解决问题：

1. 由应用管理，可以避开`同源策略`(同源指两个页面的协议，端口和域名都相同，同源策略指不同源的客户端脚本在没有明确授权的情况下不可以读写对方的资源)
2. 可以避免CSRF攻击
3. 可以是无状态的，可以在多个服务器之间共享

## 2.HTTPS

### 2.1介绍

[HTTPS基础介绍](https://blog.51cto.com/11883699/2160032)

基于`TLS`或者`SSL`提供加密处理数据，在加密信道进行HTTP内容传输的协议。

- 通信的过程：采用对称加密进行通信
- 协商通信的过程：采用非对称加密解决对协商过程的加密（应为相对而言，非对称加密的耗时较长）
  - 非对称加密使用的公钥获取依赖`SSL证书(需要购买)`和`CA机构`

### 2.2SSL证书

包括颁发机构，有效期，公钥，证书持有者，签名。

1. 浏览器校验证书中的颁发者，有效期等
2. 浏览器查找本地内置的受信任的证书颁发机构，与之对比，校验是否合法
3. 不合法说明证书不可信；合法则使用相同的hash算法进行解密签名
4. 读取证书中的公钥，进行后续加密

**证书获取**：

- 向一些云服务商申请，获取得到该CA机构的文件(`.CSR`)
- 其中KEY文件，为对应的server端的私钥（`丢失无法找回`）

**配置https**：

[阿里云SSL配置Apache,nginx等](https://help.aliyun.com/video_detail/54216.html?spm=a2c4g.11186623.4.1.WbwjQN)

```nginx
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
