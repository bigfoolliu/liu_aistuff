# effiency提高效率的小技巧

<!-- TOC -->

- [effiency提高效率的小技巧](#effiency%e6%8f%90%e9%ab%98%e6%95%88%e7%8e%87%e7%9a%84%e5%b0%8f%e6%8a%80%e5%b7%a7)
  - [1.为命令设置别名(alias)](#1%e4%b8%ba%e5%91%bd%e4%bb%a4%e8%ae%be%e7%bd%ae%e5%88%ab%e5%90%8dalias)
  - [2.dotfiles快速将恢复自身配置](#2dotfiles%e5%bf%ab%e9%80%9f%e5%b0%86%e6%81%a2%e5%a4%8d%e8%87%aa%e8%ba%ab%e9%85%8d%e7%bd%ae)
  - [3.项目里重复的工作写成makefile](#3%e9%a1%b9%e7%9b%ae%e9%87%8c%e9%87%8d%e5%a4%8d%e7%9a%84%e5%b7%a5%e4%bd%9c%e5%86%99%e6%88%90makefile)
  - [4.快速为项目选择一个source license](#4%e5%bf%ab%e9%80%9f%e4%b8%ba%e9%a1%b9%e7%9b%ae%e9%80%89%e6%8b%a9%e4%b8%80%e4%b8%aasource-license)
  - [5.量化工作](#5%e9%87%8f%e5%8c%96%e5%b7%a5%e4%bd%9c)
  - [6.会话以及终端管理tmux](#6%e4%bc%9a%e8%af%9d%e4%bb%a5%e5%8f%8a%e7%bb%88%e7%ab%af%e7%ae%a1%e7%90%86tmux)
  - [7.windows虚拟桌面(workspace)](#7windows%e8%99%9a%e6%8b%9f%e6%a1%8c%e9%9d%a2workspace)
  - [8.必读书籍](#8%e5%bf%85%e8%af%bb%e4%b9%a6%e7%b1%8d)
  - [9.开发者工具](#9%e5%bc%80%e5%8f%91%e8%80%85%e5%b7%a5%e5%85%b7)
  - [10.chrome高效使用](#10chrome%e9%ab%98%e6%95%88%e4%bd%bf%e7%94%a8)
  - [11.ssh免密以及别名登录](#11ssh%e5%85%8d%e5%af%86%e4%bb%a5%e5%8f%8a%e5%88%ab%e5%90%8d%e7%99%bb%e5%bd%95)
  - [13.HTTP Api设计指南](#13http-api%e8%ae%be%e8%ae%a1%e6%8c%87%e5%8d%97)

<!-- /TOC -->

- [效率指南](https://leohxj.gitbooks.io/a-programmer-prepares/effciency/coder-guide.html)

## 1.为命令设置别名(alias)

- [alias为命令设置别名](https://blog.csdn.net/doiido/article/details/43762791)

## 2.dotfiles快速将恢复自身配置

- [dotfiles入门](https://luolei.org/dotfiles-tutorial/)
- [dotfiles合集](http://dotfiles.github.io/)

## 3.项目里重复的工作写成makefile

- [makefile由浅入深](https://zhuanlan.zhihu.com/p/47390641)

## 4.快速为项目选择一个source license

- [chooselicense.com](https://choosealicense.com)

## 5.量化工作

- [quantify your code](https://blog.newrelic.com/culture/quantify-your-code/)

## 6.会话以及终端管理tmux

- [使用tmux加速操作](http://cenalulu.github.io/linux/tmux/)

## 7.windows虚拟桌面(workspace)

- [win10虚拟桌面](https://sspai.com/post/45594)

- win + ctrl + d: 创建新的虚拟桌面
- win + ctrl + left/right: 左右切换虚拟桌面
- win + ctrl + f4: 删除当前的虚拟桌面
- win + w: windowslink工作区
- win + e: 打开资源管理器
- win + r, psr.exe：打开步骤计数器

## 8.必读书籍

- [程序员必读书单](http://lucida.me/blog/developer-reading-list/)

## 9.开发者工具

- [免费开发工具](https://github.com/ripienaar/free-for-dev)

## 10.chrome高效使用

- ctrl + t: 打开新的标签页
- ctrl + n: 打开新的窗口
- ctrl + shift + n:打开新的无痕窗口
- ctrl + pgUp/pgDown: 切换标签页
- ctrl + w/f4: 关闭当前标签页
- alt + space + n: 最小化当前窗口
- alt + space + x: 最大化当前窗口

## 11.ssh免密以及别名登录

```shell
# 1.本地生成公钥和私钥,默认放置路径为~/.ssh/id_rsa以及~/.ssh/id_rsassh-keygen.pub
# 需要输入一个密码需要记忆,如果输入为空则为免密登录
ssh-keygen
# 2.将本地的公钥放到远程主机
ssh-copy-id ubuntu@192.168.6.121
# 3.登录时候需要输入自己的密码或者为空
ssh ubuntu@192.168.6.121

# 如果需要将远程主机取别名在~.ssh/config文件中加入
Host 1
    HostName 192.168.1.1
    User ubuntu
    Port 22
```

## 13.HTTP Api设计指南

- [http api设计指南中文版](https://github.com/ZhangBohan/http-api-design-ZH_CN)

**要点**:

- 资源名：使用复数形式为命名
- 行为：如`/runs/{id}/actions/stop`
- 最小化嵌套路径，即父子路径的嵌套关系不宜过深
- 响应：
  - `200`: GET请求成功，及DELETE或PATCH同步请求完成，或者PUT同步更新一个已存在的资源
  - `201`: POST 同步请求完成，或者PUT同步创建一个新的资源
  - `202`: POST，PUT，DELETE，或PATCH请求接收，将被异步处理
  - `206`: GET 请求成功，但是只返回一部分
  - `401`: Unauthorized: 用户未认证，请求失败
  - `403`: Forbidden: 用户无权限访问该资源，请求失败
  - `422`: Unprocessable Entity: 请求被服务器正确解析，但是包含无效字段
  - `429`: Too Many Requests: 因为访问频繁，你已经被限制访问，稍后重试
  - `500`: Internal Server Error: 服务器错误，确认状态并报告问题
- 提供资源的(UU)ID：默认给每一个资源id属性，最好uuid
- 提供标准的时间戳：为资源提供默认的创建时间和更新时间
- 使用UTC时间(世界标准时间)，并用ISO8601格式化
- 嵌套外键关系：使用嵌套对象序列化外键关联
- 生成结构化的错误
- 抱枕想用json最小化，多余的空格会增加响应的大小
