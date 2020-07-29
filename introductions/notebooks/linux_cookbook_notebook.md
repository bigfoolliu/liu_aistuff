# 鸟哥的私房菜之服务器架设篇读书笔记

<!-- vim-markdown-toc Marked -->

* [介绍](#介绍)

<!-- vim-markdown-toc -->

## 介绍

网络-->服务器-->内部防火墙-->服务配置-->内部权限-->档案权限

```sh
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
