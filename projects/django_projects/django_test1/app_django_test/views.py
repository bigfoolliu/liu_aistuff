from django.shortcuts import render

# Create your views here.
# 自己添加的hello world视图
from django.http import HttpResponse, Http404
import datetime
from django.shortcuts import render  # 用于渲染模板文件


def hello(request):
	"""
	一个hello视图函数
	:param request:
	:return:
	"""
	# 返回一个HttpResponse对象,里面包含一段文本
	return HttpResponse("Hello world.")


def show_time(request):
	"""
	返回当前的时间
	:param request:
	:return:
	"""
	return HttpResponse(datetime.datetime.now())


# def plus_time(request, offset):
# 	"""
# 	增加几个小时
# 	:param request:
# 	:param offset: 时间超出小时数
# 	:return:
# 	"""
# 	try:
# 		offset = int(offset)
# 	except ValueError:
# 		raise Http404()
# 	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
# 	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
# 	return HttpResponse(html)


def temp1(request):
	"""
	首次模板文件使用的测试
	:param request:
	:return:
	"""
	# 创建替换模板文件中hello变量的内容
	context = {"hello": "hello world,这是第一个模板文件的测试使用"}
	# 将内容替换给模板文件并渲染模板文件
	return render(request, "app_django_test/temp1.html", context)


# 在自己创建的表中添加内容
from app_django_test import models


def db_handle(request):
	"""
	处理数据库
	:param request:
	:return:
	"""
	# 向Author表中添加一个实例,并且每一次刷新访问的页面的时候就会添加一次
	# models.Author.objects.create(first_name='tony', last_name='stark', email='tony@qq.com')

	# 删除某一条数据
	# models.Author.objects.filter(id=1).delete()

	# 修改某一条数据
	# models.Author.objects.filter(id=1).update(email='tony1@qq.com')

	# 查询数据,可以将结果显示在某一个网页上
	author_list_obj = models.Author.objects.all()
	return render(request, 'app_django_test/db_handle.html', {'li': author_list_obj})


	# return HttpResponse('OK')
