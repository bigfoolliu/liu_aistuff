#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
os模块的使用
"""

import os
import stat
import subprocess


def access_demo():
    """
    检验权限模式
    os.F_OK: 作为access()的mode参数，测试path是否存在。
    os.R_OK: 包含在access()的mode参数中 ， 测试path是否可读。
    os.W_OK 包含在access()的mode参数中 ， 测试path是否可写。
    os.X_OK 包含在access()的mode参数中 ，测试path是否可执行

    https://www.cnblogs.com/yuanqiangfei/p/8109991.html
    """
    print(os.access("/mnt/d", mode=os.F_OK))
    print(os.access("./os_module.py", mode=os.X_OK))


def chdir_demo():
    """
    切换当前工作目录
    """
    print(os.getcwd())
    print(os.chdir("../"))
    print(os.getcwd())


def chflags_demo():
    """
    设置路径的标记为数字标记，只支持Unix下使用
    flags -- 可以是以下值：

    stat.UF_NODUMP: 非转储文件
    stat.UF_IMMUTABLE: 文件是只读的
    stat.UF_APPEND: 文件只能追加内容
    stat.UF_NOUNLINK: 文件不可删除
    stat.UF_OPAQUE: 目录不透明，需要通过联合堆栈查看
    stat.SF_ARCHIVED: 可存档文件(超级用户可设)
    stat.SF_IMMUTABLE: 文件是只读的(超级用户可设)
    stat.SF_APPEND: 文件只能追加内容(超级用户可设)
    stat.SF_NOUNLINK: 文件不可删除(超级用户可设)
    stat.SF_SNAPSHOT: 快照文件(超级用户可设)
    """
    ret = os.chflags("./test.txt", flags=stat.UF_NOUNLINK)
    print(ret)


def chmod_demo():
    """
    更改权限
    flags -- 可用以下选项按位或操作生成， 目录的读权限表示可以获取目录里文件名列表， ，执行权限表示可以把工作目录切换到此目录 ，删除添加目录里的文件必须同时有写和执行权限 ，文件权限以用户id->组id->其它顺序检验,最先匹配的允许或禁止权限被应用。

    stat.S_IXOTH: 其他用户有执行权0o001
    stat.S_IWOTH: 其他用户有写权限0o002
    stat.S_IROTH: 其他用户有读权限0o004
    stat.S_IRWXO: 其他用户有全部权限(权限掩码)0o007
    stat.S_IXGRP: 组用户有执行权限0o010
    stat.S_IWGRP: 组用户有写权限0o020
    stat.S_IRGRP: 组用户有读权限0o040
    stat.S_IRWXG: 组用户有全部权限(权限掩码)0o070
    stat.S_IXUSR: 拥有者具有执行权限0o100
    stat.S_IWUSR: 拥有者具有写权限0o200
    stat.S_IRUSR: 拥有者具有读权限0o400
    stat.S_IRWXU: 拥有者有全部权限(权限掩码)0o700
    stat.S_ISVTX: 目录里文件目录只有拥有者才可删除更改0o1000
    stat.S_ISGID: 执行此文件其进程有效组为文件所在组0o2000
    stat.S_ISUID: 执行此文件其进程有效用户为文件所有者0o4000
    stat.S_IREAD: windows下设为只读
    stat.S_IWRITE: windows下取消只读
    """
    ret1 = os.chmod("./test.txt", mode=stat.S_IXUSR)
    print(ret1)
    subprocess.run("ls -al", shell=True)

    ret2 = os.chmod("./test.txt", mode=stat.S_IRWXU)
    print(ret2)
    subprocess.run("ls -al", shell=True)


def chown_demo():
    """
    更改文件所有者
    id root: 查看root用户所属的组id和用户id
    cat /etc/passwd：查看当前计算机所有用户
    """
    subprocess.run("grep")


def path_demo():
    """
    os.path示例

    os.path.exists
    os.path.expanduser
    os.path.isdir
    os.path.isfile
    os.path.islink
    os.path.isabs
    os.path.join
    os.path.basename
    os.path.dirname
    os.path.samefile
    os.path.splitext
    """
    pass


if __name__ == "__main__":
    # access_demo()
    # chdir_demo()
    # chflags_demo()
    chmod_demo()
