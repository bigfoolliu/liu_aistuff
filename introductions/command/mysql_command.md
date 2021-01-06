# mysql命令

<!-- vim-markdown-toc Marked -->

* [1.安装启动](#1.安装启动)
    - [1.1安装](#1.1安装)
    - [1.2启动连接](#1.2启动连接)
* [2.数据库操作](#2.数据库操作)
    - [2.1数据库CRUD](#2.1数据库crud)
    - [2.2数据库备份](#2.2数据库备份)
    - [2.3数据库外部导入](#2.3数据库外部导入)
* [3.数据表操作](#3.数据表操作)
    - [3.1数据表CRUD](#3.1数据表crud)
    - [3.2表信息](#3.2表信息)
* [4.数据操作相关命令](#4.数据操作相关命令)
    - [4.1CRUD基本操作](#4.1crud基本操作)
    - [4.2索引操作](#4.2索引操作)
    - [4.3计算字段](#4.3计算字段)
    - [4.4视图操作](#4.4视图操作)
* [5.用户以及权限操作相关命令](#5.用户以及权限操作相关命令)
    - [5.1用户管理](#5.1用户管理)
    - [5.2权限管理](#5.2权限管理)
* [6.字符集相关操作](#6.字符集相关操作)
    - [6.1查看已经设定的字符集](#6.1查看已经设定的字符集)
    - [6.2设置字符集](#6.2设置字符集)

<!-- vim-markdown-toc -->

## 1.安装启动

### 1.1安装

```sh
# mysql命令(linux系统)
# 安装
sudo apt-get install mysql-server  # 安装mysql服务器
sudo apt-get install mysql-client  # 安装mysql客户端
sudo apt-get install libmysqlclient-dev  # 安装mysql客户端其他相关
```

### 1.2启动连接

```sh
# 开启关闭mysql服务
ps aux | grep mysql  # 查看mysql的进程是否启动
sudo service mysql start  # 开启mysql
sudo service mysql stop  # 关闭mysql
sudo service mysql restart  # 重启mysql
sudo service mysql status  # 查看服务状态

# 连接到数据库
# mysql -h(ip地址,默认为localhost) -P(端口号,默认为3306) -uroot -p(密码,可输可先不输)
mysql -h localhost -P 3306 -u root -p

# 更改登录密码
# 修改之后，然后重启mysql，登录
use user;
update user set authentication_string="123456" where User="root";
flush privileges;

# 忘记root密码,修改my.conf，加上字段
# [mysqld]
# skip-grant-tables
# 就可以免密码登录
# 然后修改密码

# 查看服务器配置文件路径，默认为/etc/my.cnf等
which mysqld  # /usr/bin/mysqld
/usr/bin/mysqld --verbose --help | grep -A 1 "Default options"  # 查找得到具体的路径以及加载顺序，可以配置更复杂的配置
```

## 2.数据库操作

### 2.1数据库CRUD

```sh
# 创建数据库:
create database db1;
create database db1 character set utf8  # 创建指定字符集的数据库
create database db1 charset utf8  # 创建指定字符集的数据库,简写
alter database db1 charset utf8  # 修改已经创建的数据库的字符集

# 查看数据库:
show databases;
show create database db1;  # 查看创建数据库的过程

# 使用数据库:
use db1;  # 只有这一句后面可以增加或者不加;
select database();  # 查询当前使用的数据库

# 删除数据库:
drop database db1;
```

### 2.2数据库备份

```sh
# 使用dump备份数据库
mysqldump -h 127.0.0.1 -p 3306 -uroot -p123456 --database db > /data/db.sql  # 备份整个testdb数据库
mysqldump -h 127.0.0.1 -p 3306 -uroot -p123456 --database db | gzip > /data/db.sql  # 整个testdb数据库,但是进行压缩,防止文件过大
mysqldump -h 127.0.0.1 -p 3306 -uroot -p123456 --database db t1 t2 > /data/db.sql  # 备份数据库的多张表
mysqldump -h 127.0.0.1 -p 3306 -uroot -p123456 --databases db1 db2 > /data/dbs.sql  # 备份一个实例的多个数据库
mysqldump -h 127.0.0.1 -p 3306 -uroot -p123456 --all-databases > /data/db.sql  # 备份实例上的所有数据库

mysqldump -u root -p db_name > db_name.sql  # 将整个数据库导出
mysqldump -u root -p db_name table_name > table_name.sql  # 导出数据库的一张表
```

### 2.3数据库外部导入

```sh
# 执行sql文件,导入数据库
use db1;
source /home/xxx.sql;


# 有可能过一段时间在打开时发现命令行提示链接超时,等待重新链接
# 这时候需要再执行以下 sql：

set global max_allowed_packet=100000000;  # 客户端/服务器之间通信的缓存区的最大大小
set global net_buffer_length=100000;  # TCP/IP 和套接字通信缓冲区大小,创建长度达 net_buffer_length 的行
set global interactive_timeout=28800000;  # 对后续起的交互链接有效时间
set global wait_timeout=28800000;  # 对当前交互链接有效时间

```

## 3.数据表操作

### 3.1数据表CRUD

```sh
# 创建表:
create table tab1(id int, name char(10));
create table tab1(id int(5), name char(10));
create table tab1(c1 int, c2 int, KEY(c1));   # 创建表并在c1列建立索引

# 查看表:
show tables;
show create table tab1;  # 查看创建表的过程
desc tab1;  # 清晰的查看表的结构
show table status like 'tab1';  # 查看表的信息，包括存储引擎，版本，行数，占用大小，更新时间等

# 显示表列
show columns from tab1;

# 修改表:
alter table tab1 rename to tab2;  # 修改表tab1的名字为tab2
alter table tab1 add age int;  # 追加一个整型字段age
alter table tab1 modify column number varchar(100);  # 修改字段number的数据类型为varchar
alter table tab1 change id number int(5);  # 更改字段名id为number, 同时要说明类型
alter table tab1 modify column number default null;  # 修改字段number默认可以为空

# 删除表:
alter table tab1 drop age;  # 删除指定字段，删除列
alter table tab1 drop column age  # 删除质指定字段，删除列
drop table tab1;  # 删除整张表
```

### 3.2表信息

```sh
# 检查表状态，是否有损坏,索引是否有错误等
check table tab1;
# 修复表，可能部分存储引擎不支持
repair table tab1;
```

## 4.数据操作相关命令

### 4.1CRUD基本操作

```sh
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
insert into tab1(name,id) values('jim',2);  # 向指定多个字段插入数据,需要一一对应
insert into tab1(id,name) values(3,'mary'),(4,'tony'),(5,'sam');  # 向指定字段插入多条数据

insert into tab1(id) values(2);  # 向指定单个字段插入一条数据, 推荐


# 修改数据:
update tab1 set id=5;  # 将字段中所有的值更改
update tab1 set id=5 where name='tom';  # 有条件的修改字段中所有的值

# 删除数据:
truncate tab1;  # 直接删除,不可恢复
delete from tab1 where name='tony';  # 指定条件删除,部分情况可通过回滚来恢复
delete from tab1;  # 不指定条件删除
```

### 4.2索引操作

```sh
# 创建索引
create index name on tab1(name);  # 创建最简单的索引
create index index1 on tab1(name(20));

# 查看索引
show index from tab1;

# 删除索引
drop index1 from tab1;
```

### 4.3计算字段

- 存储在表中的数据不是应用所需要或者能直接使用的，`计算字段是从数据库中检索出转换，计算或者格式化的数据，不实际存在于数据库表中，而是在运行select语句的时候创建的`。

```sh
# 创建计算字段，经name和age拼接为 name(age) 格式,注意空格
select Contat(name, ' (', age, ')') from tab1;
select Contat(name, ' (', age, ')') as title from tab1;  # 创建计算字段并设置别名

# 创建执行计算的计算字段
select price*numbers as total_price from tab1;

# 汇总数据
# 汇总平均数
select Avg(price) as avg_price from tab1;

# 计算最大值
select Max(price) as max_price from tab1;

# 分组数据
# 通过年龄分组
select name from tab1 group by age;
```

### 4.4视图操作

```sh
# 创建视图,会产生类似的一张表
create view view_avg_score
as
    select id, round(avg(score), 1) as avg_score
    from student group by id;

# 使用视图
select * from view_avg_score;

# 删除视图
drop view view_avg_score;
```

## 5.用户以及权限操作相关命令

### 5.1用户管理

```sh
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

### 5.2权限管理

- [mysql权限详解](https://blog.csdn.net/BlingZeng/article/details/89351946)
- [mysql grant用户权限总结](https://blog.csdn.net/anzhen0429/article/details/78296814)

```sh
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

## 6.字符集相关操作

- mysql的utf8不是真正的utf8，utf8mb4才是真正的utf8

### 6.1查看已经设定的字符集

```sh
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

### 6.2设置字符集

```sh
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
