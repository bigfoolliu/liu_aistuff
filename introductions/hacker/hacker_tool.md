# hacker tools

<!-- vim-markdown-toc Marked -->

* [1.域名/IP查看](#1.域名/ip查看)
        - [1.1fping](#1.1fping)
* [2.端口扫描](#2.端口扫描)
        - [2.1nmap](#2.1nmap)
* [3.密码破解](#3.密码破解)
        - [3.1john](#3.1john)
* [4.网络](#4.网络)
        - [4.1netcat](#4.1netcat)

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

# 简单示例，破解有密码的rar文件
# 1.生成有密码的rar文件
rar a test.rar test.txt -p
# 2.生成rar文件的哈希值
rar2john test.rar > hash.txt
# 3.使用john破解密码
john hash.txt
```

## 4.网络

### 4.1netcat

- 端口扫描，网络通信，文件传输，加密传输，硬盘克隆，远程控制等

```sh
``
