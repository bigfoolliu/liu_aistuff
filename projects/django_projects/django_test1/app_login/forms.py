#!-*-coding:utf-8-*-
# !@Date: 2018/9/14 14:59
# !@Author: Liu Rui
# !@github: bigfoolliu


"""
不同于login的用html手动创建表单,也可以使用django自带的模块进行表单的创建

说明：
	1. 要先导入forms模块
	2. 所有的表单类都要继承forms.Form类
	3. 每个表单字段都有自己的字段类型比如CharField，
		它们分别对应一种HTML语言中<form>内的一个input元素。这一点和Django模型系统的设计非常相似。
	4. max_length限制字段输入的最大长度。它同时起到两个作用，一是在浏览器页面限制用户输入不可超过字符数，
		二是在后端服务器验证用户输入的长度也不可超过。
	5. widget=forms.PasswordInput用于指定该字段在form表单里表现为<input type='password' />，也就是密码输入框。
	6. label参数用于设置<label>标签.

"""
from django import forms


class RegisterForm(forms.Form):
	"""注册表单类"""
	gender = (
		('male', "男"),
		('female', "女"),
	)
	# attrs里面的参数是为了渲染的类名
	user_name = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
	password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
	sex = forms.ChoiceField(label="性别", choices=gender)


