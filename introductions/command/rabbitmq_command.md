# rabbitmq命令

<!-- vim-markdown-toc Marked -->

* [1.安装使用](#1.安装使用)
    - [1.1window安装](#1.1window安装)
    - [1.2ubuntu安装](#1.2ubuntu安装)
    - [1.3Macos安装](#1.3macos安装)
* [2.基本命令](#2.基本命令)

<!-- vim-markdown-toc -->

## 1.安装使用

### 1.1window安装

- [Windows下RabbitMQ的安装和配置](https://blog.csdn.net/zhm3023/article/details/82217222)

### 1.2ubuntu安装

```sh
# 需要erlang环境
sudo apt-get install erlang-nox
# 查看erlang是否安装完成
erl

# 获取公钥
wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -

# 更新软件包并安装
sudo apt-get update
sudo apt-get install rabbitmq-server  # 安装成功自动启动

# 启动或者终止rabbitmq
service rabbitmq start
service rabbitmq stop
service rabbitmq restart

# 启动rabbitmq的web端需要配置插件，通过 http://localhost:15672 查看，使用默认账户guest/guest 登录
rabbitmq-plugins enable rabbitmq_management  # 启用插件
service rabbitmq-server restart  # 重启

# 查看rabbitmq的状态
systemctl status rabbitmq-server
service rabbitmq-server status
```

### 1.3Macos安装

```sh
# 安装rabbitmq
brew install rabbitmq

# 后台开启rabbitmq服务
brew services start rabbitmq

# 关闭后台rabbitmq服务
brew services stop rabbitmq

# 前台开启rabbitmq服务，需要将该配置PATH=$PATH:/usr/local/sbin
rabbitmq-server
```

## 2.基本命令

```sh
# 启动服务
sudo rabbitmqctl-server  # 前台启动
sudo rabbitmqctl-server --detached  # 守护进程方式启动，不会因为当前shell关闭而结束

# 停止服务，永远不要用kill命令终止
sudo rabbitmqctl stop

# 查看所有的用户
rabbitmqctl list_users

# 增加普通用户
rabbitmqctl add_user admin password

# 给普通用户分配管理员角色
rabbitmqctl set_user_tags admin administrator

# 查看当前状态
rabbitmqctl status

# 查看集群的状态信息
rabbitmqctl cluster_status
```
