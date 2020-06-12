# hacker tools

<!-- vim-markdown-toc Marked -->

* [1.域名/IP查看](#1.域名/ip查看)
        * [1.1fping](#1.1fping)
* [2.端口扫描](#2.端口扫描)
        * [2.1nmap](#2.1nmap)
* [3.密码破解](#3.密码破解)
        * [3.1john](#3.1john)

<!-- vim-markdown-toc -->

## 1.域名/IP查看

### 1.1fping

```shell
# 安装
brew install fping

# 输出结果为对应ip和host_name
fping -A -d jianshu.com
```

## 2.端口扫描

### 2.1nmap

- [nmap官网,doc中含有中文文档](https://nmap.org/)

```shell
# 安装
brew install nmap

# 端口扫描
nmap -A -T4 -Pn baidu.com
```

## 3.密码破解

### 3.1john

```shell
# 安装
brew install john-jumbo
```

