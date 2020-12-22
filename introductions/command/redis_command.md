# redis命令

<!-- vim-markdown-toc Marked -->

* [1.安装启动](#1.安装启动)
* [2.数据库操作](#2.数据库操作)
* [3.数据操作](#3.数据操作)
* [4.事务操作](#4.事务操作)
* [5.持久化操作](#5.持久化操作)

<!-- vim-markdown-toc -->

## 1.安装启动

- [redis命令参考](http://redisdoc.com/)

```sh
sudo apt-get install redis-server  # 安装brew
vim /etc/redis/redis.conf  # 可以配置redis的绑定ip为0.0.0.0

sudo service redis-server restart  # 启动redis

redis-server  # 进入redis服务端
redis-cli  # 进入redis客户端，输入ping来判断是否可以连接

redis-cli -h <host> -p <port> -a <password>  # 在远程的服务器上执行
redis-cli -h 192.168.1.2 -p 6379 -a 123456  # eg
```

## 2.数据库操作

```sh
# 数据库的操作
select 1  # 切换到不同的数据库，默认为0，共16个
dbsize  # 查看当前数据库的key的数量

flushdb  # 清空当前数据库的所有key
flushall  # 清空整个redis服务器的数据(所有数据库的所有key)

swapdb 0 1  # 对换0,1两个数据库

info  # 查看redis服务器的信息,进入redis-cli之后

# 调试
ping  # 客户端向服务器发送查看服务器是否正常


# 客户端连接
config get maxclients  # 获取最大连接数量
redis-server --maxclients 10000  # 服务端启动时候设置最大连接数


# 安全设置
config get requirepass  # 查看是否设置了密码
config set requirepass "123456"  # 设置密码
config get requirepass  # 获取密码
auth 123456  # 验证密码


# 发布-订阅测试
subscribe channel1  # 在客户端1订阅channel1频道的消息
psubscribe news.*channel  # 订阅多个符合条件的频道

unsubscribe  # 退订频道
publish channel1 hello  # 在客户端2发送消息到channel1,返回结果会显示订阅该频道的数量
pubsub channels  # 查看当前的活跃频道(即至少有一个订阅者的频道)
```

## 3.数据操作

```sh
# key的操作
keys *  # 查看所有的key
del key  # 删除键
exists key  # 判断给定的key是否存在

dump key  # 序列化给定key，并返回序列化的值
restore key 0 "\x00\x15hello, dumping world!\x06\x00E\xa0Z\x82\xd8r\xc1\xde"  # 将序列化的值反序列化,0为ttl的时间

expire key 10  # 给key设置过期时间为10秒
ttl key  # 查看key的剩余生存时间(s)
persist key  # 将一个带有过期的key设置为永久的不过期的key

move key 1  # 将key移动到新的数据库1
type key  # 查看key所存储的值的类型
rename key <new_key>  # 修改key的名称


# 查看数据类型
type key1

# 字符串
set name "tony"  # 设置键值
get name  # 取值

# 哈希
hmset user:1 name tony pwd 123456  # 设置hash键值对
hgetall user:1  # 取得hash键值对

# 列表
# 添加一个元素到列表的头部
lpush names tony
lpush names tom
lrange names 0 10  # 获取列表的内容

# 集合
# 添加一个string元素到key对应的set集合中，成功返回1
# 再次添加相同的元素会因为唯一性被忽略,返回0
sadd names tony
smembers names  # 获取集合中的元素
sinter tags1 tags2  # 使用交集
srandmember names 3  # 随机获取3个元素,列表长度不变
spop names 3  # 随机弹出3个元素，列表长度改变


# 有序集合
# 添加元素到有序集合
zadd names 0 tony
zadd names 10 jim
zrangebyscore names 0 100  # 取有序集合中的元素
```

## 4.事务操作

- `MULTI`
- `EXEC`
- `DISCARD`
- `WATCH`

```sh
# 开始事务。
# 命令入队。
# 执行事务。

# 一下为一个事务的全过程

multi
set name tony
get name tony
exec
```

## 5.持久化操作

```sh
# 创建当前数据库的备份，会在安装的目录创建dump.rdb文件
# 在生产环境很少执行 SAVE 操作，因为它会阻塞所有客户端，保存数据库的任务通常由 BGSAVE 命令异步地执行
save

# 恢复数据，只需要将备份文件`dump.rdb`移动到redis的安装目录

config get dir  # 查看备份文件的位置
bgsave  # 在后台异步的保存数据库
lastsave  # 返回最近一次Redis成功将数据保存到磁盘的时间，Unix时间戳形式
```
