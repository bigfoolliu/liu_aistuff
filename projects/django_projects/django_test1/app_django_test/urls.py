#!-*-coding:utf-8-*-
# !@Date: 2018/9/9 22:07
# !@Author: Liu Rui
# !@github: bigfoolliu


# 自建的urls.py文件,即二级路由,尽量在每一个app中创立
from django.conf.urls import url
from . import views

from django.contrib import admin
from django.urls import path
from app_django_test.views import *


urlpatterns = [
	path('hello/', hello),  # hello world页面
	path('time/', show_time),  # 显示当前时间
	# path(r'time/plus/([1,9])/', plus_time),  # 时间偏差
	path('temp1/', temp1),  # 模板文件首次测试使用
	path('db_handle/', db_handle),
]
