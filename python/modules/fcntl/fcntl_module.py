#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
fcntl模块的使用

给文件加锁，linux系统下

- https://www.jb51.net/article/154555.htm
- https://blog.csdn.net/wohu1104/article/details/88541524


fcntl.flock(f.fileno(), operation)

operation 的操作包括以下选项：

1. fcntl.LOCK_EX
    排他锁：除加锁进程外其他进程没有对已加锁文件读写访问权限

2. fcntl.LOCK_UN
    解锁：对加锁文件进行解锁

3. fcntl.LOCK_SH
    共享锁：所有进程都没有写权限，即使加锁进程也没有，但所有进程都有读权限

4. fcntl.LOCK_NB
    非阻塞锁：如果指定此参数，函数不能获得文件锁就立即返回，否则，函数会等待获得文件锁。

LOCK_NB可以同LOCK_SH或LOCK_NB进行按位或（|）运算操作。
"""

import fcntl
import sys
import time


class Flock(object):
    """给文件加锁的类"""

    def __init__(self, file_name):
        """
        :param file_name: 待加锁的文件名称
        """
        self.file_name = file_name
        self.f_obj = open(self.file_name, "wb")
        self.fd = self.f_obj.fileno()  # 将文件流指针转化为文件描述符
    
    def lock(self):
        """
        锁定文件
        锁定成功之后将不能对文件写操作
        """
        try:
            fcntl.lockf(self.fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            print("正在锁定文件 {}...".format(self.file_name))
            time.sleep(30)
            return True
        except Exception as e:
            print("锁定文件 {}异常：{}".format(self.file_name, e))
            return False
    
    def unlock(self):
        """解锁文件"""
        self.f_obj.close()
        print("文件{}已经解锁".format(self.file_name))


if __name__ == "__main__":
    locker = Flock(sys.argv[1])
    a = locker.lock()
    if a:
        print("文件已经加锁")
    else:
        print("无法锁定文件")
