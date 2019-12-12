"""django_test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


# 增加一个映射,简化path后面的处理函数的书写
from app_django_test.views import *
# 增加app_polls中的urls.py映射
from django.conf.urls import include

# app_login视图url注册
from app_login.views import *

# 增加一个路径,所有指向url/hello的请求都由hello函数处理
urlpatterns = [
	path('admin/', admin.site.urls),  # 后台登录管理
	path('app_django_test/', include('app_django_test.urls')),
	path('app_polls/', include('app_polls.urls')),  # include相当于多级路由,将接收到的url传给下一级路由
	path('index/', index),
	path('login/', login),
	path('logout/', logout),
	path('register/', register),
]
