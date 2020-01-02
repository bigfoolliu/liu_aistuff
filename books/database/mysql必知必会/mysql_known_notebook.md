# mysql必知必会读书笔记

<!-- TOC -->autoauto- [mysql必知必会读书笔记](#mysql必知必会读书笔记)auto    - [1.数据库](#1数据库)auto    - [2.mysql相关命令](#2mysql相关命令)auto        - [2.1安装启动等](#21安装启动等)auto        - [2.2数据库操作相关命令](#22数据库操作相关命令)auto        - [2.3数据表操作相关命令](#23数据表操作相关命令)auto        - [2.4数据操作相关命令](#24数据操作相关命令)auto            - [2.4.1CRUD基本操作](#241crud基本操作)auto            - [2.4.2索引基础](#242索引基础)auto        - [2.5用户以及权限操作相关命令](#25用户以及权限操作相关命令)auto            - [2.5.1用户管理](#251用户管理)auto            - [2.5.2权限管理](#252权限管理)auto        - [2.6字符集相关操作](#26字符集相关操作)auto            - [2.6.1查看已经设定的字符集](#261查看已经设定的字符集)auto            - [2.6.2设置字符集](#262设置字符集)auto    - [3.创建计算字段](#3创建计算字段)auto    - [4.汇总数据](#4汇总数据)auto        - [5.分组数据](#5分组数据)auto        - [6.联结表](#6联结表)auto        - [7.事务](#7事务)autoauto<!-- /TOC -->

## 1.数据库

## 2.mysql相关命令

### 2.1安装启动等

```shell
# mysql命令(linux系统):
sudo apt-get install mysql-server  # 安装mysql服务器
sudo apt-get install mysql-client  # 安装mysql客户端
sudo apt-get install libmysqlclient-dev  # 安装mysql客户端其他相关

ps aux | grep mysql  # 查看mysql的进程是否启动
sudo service mysql start  # 开启mysql
sudo service mysql stop  # 关闭mysql
sudo service mysql restart  # 重启mysql
sudo service mysql status  # 查看服务状态

# 连接到数据库进行操作
mysql -h(ip地址,默认为localhost) -P(端口号,默认为3306) -uroot -p(密码,可输可先不输)

# 更改登录密码
use user;
update user set authentication_string="123456" where User="root";
flush privileges;
# 然后重启mysql，登录

# 忘记root密码,修改my.conf，加上字段
# [mysqld]
# skip-grant-tables
# 就可以免密码登录
# 然后修改密码

# 执行sql文件
use db1;
source /home/xxx.sql;
```

### 2.2数据库操作相关命令

```shell
# 创建数据库:
create database db1;
create database db1 character set utf8;  # 创建指定字符集的数据库
create database db1 charset utf8;  # 创建指定字符集的数据库,简写
alter database db1 charset utf8;  # 修改已经创建的数据库的字符集

# 查看数据库:
show databases;
show create database db1;  # 查看创建数据库的过程

# 使用数据库:
use db1;  # 只有这一句后面可以增加或者不加;
select database();  # 查询当前使用的数据库

# 删除数据库:
drop database db1;
```

### 2.3数据表操作相关命令

```shell
# 数据表操作:
# 创建表:
create table tab1(id int, name char(10));
create table tab1(id int(5), name char(10));

# 查看表:
show tables;
show create table tab1;  # 查看创建表的过程
desc tab1;  # 清晰的查看表的结构

# 显示表列
show columns forom tab1;

# 修改表:
alter table tab1 rename to tab2;  # 修改表的名字
alter table tab1 add age int;  # 追加一个字段
alter table tab1 modify name varchar(100);  # 修改字段的数据类型
alter table tab1 change id number int(5);  # 更改字段名,同时要说明类型

# 删除表:
alter table tab1 drop age;  # 删除指定字段
drop table tab1;
```

### 2.4数据操作相关命令

#### 2.4.1CRUD基本操作

```shell
# 从表中查询所有的数据:
select * from tab1;
select id, name, age from tab1;  # 指定显示的列
select distinct age from tab1;  # 只返回不同的值
select age from tab1 limit 10;  # 指定返回前10行

# 数据显示排序
select name, age from tab1 order by age;  # 按年龄排序
select name, age from tab1 order by age desc;  # 按年龄降序排序

# 插入数据:
insert into tab1 values(1, 'tom');  # 向所有字段插入一条数据,需要一一对应
insert into tab1(id) values(2);  # 向指定单个字段插入一条数据
insert into tab1(name,id) values('jim',2);  # 向指定多个字段插入数据,需要一一对应
insert into tab1(id,name) values(3,'mary'),(4,'tony'),(5,'sam');  # 向指定字段插入多条数据

# 修改数据:
update tab1 set id=5;  # 将字段中所有的值更改
update tab1 set id=5 where name='tom';  # 有条件的修改字段中所有的值

# 删除数据:
truncate tab1;  # 直接删除,不可恢复
delete from tab1 where name='tony';  # 指定条件删除,部分情况可通过回滚来恢复
delete from tab1;  # 不指定条件删除
```

#### 2.4.2索引基础

```shell
# 索引:
create index name on tab1(name);  # 创建最简单的索引
# 查看:
show index from tab1;
# 创建:
create index index1 on tab1(name(20));
# 删除:
drop index1 from tab1;
```

### 2.5用户以及权限操作相关命令

#### 2.5.1用户管理

```shell
# 用户管理:
# 避免非开发用户误操作.
# 查看所有用户 MySQL中所有的用户及权限信息都存储在MySQL数据库的user表中

# 查看所有用户:
select host, user, authentication_string from user;

# 添加用户并分配权限
# https://blog.csdn.net/xudejun/article/details/84779442
use mysql;
create user tonyliu@localhost identified by "123456";
flush privileges;

# 删除用户:
drop user "liu"@"localhost";
```

#### 2.5.2权限管理

- [mysql权限详解](https://blog.csdn.net/BlingZeng/article/details/89351946)
- [mysql grant用户权限总结](https://blog.csdn.net/anzhen0429/article/details/78296814)

```shell
# 查看权限:
show grants for 用户名@主机地址
show grants for liu@localhost

# 修改权限:
grant 权限名称 on 数据库 to 账户@主机 with grant option;
grant all privileges on *.* to "liu"@"localhost" with grant option;  # 赋予该用户所有数据库的权限
flush privileges;  # 刷新权限

# 当使用orm连数据库,仍有权限问题的时候,需要修改用户的密码并重启mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'new-password';
```

### 2.6字符集相关操作

**mysql的utf8不是真正的utf8, utf8mb4才是真正的utf8。**

#### 2.6.1查看已经设定的字符集

```shell
# 查看mysql支持的字符集
show charset;

# 查看数据库服务器和数据库字符集
show variables like '%character%';

# 查看指定数据库的字符集
show create database test_db;

# 查看表的字符集
show create table test_table;
show table status from test_tb like "test_table";

# 查看表中所有列的字符集
show full columns from test_table;
```

#### 2.6.2设置字符集

```shell
# 创建数据库的时候设置字符集
create database test_db default character set="utf8mb4";
# 创建表的时候设置字符集
create table test_table(id int(6), name char(10)) default character set="utf8mb4";

# 修改库的字符集
alter database test_db default character set "utf8mb4";
# 修改表的字符集
alter table test_table convert to character set "utf8mb4";
# 修改字段的字符集
alter table test_table modify test_field char(10) character set "utf8mb4";
```

## 3.创建计算字段

存储在表中的数据不是应用所需要或者能直接使用的，`计算字段是从数据库中检索出转换，计算或者格式化的数据，不实际存在于数据库表中，而是在运行select语句的时候创建的`。

```shell
# 创建计算字段，经name和age拼接为 name(age) 格式,注意空格
select Contat(name, ' (', age, ')') from tab1;
select Contat(name, ' (', age, ')') as title from tab1;  # 创建计算字段并设置别名

# 创建执行计算的计算字段
select price*numbers as total_price from tab1;
```

## 4.汇总数据

```shell
# 汇总平均数
select Avg(price) as avg_price from tab1;

# 计算最大值
select Max(price) as max_price from tab1;
```

### 5.分组数据

```shell
# 通过年龄分组
select name from tab1 group by age;
```

### 6.联结表

不同表之间通过外键进行联系关联起来。

### 7.事务

**mysql默认是自动提交，即每个语句后面一个提交，可以通过设置`autocmmit`关闭**

```shell
# 开启事务
start transaction;

# 回滚,将事务之前的步骤取消
rollback;

# 提交事务
commit;
```
