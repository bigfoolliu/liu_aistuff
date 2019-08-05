#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
发邮件
"""
import smtplib
import email


host = ""  # smtp的远程服务器主机
port = 25  # smtp默认的端口号设置为25
local_hostname = ""  #  如果 SMTP 在你的本机上，你只需要指定服务器地址为 localhost 即可

smtp_obj = smtplib.SMTP(host=host, port=port, local_hostname=local_hostname)
smtp_obj.sendmail(from_addr="", to_addrs="", msg="", mail_options=[])
