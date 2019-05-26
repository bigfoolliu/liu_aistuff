# linux 相关命令

切换当前使用的python版本: sudo update-alternatives --config python

设置python使用的优先级: sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 100

完全卸载python：sudo apt-get remove --purge python3.4

hostname -f     显示完整的主机名和域名
hostname -i     显示当前机器的ip地址

ping baidu.com          发送ECHO＿REQUEST包到指定的地址,连续不断
ping -c 4 baidu.com     指定发送的包的个数为4

tracepath baidu.com     追踪到指定目的地址的网络路径，并给出在路径上的每一跳

mtr baidu.com       持续发包并显示每一跳ping所用的时间

host google.com     DNS查询，参数是域名则会给出关联ip,参数为ip则输出关联域名

whois google.com    输出指定站点的whois记录，查到该站点的一些相关信息

ifplugstatus        产看所有的网络接口的状态，或者指定网络接口的状态

netstat         显示网络接口的信息，包括打开的socket和路由表
netstat -p      显示打开的socket对应的程序

telnet 192.168.120.209          通过telnet协议来连接目标主机

dpkg --list     显示所有已经安装的程序
sudo apt-get remove `programe`      删除程序但是保留配置文件
sudo apt-get --purge remove `programe`      REMOVE THE PROGRAME AND THE CONFIG FILE

sudo apt-get update     更新源
sudo apt-get upgrade `programe`     升级软件

tree -a     展示当前目录所有的文件
tree -d     只展示目录
tree -f     展示的同时输出文件的路径

id      显示当前的用户信息，0的权限最高
echo $SHELL     确定当前使用的是哪一个shell

touch `date +%Y-%m-%d_%H:%M:%S`.txt     创建一个当前时间的文件

ls -l | grep "^-" | wc -l       显示当前文件夹中的文件数量
ls -l | grep "^d" | wc -l       显示当前文件夹中的文件夹数量

tar -xvf <file.tar>     解压tar包
tar -xzvf <file.tar.gz>     解压tar.gz
tar -xjvf <file.tar.bz2>        解压tar.bz2