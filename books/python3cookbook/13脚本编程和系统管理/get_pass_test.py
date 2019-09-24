#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
弹出一个密码提示输入框(输入的字符不可见),输入密码

注意在前面代码中 getpass.getuser() 不会弹出用户名的输入提示。它会根据该
用户的 shell 环境或者会依据本地系统的密码库（支持 pwd 模块的平台）来使用当前用
户的登录名，
如果你想显示的弹出用户名输入提示，使用内置的 input 函数
"""
import getpass

user = getpass.getuser()
passwd = getpass.getpass()


def svc_login(user, passwd):
    if user == "tonyliu" and passwd == "hahaha":
        return True
    else:
        return False


if svc_login(user, passwd):
    print("Passed")
else:
    print("Denied")
