# hacker tools

<!-- vim-markdown-toc Marked -->

- [hacker tools](#hacker-tools)
  - [1.域名/IP查看](#1域名ip查看)
    - [1.1fping](#11fping)
  - [2.端口扫描](#2端口扫描)
    - [2.1nmap](#21nmap)
  - [3.密码破解](#3密码破解)
    - [3.1john](#31john)
  - [4.网络](#4网络)
    - [4.1netcat](#41netcat)

<!-- vim-markdown-toc -->

## 1.域名/IP查看

### 1.1fping

```sh
# 安装
brew install fping

# 输出结果为对应ip和host_name
fping -A -d baidu.com
```

## 2.端口扫描

### 2.1nmap

- [nmap官网,doc中含有中文文档](https://nmap.org/)

```sh
# 安装
brew install nmap

# 端口扫描
nmap -A -T4 -Pn baidu.com
```

## 3.密码破解

### 3.1john

```sh
# 安装
brew install john-jumbo
```

## 4.网络

### 4.1netcat

- 端口扫描，网络通信，文件传输，加密传输，硬盘克隆，远程控制等

```sh
``
