#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
发邮件

执行发送邮件的耗时代码
"""
from django.conf import settings

from celery_tasks.main import app
from django.core.mail import send_mail  # django自带发送邮件的功能

# import smtplib
# import email


# host = ""  # smtp的远程服务器主机
# port = 25  # smtp默认的端口号设置为25
# local_hostname = ""  #  如果 SMTP 在你的本机上，你只需要指定服务器地址为 localhost 即可

# # 构建对象然后发送邮件
# smtp_obj = smtplib.SMTP(host=host, port=port, local_hostname=local_hostname)
# smtp_obj.sendmail(from_addr="", to_addrs="", msg="", mail_options=[])


"""
用celery事项框架异步的配置文件
"""

# 指定代理人,此处redis的数据库开始倒着用
broker_url = 'redis://127.0.0.1:6379/15'


"""
用于创建celery对象
"""

from celery import Celery

# 为celery使用django配置文件进行设置,注意下面配置的路径
import os
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'MeiDuo.settings.dev'

# 创建celery应用,名字可以随便写
app = Celery('MeiDuo')

# 导入celery配置
app.config_from_object('celery_tasks.config')

# 自动注册celery任务(sms包名)
app.autodiscover_tasks([
    'celery_tasks.sms',
    'celery_tasks.email',
])


@app.task(name='send_verify_email')
def send_verify_email(to_email, verify_url):
    """
    发送验证邮件
    :param to_email: 目的邮箱
    :param verify_url: 邮件中的验证url
    :return:
    """
    print(verify_url)  # TODO: 测试

    # 配发送的邮件的内容
    subject = '美多商城验证'  # 邮件主题
    # 发送的html邮件内容
    html_message = '<p>你好!</p>' \
                   '<p>感谢使用美多商城.</p>' \
                   '<p>您的邮箱为: %s</p>' \
                   '<p>点此链接激活您的邮箱:</p>' \
                   '<p><a href="%s">%s</a></p>' % (to_email, verify_url, verify_url)

    # 使用django自带的email功能发送邮件,此句为耗时代码
    send_mail(subject, '', settings.EMAIL_FROM, [to_email], html_message=html_message)