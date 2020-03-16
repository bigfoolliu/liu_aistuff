# Linux相关知识

<!-- TOC -->autoauto- [Linux相关知识](#linux相关知识)auto    - [1.进程](#1进程)auto        - [1.1进程信息](#11进程信息)auto        - [1.2僵尸进程(zombie process)](#12僵尸进程zombie-process)auto        - [1.3几个与开关进程有关的标准信号](#13几个与开关进程有关的标准信号)auto        - [1.4supervisor进程管理](#14supervisor进程管理)auto    - [2.linux命令](#2linux命令)auto        - [2.1系统信息](#21系统信息)auto        - [2.2目录及文件](#22目录及文件)auto        - [2.3进程相关](#23进程相关)auto            - [2.3.1杀死进程的几种方式](#231杀死进程的几种方式)auto        - [2.4网络相关](#24网络相关)auto            - [2.4.1tcpdump网络抓包](#241tcpdump网络抓包)auto            - [2.4.2网关相关命令](#242网关相关命令)auto            - [2.4.3curl命令](#243curl命令)auto            - [2.4.4wget命令](#244wget命令)auto            - [2.4.5网络其他](#245网络其他)auto        - [2.5其它](#25其它)auto    - [8.Linux文件系统](#8linux文件系统)auto        - [8.1使用tmpfs](#81使用tmpfs)auto    - [9.linux重要文件](#9linux重要文件)auto        - [9.1/etc/hosts文件](#91etchosts文件)auto        - [9.2/etc/resolv.conf文件](#92etcresolvconf文件)auto        - [9.3/etc/hosts文件](#93etchosts文件)auto    - [10.系统监控](#10系统监控)auto    - [a.其他](#a其他)auto        - [a.1文件改变](#a1文件改变)auto        - [a.2流量监控工具](#a2流量监控工具)auto        - [a.3使用crontab开启定时任务](#a3使用crontab开启定时任务)auto        - [a.4ssh文件传输](#a4ssh文件传输)auto        - [a.5有趣命令](#a5有趣命令)autoauto<!-- /TOC -->

- [Linux知识介绍](http://billie66.github.io/TLCL/book/chap04.html)
- [Linux命令大全网站](https://man.linuxde.net/)

## 1.进程

### 1.1进程信息

**进程状态码(PROCESS STATE CODES)：**

进程的状态码的含义，ps之后的`STAT`列。

```shell
# Here are the different values that the s, stat and state output specifiers (header "STAT" or "S") will display to describe the state of a process:
D    uninterruptible sleep (usually IO)
R    running or runnable (on run queue)
S    interruptible sleep (waiting for an event to complete)
T    stopped, either by a job control signal or because it is being traced.
W    paging (not valid since the 2.6.xx kernel)
X    dead (should never be seen)
Z    defunct ("zombie") process, terminated but not reaped by its parent.

For BSD formats and when the stat keyword is used, additional characters may be displayed:
<    high-priority (not nice to other users)
N    low-priority (nice to other users)
L    has pages locked into memory (for real-time and custom IO)
s    is a session leader
l    is multi-threaded (using CLONE_THREAD, like NPTL pthreads do)
+    is in the foreground process group.
```

**进程信息:**

```shell
cat /proc/pid/statm

# pid 为进程号
# 输出解释
# 第一列  size:任务虚拟地址空间大小
# 第二列  Resident：正在使用的物理内存大小
# 第三列  Shared：共享页数
# 第四列  Trs：程序所拥有的可执行虚拟内存大小
# 第五列  Lrs：被映像倒任务的虚拟内存空间的库的大小
# 第六列  Drs：程序数据段和用户态的栈的大小
# 第七列 dt：脏页数量
```

### 1.2僵尸进程(zombie process)

子进程的结束和父进程的运行是一个异步过程,即父进程永远无法预测子进程 到底什么时候结束。 当一个 进程完成它的工作终止之后，它的父进程需要调用wait()或者waitpid()系统调用取得子进程的终止状态。

- 孤儿进程
  一个父进程退出，而它的一个或多个子进程还在运行，那么那些子进程将成为孤儿进程。孤儿进程将被init进程(进程号为1)所收养，并由init进程对它们完成状态收集工作。

- 僵尸进程
  一个进程使用fork创建子进程，如果子进程退出，而父进程并没有调用wait或waitpid获取子进程的状态信息，那么子进程的进程描述符仍然保存在系统中。这种进程称之为僵死进程。

### 1.3几个与开关进程有关的标准信号

- `SIGINT`
  其实我们平时在使用终端运行某个软件的时候，如果这个软件会持续运行而不再显示shell提示符，那么我们通常关闭这个程序是使用^C（就是Ctrl+C），其实就是向当前运行的进程发送了一个SIGINT。通知前台进程组停止进程。也就是会中断前台运行的所有进程。

- `SIGQUIT`
  与SIGINT其实相似，通过终端键入^\（就是Ctrl+\）来发送，相当于错误信号，会让进程产生core文件。

- `SIGTERM`
  当我们不加任何参数直接调用kill时，则会发送这个信号给进程，这个关闭请求并非强制，它会被阻塞，通常会等待一个程序正常退出。

- `SIGKILL`
  这个就厉害了，这也是为什么关不掉一个程序，网上通常会教你kill -9，它发送一个强制的关闭信号，不可被忽略。但正是因为这样，程序难以进行自我清理，而且会产生僵尸进程。

### 1.4supervisor进程管理

Python开发的一套client/server架构的进程管理程序，能做到开机启动，以daemon进程的方式运行程序，并可以监控进程状态等等。

组件：

1. supervisord，supervisor的服务器端，负责启动子程序，响应客户端发来的命令，重启子程序，记录子程序stdout和stderr的日志，处理Event，配置位置为：`/etc/supervisord.conf`
2. supervisorctl，提供一个类shell接口，用户可以使用supervisorctl连接不同的supervisord进程，查看子进程状态，start、stop子进程，获取控制的子进程列表。
3. Web Server，使用tcp socket启动supervisord的时候，提供的一个访问supervisor的web接口。
4. XML-RPC Interface，一个XML-RPC接口。

**supervisor相关命令：**

```shell
# 重启服务
service supervisor restart

# 启动指定子进程
supervisorctl start <process_name>

# 查看错误日志
supervisor tail <process_name> stdout

# 查看管理子进程运行状态
supervisorctl status

# 关闭子进程
supervisorctl stop <process_name>

# 更新了配置supervisor的配置文件(/etc/supervisor/conf.d/worker)之后重启
supervisorctl reread
supervisorctl update  # 更新新的配置到supervisord

# 更新了代码之后重启模块adm
supervisorctl restart adm

# 重新启动配置中的所有程序
supervisorctl reload
```

```shell
# worker上设置代理服务器
git config --global http.proxy http://192.168.0.118:4080
```

## 2.linux命令

### 2.1系统信息

```shell
# 设置系统默认的UTC时间为Shanghai时间
tzselect
TZ='Asia/Shanghai'
export TZ

# 查看内存情况
free -mh

# 查看usb设备连接信息
# Bus 005 Device 004: ID 1871:1130 Aveo Technology Corp.  # 普通摄像头
# Bus 005 表示这是第5个usb主控制器
# Device 004 表示系统给usb分配的设备号
# ID 1871:1130 表示usb设备的ID，由芯片制造商设置，可以唯一表示该设备
# Aveo Technology Corp. 表示生产商的名字和设备名
lsusb
lsusb -v

# v4l命令查看设备
v4l2-ctl --list-devices  # 查看v4l设备列表
v4l2-ctl -d /dev/video0 --list-formats  # 查看当前摄像头支持的视频压缩格式
v4l2-ctl --list-formats-ext -d /dev/video0  # 查看usb摄像头支持的格式

# 查看某个摄像头的详细信息
udevadm info --query=all --name=/dev/video0

# 查看CPU信息
cat /proc/cpuinfo

id  # 展示当前用户的身份号
passwd user1  # 更改用户密码
uptime  # 查看系统启动的时间统计
uname -a  # 查看系统信息

lsb_release -a  # 简洁的显示系统信息的命令

useradd user1  # 增加用户
useradd -g group1 user2  # 增加用户并指定用户组
useradd -d /mnt/d user3  # 增加用户并指定家目录
useradd -p 123456 user4  # 增加用户并设置密码

userdel user1  # 删除用户

groupadd group1  # 新增工作组


cat /etc/passwd  # 查看所有的用户
cat /etc/shadow  # 查看用户密码
cat /etc/group  # 查看所有用户组
```

### 2.2目录及文件

```shell
ls -t  # 列举当前文件夹下所有目录和文件并以时间排列
ls -u  # 以文件上次被访问的时间排序
ls -S  # 以文件大小排序

ls -lh  # 显示文件大小
ls -lhS  # 从大到小排列
ls -d */  # 只列出文件夹
ls -i  # 带索引号显示
ls -t  # 按照修改时间显示，新文件在前

# 用grep直接搜索文件中的文本内容
grep -i 'Out of Memory' /var/log/messages

# 查看文件占用
fuser -s file  # 查看文件是否被其他进程占用(持续写入状态，vi打开不是), 返回值为1则为被占用，0则为未被占用
fuser -v file  # 查看文件的具体占用信息，包括占用进程的 USER, PID 等

# 文件查找
find . -name *.sh -print  # 根据文件名查找文件,在当前目录下查找*.sh并将其输出
find . -ctime 1 -type f -print  # 查找过去 1 小时修改过的普通文件
find . -ctime 10 -type d -print  # 查找过去 10 分钟修改过的目录
find . -size +10M -type f -print  # 查找文件大小超过 10（b/c/w/k/M/G）的文件
find . -path ./test -prune -o -print  # 查找文件的时候避开当前目录下的test文件夹

# 统计当前路径下所有.py文件的个数
find ./ -name *.py | wc -l
find ./ -name "*.py" | wc -l

# 统计当前路径下所有.py文件各自的行数
find ./ -name *.py | xargs wc -l
find ./ -name "*.py" | xargs wc -l

# 递归的统计一目录下及其子目录下所有匹配文件的总的行数和每个文件的行数，可以使用一下命令
wc -l `find ./ -name *.csv`

# 查看目录下的文件夹占用空间情况
du -h --max-depth=1 /data/

# 查看文件夹占据磁盘大小以及根据文件夹的大小排序
du -hs /data/
du -hs /data/ | sort -n

# 查看文件信息
file test.py

# 以可以滚动翻页的方式查看文件
less test.py

# 使用tar进行文件归档
tar -cf out.tar file1 file2 folder1  # f表示指定tar文件名必须在参数最后，c表示新建一个tar包
tar -tf out.tar  # 列出已经归档文件中的内容
tar -rvf out.tar file3  # r向已经归档文件添加新的文件,v表示输出待打包文件更详细的信息

tar -xf out.tar  # 将归档内容提取到当前文件夹
tar -xf out.tar -C /  # -C提取到指定的文件夹

# 使用gzip进行文件压缩，gunzip将压缩文件还原
gzip test.py  # 压缩文件会替代原始文件
gzip -c test.py > test.py.gz  # 将压缩结果重定向，可以保留压缩源文件

gunzip test.py.gz  # 解压缩文件
gzip -d test.py.gz  # 解压缩文件，与上效果相同

gzip -r folder1  # 压缩文件夹, gzip 命令只会压缩，不能打包，所以才会出现没有打包目录，而只把目录下的文件进行压缩的情况
gunzip -r folder1  # 解压缩文件夹，同理，也只会解压缩其目录下的压缩文件

# 总结
# 1、*.tar 用 tar -xvf 解压
# 2、*.gz 用 gzip -d或者gunzip 解压
# 3、*.tar.gz和*.tgz 用 tar -xzf 解压
# 4、*.bz2 用 bzip2 -d或者用bunzip2 解压
# 5、*.tar.bz2用tar -xjf 解压
# 6、*.Z 用 uncompress 解压
# 7、*.tar.Z 用tar -xZf 解压
# 8、*.rar 用 unrar e解压
# 9、*.zip 用 unzip 解压

# 单重定向从头开始写文件，使用重定向符来清空一个文件或者创建一个新的空文件
> test.py

# 使用双重定向符来追加写文件
>> test.py

# 返回上一次的目录
cd -
```

### 2.3进程相关

```shell
# 打开应用进程,查看系统调用，排查问题
strace
```

#### 2.3.1杀死进程的几种方式  

```shell
# 知道进程号，直接强制杀死进程
kill -s 9 1024

# ps | grep firefox,直接获得对应的进程id
pgrep firefox
kill ...

# 找到所有关于firefox的进程
# 去掉有grep的进程
# 截取输入行的9-15个字符，即进程的pid
# xargs将前面命令的结果作为kill -s 9的参数并执行
ps -ef | grep firefox | grep -v grep | cut -c 9-15 | xargs kill -s 9

# 上面命令的简化版
pgrep firefox | xargs kill -s 9

# pkill=pgrep + kill
pkill -9 firefox
```

### 2.4网络相关

#### 2.4.1tcpdump网络抓包

- [tcpdump基础教程](https://www.jianshu.com/p/d9162722f189)

- 用于截取网络分组，并输出分组内容的工具
- 针对网络层，协议，主机，网络或者端口的过滤

```shell
# -n 表示不要解析域名，直接显示 ip。
# -nn 不要解析域名和端口
# -X 同时用 hex 和 ascii 显示报文的内容。
# -XX 同 -X，但同时显示以太网头部。
# -S 显示绝对的序列号（sequence number），而不是相对编号。
# -i any 监听所有的网卡
# -v, -vv, -vvv：显示更多的详细信息
# -c number: 截取 number 个报文，然后结束
# -A： 只使用 ascii 打印报文的全部数据，不要和 -X 一起使用。截取 http 请求的时候可以用 sudo tcpdump -nSA port 80！

tcpdump  # 默认启动，会监视第一个网络接口,抓取的结果会很多

tcpdump -i ens33  # 监视指定网络接口的数据包
tcpdump -i ens33 host node1  # 监视指定主机的数据包

tcpdump -i ens33 dst host node1  # 监视所有发送到主机node1的数据包

tcpdump -i ens433 port 8888 and host node1  # 监视指定主机和端口的数据包
```

#### 2.4.2网关相关命令

能够向外部网络转发分组的特殊节点主机叫`网关`。

```shell
# 查看操作系统维护的路由表
# 其包含了关于分组如何转发以及通过
route

# 设置默认网关
route add default gw 192.168.0.1 wlan0

# 查看与远端服务器之间的多个网关或者设备节点，获取分组途径中的所有网关地址
traceroute google.com

# 查看与某个节点的连通性
ping google.com
ping google.com -c 3  # 限制发送的分组的数量

# 查看远程主机的端口是否开放
telnet 106.53.65.70 1935

# 开启和关闭网卡:
# 关闭ens33网卡
sudo ifconfig ens33 down
# 开启ens33网卡
sudo ifconfig ens33 up

# 本地局域网ip为动态分配的
# 修改网卡ip地址(即手动设置ip),不建议手动设置:
sudo ifconfig ens33 192.168.42.130
```

#### 2.4.3curl命令

- [阮一峰curl网站开发指南](http://www.ruanyifeng.com/blog/2011/09/curl.html)

```shell
# curl直接返回html
curl http://www.linux.com

# -i参数可以显示头信息
curl -i http://www.linux.com

# -v参数可以显示一次http通信的全部过程,包括端口连接和http request头信息
curl -v http://www.linux.com
curl --trace output.txt http://www.linux.com  # 获取更详细的通信信息

# 发送表单信息
curl http://example.com?data=xxx  # GET请求直接将数据附在网址后面
curl -X POST --data "data=xxx&&data2=xxx" http://example.com  # POST请求则需要将数据和网址分开，同时用到data参数，POST可以替换为DELETE

# 携带cookie
curl --cookie "name=xxx" http://example.com

# http认证
curl --user name:password http://example.com

# 增加头信息
curl --header "Content-Type:application/json" http://example.com

# 将返回的数据保存
curl -o linux.html http://www.linux.com
curl -O http://www.linux.com/hello.sh  # 保存具体的文件，后面也要接具体的文件路径
curl -o /dev/null -s -w %{http_code} www.linux.com  # 测试网页的返回值

# 查看自己的公网ip
curl -s https://ip.cn
```

#### 2.4.4wget命令

```shell
# wget相关命令
wget http://www.baidu.com  # 将首页下载
wget -x http://www.baidu.com  # 强制建立服务器上一模一样的目录
wget -nd http://www.baidu.com  # 服务器上下载的所有内容加到本地目录

wget -c -t 10 -T 120http://www.baidu.com/a.mp4  # 大文件断点续传，-t表示重试次数，-t 100表示重试100次, -T表示超时等待时间
wget -i downloadlist.txt  # 批量下载，将每一个文件的url写一行
wget -m -accept=mp4 http://www.baidu.com  # 只下载某种类型的文件,-reject表示忽略下载某种类型的文件
```

#### 2.4.5网络其他

```shell
# 监听指定的网络接口并以top形式呈现
iftop
# 快速告知哪些进程在占用带宽
nethlogs
# 轻量级守护进程在后台运行并实时记录网络情况
vnstat

# 打印网络信息，得知整个linux系统的网络情况
netstat -anptu
```

### 2.5其它

```shell
# 定期检查
watch -n 1 -d 'netstat -i | grep tun0'

# 查看上一个命令的返回值
echo $?

# 让shell进程一直阻塞
tail -f /dev/null

# 指定路径升级安装
pip install edgebox -i http://pypi.jiangxingai.com --trusted-host pypi.jiangxingai.com --upgrade

# 设置git的代理
git config --global http.proxy https://localhost:4080

# 使用setup.py打包，生成的.tar.gz的压缩包在当前路径的dist文件夹下
python setup.py sdist

# 对命令的一些命令操作
type ls  # 说明怎么样解释命令ls,即显示命令的类别
man ls  # 显示ls的手册页面
which ls  # 显示会执行哪一个可执行程序, 可执行程序的位置
apropos ls  # 显示ls一系列的适合的命令
info ls  # 显示ls的命令,类似于man
whatis ls  # 显示ls命令的简介描述
alias ls  # 创建ls命令的别名

# 标准输入、输出和错误，shell 内部分别将其称为文件描述符0、1和2
ls / 2> ls-error.txt  # 将执行重定向的错误输出写入到指定文件
ls / ls-output.txt 2>&1  # 将错误和正确的信息都写入到文件，注意2和1的顺序不能乱
ls / 2> /dev/null  # 将输出错误的信息定位到"存储桶"，可以隐藏

# 直接输入不带参数的cat，会等待从标准输入读入数据，默认为键盘，按ctrl+d结束
cat
cat > test.txt  # 复制标准输入到指定文件来创建简单的文件

# 显示文件的行数，字数，字节数
wc test.py

# 打印文件开头部分和结尾部分
head -n 5 test.py  # 打印文件的前5行
tail -n 5 test.py  # 打印文件的结尾5行

# 算术表达式展开
echo $((2 + 2))

# 花括号展开，可以从一个包含花括号的模式中创建多个文本字符串
echo a-{b, c, d}-e
echo num_{1..5}
echo {A..Z}
mkdir {2019..2020}-0{1..12}

last  # 查看登录回话信息
last admin  # 获取单个用户登录回话信息
last reboot  # 查看重启回话信息
lastb  # 获取失败的登录回话信息

# 展示所有进程，无论由什么终端控制
ps x

# 查看文件系统的挂载情况
mount
```

## 8.Linux文件系统

普通文件、目录文件（也就是文件夹）、设备文件、链接文件、管道文件、套接字文件（数据通信的接口）等等。而这些种类繁多的文件被Linux使用目录树进行管理， 所谓的目录树就是以根目录（/）为主，向下呈现分支状的一种文件结构。

`文件系统`是文件被命名，存储，检索以及在存储磁盘或分区上更新的方式;文件在磁盘上的组织方式。文件系统分为两个部分，称为用户数据和元数据 （文件名，创建时间，修改时间，目录层次结构中的大小和位置等）。

三种文件类型，7种文件：

1. 普通文件
2. 目录文件
3. 特殊文件（该类有 5 个文件类型）
   - 链接文件
   - 字符设备文件
   - Socket 文件
   - 命名管道文件
   - 块文件

参考下面的表可以更好地理解 Linux 中的文件类型。

| 符号 | 含义                                      |
| ---- | ----------------------------------------- |
| –    | 普通文件。长列表中以中划线 - 开头。       |
| d    | 目录文件。长列表中以英文字母 d 开头。     |
| l    | 链接文件。长列表中以英文字母 l 开头。     |
| c    | 字符设备文件。长列表中以英文字母 c 开头。 |
| s    | Socket 文件。长列表中以英文字母 s 开头。  |
| p    | 命名管道文件。长列表中以英文字母 p 开头。 |
| b    | 块文件。长列表中以英文字母 b 开头。       |

### 8.1使用tmpfs

`mount -t tmpfs -o size=20m tmpfs /mnt/tmp`

上面这条命令分配了上限为20m的VM到/mnt/tmp目录下，用df命令查看一下，确实/mnt/tmp挂载点显示的大小是20m，但是tmpfs一个优点就是它的大小是随着实际存储的容量而变化的，换句话说，假如/mnt/tmp目录下什么也没有，tmpfs并不占用VM。上面的参数20m只是告诉内核这个挂载点最大可用的VM为20m，如果不加上这个参数，tmpfs默认的大小是RM的一半，假如你的物理内存是128M，那么tmpfs默认的大小就是64M。

由于它的数据是在VM里面，因此断电或者你卸载它之后，数据就会立即丢失。

## 9.linux重要文件

### 9.1/etc/hosts文件

常用的网址域名与其对应的 IP 地址建立一个关联"数据库"，用户在浏览器中输入一个需要登录的网址时，系统会首先自动从hosts文件中寻找对应的 IP 地址，一旦找到，系统就会立即打开对应网页，如果没有找到，则系统会将网址提交 DNS 域名解析服务器进行 IP 地址的解析。

作用：

1. `加快域名解析`
2. `构建映射关系`
3. `屏蔽垃圾网站`

### 9.2/etc/resolv.conf文件

- [linux下的DNS域名解析配置文件](https://blog.csdn.net/u014453898/article/details/62426848)
- `/etc/resolv.conf`文件设置了本地的DNS,指明域名和IP的对应关系，一个域名可以分配多个ip地址，dns服务器只会返回一个。

```shell
# 手动添加名字服务器
echo google.com 172.217.24.14 >> /etc/resolv.conf

# dns查找，列出某个域名的所有ip地址
host google.com

# 查询dns相关的细节信息
nsloopup google.com
```

### 9.3/etc/hosts文件

- [linux下/etc/hosts文件介绍](https://blog.csdn.net/Aempty/article/details/79593625)
- 负责ip地址与域名快速解析的文件，包含ip地址和主机名之间的映射，`没有域名解析服务器的情况下，系统上的所有网络程序都是通过查询该文件来解析对应于某个主机名的ip地址`

## 10.系统监控

```shell
# 报告关于线程、虚拟内存、磁盘、陷阱和 CPU 活动的统计信息
# vmstat参数解释：
# 　　Procs
# 　　r: 等待运行的进程数 b: 处在非中断睡眠状态的进程数 w: 被交换出去的可运行的进程数。此数由 linux 计算得出，但 linux 并不耗尽交换空间
# 　　Memory
# 　　swpd: 虚拟内存使用情况，单位：KB
# 　　free: 空闲的内存，单位KB
# 　　buff: 被用来做为缓存的内存数，单位：KB
# 　　Swap
# 　　si: 从磁盘交换到内存的交换页数量，单位：KB/秒
# 　　so: 从内存交换到磁盘的交换页数量，单位：KB/秒
# 　　IO
# 　　bi: 发送到块设备的块数，单位：块/秒
# 　　bo: 从块设备接收到的块数，单位：块/秒
# 　　System
# 　　in: 每秒的中断数，包括时钟中断
# 　　cs: 每秒的环境(上下文)切换次数
# 　　CPU
# 　　按 CPU 的总使用百分比来显示
# 　　us: CPU 使用时间
# 　　sy: CPU 系统使用时间
# 　　id: 闲置时间
vmstat 2 5
```

## a.其他

### a.1文件改变

***文件在网络传输过程中容易发生变化的部分通常是在文件头或者尾部，可以通过文件的二进制值(notepad++ hex插件)来对比。***

```shell
# 计算文件的md5值，可以来查看文件前后值的变化知道其是否改变
md5sum filename
```

### a.2流量监控工具

```shell
# TX：发送流量
# RX：接收流量
# TOTAL：总流量
# Cumm：运行iftop到目前时间的总流量
# peak：流量峰值
# rates：分别表示过去 2s 10s 40s 的平均流量

# 一般显示
iftop
# 指定待检测的网卡
iftop -i eth0
# 使host信息默认都显示IP
iftop -n
```

### a.3使用crontab开启定时任务

- [crontab-generator](https://crontab-generator.org/)
- [crontab guru](https://crontab.guru/)

使用crontab的步骤：

1. 开启服务(`sudo service cron start`)
2. 编写cron调度任务(`vim tonycron`)
3. 将条目加入任务列表(`crontab tonycron`)
4. 任务自动开始

```txt
新增调度任务可用两种方法:
1)、在命令行输入: crontab -e 然后添加相应的任务，wq存盘退出。
2)、直接编辑/etc/crontab 文件，即vi /etc/crontab，添加相应的任务。
crontab -e配置是针对某个用户的，而编辑/etc/crontab是针对系统的任务
```

crontab调度任务:

```shell
# 建立一个比如tonycron的文件，加入下面的内容
# 每隔一分钟执行一次脚本,注意需要使用绝对路径
*/1 * * * * /test.sh
```

```shell
# crontab命令的一般格式
# -u 用户名
# -l 列出crontab文件中的内容
# -r 删除crontab的文件
crontab [-u user] -e -l -r

# 查看简介
crontab -e
# 开启cron的服务(可能为service crond start)
service cron start
# 使用特定的cron配置文件来
crontab /crontab_config.txt
# 查看当前用户的crontab任务列表
crontab -l
# 指定编辑器来增删文件内容来更改crontab文件
crontab -e

# 提交创建的crontab文件，之后其就会定时执行
crontab tonycron
```

### a.4ssh文件传输

**设置ssh的自动化认证：**

```shell
# 1.进入.sh
cd ~/.ssh

# 2.创建ssh秘钥,指定加密算法为rsa,生成公钥id_rsa.pub和私钥id_rsa
ssh-keygen -t rsa

# 3.将公钥加入到远程服务器~/.ssh/authorized_keys文件中
ssh USERNAME@REMOTE_HOST "cat >> ~/.ssh/authorized_keys" < ~./ssh/id_rsa.pub

# 4.可以直接ssh连接到那台远程服务器了
```

**使用sshfs设置本地挂载点挂载远程驱动器：**

```shell
# 将远程的/home挂载到本地的/mnt/e
sshfs USERNAME@REMOTE_HOST:/home /mnt/e

# 卸载本地的挂载点
umount /mnt/e
```

**ssh端口转发：**

```shell
# 下载插件，设置代理: 代理协议 SOCKS5 代理服务器 127.0.0.1 代理端口 1080
https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif

# 本地执行ssh命令来和远端的服务器建立信道
ssh -D localhost:1080 ubuntu@sgcc.jiangxingai.com

# 本地浏览器即可访问远程的即使未开放的端口
http://172.16.16.14:5920
```

### a.5有趣命令

```shell
# 小火车
sl

# 输出笑话，名人名言什么的
fortune

# 用ascii码打印字符画，还可以用其他的动物
cowsay "i am cow"
fortune | cowsay

# 矩阵代码效果
cmatrix

# 艺术字生成，字符文字
figlet fuck you !

# 出现一只跟着鼠标的猫
oneko
```
