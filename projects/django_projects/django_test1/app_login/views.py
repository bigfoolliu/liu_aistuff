from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect

from app_login.models import *

from app_login.forms import *


def index(request):
	""""""
	pass
	return render(request, 'app_login/index.html')


def login(request):
	"""用户的表单中的账号和密码post到该函数进行处理"""
	# 使用session,request中带有session属性
	# 如果用户处于登录状态,就直接重定向至index页面,可以使用户不会多次登录
	if request.session.get('is_login', None):
		return redirect('/index/')

	if request.method == 'POST':
		# 确保当数据请求中没有username键时不会抛出异常，而是返回一个我们指定的默认值None
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		message = "所有字段都需要填写!"

		if username and password:  # 如果两者都不为空
			username = username.strip()  # 将用户名中不易发现的空格去掉
			# 各种账号和密码验证写在这里
			try:
				# 使用django的ORM去数据库中查询用户数据,用户名匹配之后再去对比密码
				user = Users.objects.get(name=username)  # 基础的django查询api
				# 验证成功,表单提交之后就不能继续停留在登录界面,需要跳转
				if user.password == password:
					# 如果登录成功,则修改session的内容,而session的本质类似于一个字典
					# session内部的数据完全是自定义的,可以和用户有关,也可以和用户无关,不需要事先定义
					request.session['is_login'] = True
					request.session['user_id'] = user.id
					request.session['user_name'] = user.name
					return redirect('/index/')
				else:
					message = "密码不正确!"
			except:  # 未匹配到用户名
				message = "用户不存在!"
		return render(request, 'app_login/login.html', {"message": message})

	return render(request, 'app_login/login.html')


def register(request):
	"""注册视图函数"""
	# 用户已经登录则不允许注册
	if request.session.get('is_login', None):
		return redirect('/index/')

	# 用户想要注册
	if request.method == 'POST':
		# 创建一个表单
		register_form = RegisterForm(request.POST)
		message = "请检查填写的内容!"
		if register_form.is_valid():  # 如果表单正确,获取表单里面的数据
			username = register_form.cleaned_data['user_name']
			password1 = register_form.cleaned_data['password1']
			password2 = register_form.cleaned_data['password2']
			email = register_form.cleaned_data['email']
			sex = register_form.cleaned_data['sex']
			if password1 != password2:  # 两次输入的密码不同
				message = "两次输入的密码不同"
				# locals()函数的作用:
				return render(request, 'app_login/register.html', locals())
			else:
				same_name_user = Users.objects.filter(name=username)
				if same_name_user:  # 用户名唯一
					message = "用户已经存在,需重新选择用户名!"
					return render(request, 'app_login/register.html', locals())
				same_email_user = Users.objects.filter(email=email)
				if same_email_user:  # 邮箱地址唯一
					message = "该邮箱已被注册,需重新选择邮箱!"
					return render(request, 'app_login/register.html', locals())

				# 所有情况都数据都准确的情况下,创建新用户
				new_user = Users()
				new_user.name = username
				new_user.password = password1
				new_user.email = email
				new_user.sex = sex
				new_user.save()  # 保存该用户至数据库
				return redirect('/login/')  # 自动跳转至登录页面
	register_form = RegisterForm()
	return render(request, 'app_login/register.html', locals())


def logout(request):
	"""登出视图函数"""
	# 如果用户未登录,就不用登出了
	if not request.session.get('is_login', None):
		return redirect('/index/')
	# 直接销毁session会话内容,包括其中的cookie和相关数据,从而达到登出效果
	request.session.flush()
	# logout重定向至index页面
	return redirect('/index/')
