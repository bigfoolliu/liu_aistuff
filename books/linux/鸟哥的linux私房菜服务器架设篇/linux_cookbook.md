# 鸟哥的私房菜之服务器架设篇读书笔记

<!-- TOC -->

- [鸟哥的私房菜之服务器架设篇读书笔记](#%e9%b8%9f%e5%93%a5%e7%9a%84%e7%a7%81%e6%88%bf%e8%8f%9c%e4%b9%8b%e6%9c%8d%e5%8a%a1%e5%99%a8%e6%9e%b6%e8%ae%be%e7%af%87%e8%af%bb%e4%b9%a6%e7%ac%94%e8%ae%b0)
  - [介绍](#%e4%bb%8b%e7%bb%8d)

<!-- /TOC -->

## 介绍

网络-->服务器-->内部防火墙-->服务配置-->内部权限-->档案权限

```shell
# 创建分组
groupadd <group-name>

# 创建用户并将其加入指定的组内
useradd -G <group-name> <user-name>

# 查看用户的分组信息
id <user-name>

# 将某个目录共享给某个组
chgrp <group-name> <dir-path>
chmod 2770 <dir-path>
```

TODO:用户的磁盘大小控制
TODO:文件系统的放大,即将某盘扩容
