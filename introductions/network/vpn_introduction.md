# vpn(virtual private networking)

<!-- TOC -->

- [vpn(virtual private networking)](#vpnvirtual-private-networking)
  - [工作原理](#工作原理)
  - [openvpn安装配置](#openvpn安装配置)

<!-- /TOC -->

`虚拟专用网络`，在公用网络上建立专用网络，进行加密通讯。VPN网关通过对数据包的加密和数据包目标地址的转换实现远程访问。VPN可通过服务器、硬件、软件等多种方式实现。基于c-s架构。

实质：利用加密技术，在公网上封装出一个数据通信隧道，从而只要连上互联网，就可以通过连接vpn服务器来进入内网。

## 工作原理

1. vpn使用双网卡，外网卡使用公网ip接入互联网
2. 最关键的技术是在公网上建立虚拟信道

## openvpn安装配置

- [参考](https://mp.weixin.qq.com/s/vQV86VFAclcAa2OeDcNt-w)
