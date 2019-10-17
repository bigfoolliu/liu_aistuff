# mysql必知必会读书笔记

<!-- TOC -->

- [mysql必知必会读书笔记](#mysql必知必会读书笔记)
    - [1.数据库](#1数据库)
        - [数据库设计三大范式](#数据库设计三大范式)
    - [2.mysql相关命令](#2mysql相关命令)
        - [2.1安装以及使用命令](#21安装以及使用命令)
        - [2.2数据库操作相关命令](#22数据库操作相关命令)
        - [2.3数据表操作相关命令](#23数据表操作相关命令)
        - [2.4数据操作相关命令](#24数据操作相关命令)
        - [2.5用户以及权限操作相关命令](#25用户以及权限操作相关命令)
    - [3.创建计算字段](#3创建计算字段)
    - [4.汇总数据](#4汇总数据)
        - [5.分组数据](#5分组数据)
        - [6.联结表](#6联结表)

<!-- /TOC -->

## 1.数据库

### 数据库设计三大范式

1. 每一列都具有原子性, 即不可再分割
2. 每个表只描述一件事情
3. 表中不能存在冗余字段

## 2.mysql相关命令

### 2.1安装以及使用命令

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
alter table tab1 add age int;  # 追加一个字段
alter table tab1 modify name varchar(100);  # 修改字段的数据类型
alter table tab1 change id number int(5);  # 更改字段名,同时要说明类型

# 删除表:
alter table tab1 drop age;  # 删除指定字段
drop table tab1;
```

### 2.4数据操作相关命令

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

### 2.5用户以及权限操作相关命令

```shell
# 索引:
# 查看:
show index from tab1;
# 创建:
create index index1 on tab1(name(20));
# 删除:
drop index1 from tab1;
# 结论:
#     1. 索引可以明显提高某些字段的查询效率, 但不是所有的表都需要建立索引
#     2. 如果表中数据很少，没有必要建立索引
#     3. 如果一个表中的数据增删很频繁，不能建立索引, 因为只要数据发生增减，索引就要重新建立。增加了系统开销，反而慢了。
#     4. 索引只适合查询操作频繁的表。


# 用户管理:
#     - 避免非开发用户误操作.
#     - 查看所有用户 MySQL中所有的用户及权限信息都存储在MySQL数据库的user表中
#     - 查看所有用户:
select host ,user,authentication_string from user;

# 创建账户并授予查询权限:
    # grant 权限列表 on 数据库 to '用户名'@'访问主机' identified by '密码';
grant tab1 on db1 to "liu"@"localhost" identified by "123456"
# 或
grant select on db1.* to "liu"@"localhost" identified by "123456"

# 查看权限:
show grants for 用户名@主机地址
show grants for liu@localhost

# 修改权限:
grant 权限名称 on 数据库 to 账户@主机 with grant option;
grant all privileges on *.* to "liu"@"localhost" with grant option;  # 赋予该用户所有数据库的权限
flush privileges;  # 刷新权限

# 删除用户:
drop user "liu"@"localhost";
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
