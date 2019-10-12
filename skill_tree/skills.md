# effiency提高效率的小技巧

<!-- TOC -->

- [effiency提高效率的小技巧](#effiency提高效率的小技巧)
    - [1.为命令设置别名(alias)](#1为命令设置别名alias)
    - [2.dotfiles快速将恢复自身配置](#2dotfiles快速将恢复自身配置)
    - [3.项目里重复的工作写成makefile](#3项目里重复的工作写成makefile)
    - [4.快速为项目选择一个source license](#4快速为项目选择一个source-license)
    - [5.量化工作](#5量化工作)
    - [6.会话以及终端管理tmux](#6会话以及终端管理tmux)
    - [7.windows虚拟桌面(workspace)](#7windows虚拟桌面workspace)
    - [8.必读书籍](#8必读书籍)
    - [9.开发者工具](#9开发者工具)
    - [10.chrome高效使用](#10chrome高效使用)
    - [11.ssh免密以及别名登录](#11ssh免密以及别名登录)
    - [12.python代码](#12python代码)
        - [12.1变量](#121变量)
        - [12.2条件分支](#122条件分支)
        - [12.3使用数字和字符串的](#123使用数字和字符串的)
    - [13.HTTP Api设计指南](#13http-api设计指南)

<!-- /TOC -->

[效率指南](https://leohxj.gitbooks.io/a-programmer-prepares/effciency/coder-guide.html)

## 1.为命令设置别名(alias)

[alias为命令设置别名](https://blog.csdn.net/doiido/article/details/43762791)

## 2.dotfiles快速将恢复自身配置

[dotfiles入门](https://luolei.org/dotfiles-tutorial/)
[dotfiles合集](http://dotfiles.github.io/)

## 3.项目里重复的工作写成makefile

[makefile由浅入深](https://zhuanlan.zhihu.com/p/47390641)

## 4.快速为项目选择一个source license

[chooselicense.com](https://choosealicense.com)

## 5.量化工作

[quantify your code](https://blog.newrelic.com/culture/quantify-your-code/)

## 6.会话以及终端管理tmux

[使用tmux加速操作](http://cenalulu.github.io/linux/tmux/)

## 7.windows虚拟桌面(workspace)

[win10虚拟桌面](https://sspai.com/post/45594)

- win + ctrl + d: 创建新的虚拟桌面
- win + ctrl + left/right: 左右切换虚拟桌面
- win + ctrl + f4: 删除当前的虚拟桌面
- win + w: windowslink工作区
- win + e: 打开资源管理器
- win + r, psr.exe：打开步骤计数器

## 8.必读书籍

[程序员必读书单](http://lucida.me/blog/developer-reading-list/)

## 9.开发者工具

[免费开发工具](https://github.com/ripienaar/free-for-dev)

## 10.chrome高效使用

- ctrl + t: 打开新的标签页
- ctrl + n: 打开新的窗口
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

## 12.python代码

- [如何编写优秀的python代码https://github.com/piglei/one-python-craftsman](https://github.com/piglei/one-python-craftsman)

### 12.1变量

1. bool类型：`is_superuser`,`allow_vip`,`has_error`
2. int/float类型：`user_id`,`age`,`length_of_username`,`users_count`
3. 适当使用[匈牙利命名法](https://blog.csdn.net/z_h_s/article/details/24007249)
4. 尽量不要使用globals()/locals()
5. 变量定义尽量靠近使用
6. `使用namedtuple/dict来返回多个值，这样便于扩展和修改`
7. 控制单个函数内的变量数量
8. 能不用变量就不定义变量，及时删掉没用的变量

### 12.2条件分支

1. `避免多层分支嵌套,使用raise或者return提前结束代码`
2. `封装过于复杂的逻辑判断到函数或者方法`
3. 留意不同的重复代码，消灭之
4. 谨慎只用三元表达式
5. 使用`德摩根定律`
6. 在条件判断中使用`all()/any()`
7. 留意and和or的运算优先级，`and优先级别高于or`

### 12.3使用数字和字符串的

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
