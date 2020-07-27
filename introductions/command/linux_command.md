# LINUX平台下的常用命令

<!-- vim-markdown-toc Marked -->

* [1.系统管理](#1.系统管理)
        * [1.1系统时间(tzselect, uptime)](#1.1系统时间(tzselect,-uptime))
        * [1.2系统信息(free, lsusb, v4l2-ctl, cpuinfo, udevadm)](#1.2系统信息(free,-lsusb,-v4l2-ctl,-cpuinfo,-udevadm))
        * [1.3系统用户(id, passwd, uname, last, useradd, userdel, groupadd)](#1.3系统用户(id,-passwd,-uname,-last,-useradd,-userdel,-groupadd))
* [2.文件目录管理](#2.文件目录管理)
        * [2.1目录基本操作(ls, tree, cd, dirs, pushd, popd)](#2.1目录基本操作(ls,-tree,-cd,-dirs,-pushd,-popd))
        * [2.2文件信息(fuser, du, file, less)](#2.2文件信息(fuser,-du,-file,-less))
        * [2.3文件查找和比较(find, ag, wc, grep)](#2.3文件查找和比较(find,-ag,-wc,-grep))
        * [2.4文件归档(tar, gzip, gunzip, extract)](#2.4文件归档(tar,-gzip,-gunzip,-extract))
        * [2.x文件其他(>, >>, ln)](#2.x文件其他(>,->>,-ln))
* [3.进程相关](#3.进程相关)
        * [3.1杀死进程的几种方式](#3.1杀死进程的几种方式)
        * [3.2supervisor对进程进行管理](#3.2supervisor对进程进行管理)
* [4.网络管理](#4.网络管理)
        * [4.1网络抓包(tcpdump)](#4.1网络抓包(tcpdump))
        * [4.2网络服务器(ifconfig, route)](#4.2网络服务器(ifconfig,-route))
        * [4.3网络应用(curl, wget, telnet, ping)](#4.3网络应用(curl,-wget,-telnet,-ping))
        * [4.5网络其他](#4.5网络其他)
* [5.实用工具](#5.实用工具)
        * [5.1dos2unix](#5.1dos2unix)
        * [5.2watch](#5.2watch)
        * [5.3jq](#5.3jq)
        * [5.4when-changed工具](#5.4when-changed工具)
        * [5.5ranger](#5.5ranger)
        * [5.6sed](#5.6sed)
        * [5.7pandoc](#5.7pandoc)
        * [5.x其他](#5.x其他)
* [性能检测与优化](#性能检测与优化)
        * [ifstat](#ifstat)

<!-- vim-markdown-toc -->

## 1.系统管理

### 1.1系统时间(tzselect, uptime)

- [linux命令详解网站](https://man.linuxde.net)

```sh
# 设置系统默认的UTC时间为Shanghai时间
tzselect
TZ='Asia/Shanghai'
export TZ

# 查看系统运行的时间
uptime
```

### 1.2系统信息(free, lsusb, v4l2-ctl, cpuinfo, udevadm)

```sh
# 查看内存情况
free -mh

uname -a  # 查看系统信息
lsb_release -a  # 简洁的显示系统信息的命令

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
```

### 1.3系统用户(id, passwd, uname, last, useradd, userdel, groupadd)

```sh
id  # 展示当前用户的身份号
passwd user1  # 更改用户密码

last  # 查看用户登入情况

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

## 2.文件目录管理

### 2.1目录基本操作(ls, tree, cd, dirs, pushd, popd)

```sh
ls -t  # 列举当前文件夹下所有目录和文件并以时间排列
ls -u  # 以文件上次被访问的时间排序
ls -S  # 以文件大小排序

ls -lh  # 显示文件大小
ls -lhS  # 从大到小排列
ls -d */  # 只列出文件夹
ls -i  # 带索引号显示
ls -t  # 按照修改时间显示，新文件在前

ls -t | cat -n  # 按照时间排序,且给每一个文件编号

# 返回上一次的目录
cd -
# 快速目录切换
# dirs显示目录栈,索引为0的始终为当前目录
# pushd将目录压入目录栈
# popd将目录弹出栈
dirs -p  # 每行显示一条记录
dirs -v  # 每行显示一条记录，并显示index
dirs -c  # 清空目录栈

pushd  # 目录栈索引为0和1调换，所以同时当前目录切换为之前索引为1的目录
pushd +2  # 切换到目录栈index为2的目录(使用)
pushd -2  # 切换为目录栈倒数为2的目录

popd  # 目录栈栈顶元素出栈，所以目录会切换到之前索引为1的目录
popd +2  # 索引为2的目录弹出
popd -2  # 倒数为2的目录弹出

# tree递归展示
tree -a  # 显示所有文件，包含隐藏文件
tree -d  # 仅展示目录
tree -N ./  # 若有中文字符的话可以显示中文文件名
tree -L 2 ./  # 展示的目录深度为2
```

### 2.2文件信息(fuser, du, file, less)

```sh
# 查看文件占用
fuser -s file  # 查看文件是否被其他进程占用(持续写入状态，vi打开不是), 返回值为1则为被占用，0则为未被占用
fuser -v file  # 查看文件的具体占用信息，包括占用进程的 USER, PID 等

# 查看当前文件文件以及目录占用空间情况
du -sh ./*

# 查看文件夹占据磁盘大小以及根据文件夹的大小排序
du -hs /data/
du -hs /data/ | sort -n

# 查看目录下的文件夹占用空间情况
du -h --max-depth=1 /data/

# du的替代工具,更好的使用体验
ncdu

# 查看文件信息
file test.py

# 以可以滚动翻页的方式查看文件
less test.py
```

### 2.3文件查找和比较(find, ag, wc, grep)

```sh
# 文件查找
find . -name "*.sh" -print  # 根据文件名查找文件,在当前目录下查找*.sh并将其输出
find . -ctime 1 -type f -print  # 查找过去 1 小时修改过的普通文件
find . -ctime 10 -type d -print  # 查找过去 10 分钟修改过的目录
find . -size +10M -type f -print  # 查找文件大小超过 10（b/c/w/k/M/G）的文件
find . -path ./test -prune -o -print  # 查找文件的时候避开当前目录下的test文件夹

# 统计当前路径下所有.py文件的个数
find ./ -name "*.py" | wc -l
find ./ -name "*.py" | wc -l

# 统计当前路径下所有.py文件各自的行数
find ./ -name "*.py" | xargs wc -l
find ./ -name "*.py" | xargs wc -l

# 查找文件并用file查看详细信息
find ./ -name "core*" | xargs file

# 更快的搜索
ag <something>
ag <something> ./  # 指定文件夹搜索

# 递归的统计一目录下及其子目录下所有匹配文件的总的行数和每个文件的行数，可以使用一下命令
wc -l `find ./ -name "*.csv"`

# 用grep直接搜索文件中的文本内容
grep -i 'Out of Memory' /var/log/messages
```

### 2.4文件归档(tar, gzip, gunzip, extract)

```sh
# 使用tar进行文件归档
tar -cf out.tar file1 file2 `folder1  # f表示指定tar文件名必须在参数最后，c表示新建一个tar包
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

extract  # 万能的解压(基于zsh的插件)
```

### 2.x文件其他(>, >>, ln)

```sh
# 单重定向从头开始写文件，使用重定向符来清空一个文件或者创建一个新的空文件
> test.py

# 使用双重定向符来追加写文件
>> test.py

# 给文件建立别名
ln a.txt aa.txt  # 硬连接，删除一个，仍能找到
ln -s a.txt aa.txt  # 符号连接(软连接)，删除源头，另一个无法使用
```

## 3.进程相关

```sh
# 打开应用进程,查看系统调用，排查问题
strace
```

### 3.1杀死进程的几种方式

```sh
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

### 3.2supervisor对进程进行管理

```sh
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

## 4.网络管理

### 4.1网络抓包(tcpdump)

- [tcpdump基础教程](https://www.jianshu.com/p/d9162722f189)

- 用于截取网络分组，并输出分组内容的工具
- 针对网络层，协议，主机，网络或者端口的过滤

```sh
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

### 4.2网络服务器(ifconfig, route)

```sh
# 查看操作系统维护的路由表
# 其包含了关于分组如何转发以及通过
route

# 设置默认网关
route add default gw 192.168.0.1 wlan0

# 查看与远端服务器之间的多个网关或者设备节点，获取分组途径中的所有网关地址
traceroute google.com

# 开启和关闭网卡:
# 关闭ens33网卡
sudo ifconfig ens33 down
# 开启ens33网卡
sudo ifconfig ens33 up

# 本地局域网ip为动态分配的
# 修改网卡ip地址(即手动设置ip),不建议手动设置:
sudo ifconfig ens33 192.168.42.130
```

### 4.3网络应用(curl, wget, telnet, ping)

- [阮一峰curl网站开发指南](http://www.ruanyifeng.com/blog/2011/09/curl.html)

```sh
# curl命令
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

# wget相关命令
wget http://www.baidu.com  # 将首页下载
wget -x http://www.baidu.com  # 强制建立服务器上一模一样的目录
wget -nd http://www.baidu.com  # 服务器上下载的所有内容加到本地目录

wget -c -t 10 -T 120http://www.baidu.com/a.mp4  # 大文件断点续传，-t表示重试次数，-t 100表示重试100次, -T表示超时等待时间
wget -i downloadlist.txt  # 批量下载，将每一个文件的url写一行
wget -m -accept=mp4 http://www.baidu.com  # 只下载某种类型的文件,-reject表示忽略下载某种类型的文件

# telnet命令
# 查看远程主机的端口是否开放
telnet 106.53.65.70 1935

# pin命令
# 查看与某个节点的连通性
ping google.com
ping google.com -c 3  # 限制发送的分组的数量
```

### 4.5网络其他

```sh
# 监听指定的网络接口并以top形式呈现
iftop
# 快速告知哪些进程在占用带宽
nethlogs
# 轻量级守护进程在后台运行并实时记录网络情况
vnstat

# 打印网络信息，得知整个linux系统的网络情况
netstat -anptu

# 查询DNS的记录，查看域名解析是否正常，在网络故障的时候用来诊断网络问题
# https://www.cnblogs.com/yonghegn/p/10059997.html
nslookup -q=TXT coding3min.com
```

## 5.实用工具

### 5.1dos2unix

- 将windows中的文件转义为unix格式

```sh
# 单个文件转换
dos2unix windows.txt

# 同时数个文件转换
dos2unix 1.txt, 2.txt

# 批量转换
find ./ -name "*.md" | args dos2unix
```

### 5.2watch

- 没有选项的情况下每隔2秒执行一次
- -n 为时间间隔
- -d 为执行的命令

```sh
# 定期检查
watch -n 1 -d 'netstat -i | grep tun0'

watch date
```

### 5.3jq

- json格式化工具

```sh
# 输出file.json格式后的内容
jq . file.json

# 等价于上式
cat file.json | jq .
cur xxx | jq .

# 将结果写入到新文件
jq . file.json | >> new_file.json
```

### 5.4when-changed工具

- 监控文件的变化来执行相应的操作

```sh
# 安装
pip3 install when-changed

todo:

```

### 5.5ranger

- [ranger使用介绍](https://blog.csdn.net/function_dou/article/details/88909110)
- 类似于vim的操作
- 也可使用鼠标

### 5.6sed

- 流编辑，处理数据之前需要预先提供一组规则
- sed 默认不会直接修改源文件数据，而是会将数据复制到缓冲区中，修改也仅限于缓冲区中的数据
- [sed命令介绍](https://www.cnblogs.com/zhangzongjian/p/10708222.html)

### 5.7pandoc

- 文档格式转换

```sh
# markdown格式转换为html格式
pandoc a.md -o a.html
```

### 5.x其他

```sh
# 查看上一个命令的返回值
echo $?

# 让shell进程一直阻塞
tail -f /dev/null

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
cat -n a.txt  # 查看的时候同时显示行号

# 显示文件的行数，字数，字节数
wc test.py

# 打印文件开头部分和结尾部分
head -n 5 test.py  # 打印文件的前5行
tail -n 5 test.py  # 打印文件的结尾5行

tail -f spider.log  # 动态显示文本的最新信息

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


# 有趣命令

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

# 查找单词意思
curl v2en.co/cool
curl v2en.co/shut%20down  # 查找词组
```

## 性能检测与优化

### ifstat

```sh
ifstat -tTz
```
