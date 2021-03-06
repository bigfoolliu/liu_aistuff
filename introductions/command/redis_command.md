# redis命令

<!-- vim-markdown-toc Marked -->

* [1.安装启动](#1.安装启动)
* [2.数据库操作](#2.数据库操作)
* [3.数据操作](#3.数据操作)
    - [3.1基础数据操作](#3.1基础数据操作)
    - [3.2scan命令](#3.2scan命令)
* [4.事务操作](#4.事务操作)
* [5.持久化操作](#5.持久化操作)
* [6.redis客户端命令](#6.redis客户端命令)

<!-- vim-markdown-toc -->

## 1.安装启动

- [redis命令参考](http://redisdoc.com/)
- 使用 Lua 解释器来执行脚本

```sh
sudo apt-get install redis-server  # 安装brew
vim /etc/redis/redis.conf  # 可以配置redis的绑定ip为0.0.0.0

# linux启动
sudo service redis-server restart  # 启动redis
# macos启动
brew services start redis

redis-server  # 进入redis服务端
redis-cli  # 进入redis客户端，输入ping来判断是否可以连接

redis-cli -h <host> -p <port> -a <password>  # 在远程的服务器上执行
redis-cli -h 192.168.1.2 -p 6379 -a 123456  # eg

# 查看所有配置
config get *
config get masterauth  # 获取具体的一项配置
config set masterauth xxx  # 设置一项具体配置

redis-benchmark -n 1000  # redis基准测试，-n指定请求数
redis-benchmark -h 127.0.0.1 -p 6379 -t set,lpush -n 100000 -q  # 只执行set和lpush命令10000次，-q 参数让结果只显示每秒执行的请求数
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
quit  # 关闭当前连接

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

### 3.1基础数据操作

```sh
# keys的操作
keys *  # 查看所有的key
del key  # 删除键
exists key  # 判断给定的key是否存在

dump key  # 序列化给定key，并返回序列化的值,eg: "\x00\x04tony\t\x00\xebU\x96oF~6\xa8"
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
mset name "tony" age "10"  # 同时设置多个key-value对
mget name age  # 同时获取多个key值

setnx name "tony"  # 当key不存在的时候设置key的值
setex name 10 "tony"  # 设置key同时设置过期时间

# 哈希
hmset user:1 name tony pwd 123456  # 设置hash键值对
hgetall user:1  # 取得hash键值对
hdel user:1  # 删除一个或多个哈希表字段
hexists user:1  # 判断哈希表指定的key是否存在
hkeys *  # 查看所有哈希表中的字段

# 列表
# 添加一个元素到列表的头部
lset names 0 "b"  # 设置索引为0的元素为b
lpush names tony  # 将一个或者多个值插入到列表头部
lrange names 0 -1  # 获取列表的内容,0到-1则是所有的值
llen names  # 查看列表的长度    
blpop names  # 移出并获取列表的第一个元素
brpop names  # 移出并获取列表的最后一个元素
lindex names 0  # 通过索引获取元素

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

# 位图(redis bitmap)
setbit aaa:001 10001 1  # 返回操作之前的数值
```

### 3.2scan命令

- 复杂度为O(n), 但是通过游标分步进行，不阻塞线程
- 提供limit控制返回数量
- 提供模式匹配
- 返回的结果可能有重复，需要去重
- redis的底层是Hash表实现(key的存储结构就是HashMap那样数组+链表的结构)，scan返回的游标就也是数组的索引

```sh
# cursor初始为0，返回结果中有新的游标值，默认最多返回10条数据
scan 0  # 返回结果中包含新的游标值
scan 0 match test_* count 20  # 使用模式匹配和数量限制
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

multi  # 标记一个事务块的开始
set name tony
get name tony
exec  # 执行所有事务块的命令

discard  # 取消事务
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

## 6.redis客户端命令

```sh
client list  # 返回连接到redis服务的客户端的列表

client setname tony  # 设置当前连接的名称
client getname  # 获取当前连接的名称

client pause  # 挂起客户端连接
client kill  # 关闭客户端连接
```
