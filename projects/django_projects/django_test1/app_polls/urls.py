#!-*-coding:utf-8-*-
# !@Date: 2018/9/9 22:00
# !@Author: Liu Rui
# !@github: bigfoolliu


# 自建的urls.py文件,可以在项目中的urls.py指向此处
# from django.conf.urls import url
# from . import views

# from django.contrib import admin
from django.urls import path, re_path
from app_polls.views import *
# 使用URLconf的命名空间,便于区分多个app之间的URL name
from django.conf.urls import url


# 增加该变量,以后不同app之间的模板url name引用将更加清晰
app_name = 'app_polls'

urlpatterns = [
	# path('index/', index, name='index'),
	# re_path(r'^$', index, name='index'),
	# re_path(r'^(?P<question_id>[0-9]+)/$', detail, name='detail'),
	# re_path(r'^(?P<question_id>[0-9]+)/results/$', results, name='results'),
	# re_path(r'^(?P<question_id>[0-9]+)/vote/$', vote, name='vote'),

	# 为了使用类视图,修改URLConf重新设置
	re_path(r'^$', IndexView.as_view(), name='index'),
	re_path(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail'),
	re_path(r'^(?P<pk>[0-9]+)/results/$', ResultsView.as_view(), name='results'),
	re_path(r'^(?P<question_id>[0-9]+)/vote/$', vote, name='vote'),
]
