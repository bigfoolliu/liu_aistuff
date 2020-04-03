# Linux相关知识

<!-- vim-markdown-toc Marked -->

* [1.进程](#1.进程)
        * [1.1进程信息](#1.1进程信息)
        * [1.2僵尸进程(zombie process)](#1.2僵尸进程(zombie-process))
        * [1.3几个与开关进程有关的标准信号](#1.3几个与开关进程有关的标准信号)
        * [1.4supervisor进程管理](#1.4supervisor进程管理)
* [8.Linux文件系统](#8.linux文件系统)
        * [8.1使用tmpfs](#8.1使用tmpfs)
* [9.linux重要文件](#9.linux重要文件)
        * [9.1/etc/hosts文件](#9.1/etc/hosts文件)
        * [9.2/etc/resolv.conf文件](#9.2/etc/resolv.conf文件)
        * [9.3/etc/hosts文件](#9.3/etc/hosts文件)
* [10.系统监控](#10.系统监控)
* [a.其他](#a.其他)
        * [a.1文件改变](#a.1文件改变)
        * [a.2流量监控工具](#a.2流量监控工具)
        * [a.3使用crontab开启定时任务](#a.3使用crontab开启定时任务)
        * [a.4ssh文件传输](#a.4ssh文件传输)
        * [a.5有趣命令](#a.5有趣命令)

<!-- vim-markdown-toc -->

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
