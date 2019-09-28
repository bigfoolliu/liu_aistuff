#!-*-coding:utf-8-*-
# !@Date: 2018/8/26 8:56
# !@Author: Liu Rui
# !@github: bigfoolliu


"""
flask初识

Web 服务器使用一种名为Web 服务器网关接口
（Web Server Gateway Interface，WSGI）的协议，把接收自客户端的所有请求都转交给这
个对象处理。程序实例是Flask 类的对象，经常使用下述代码创建：

主模块
"""
# from flask import Flask
#
# # 1. 初始化一个Flask对象,参数表明查询文件时应该访问的路径,即决定资源的根路径
# app = Flask(__name__)
#
#
# # 2. 使用装饰器声明路由,来处理url和函数的关系
# # 把index()函数注册为程序根地址的处理程序,为 视图函数.
# @app.route("/")
# def index():
# 	return "<h1>Hello World!</h1>"
#
#
# # # 当url的格式为.../user/(动态的)用户名时,生成动态的针对个人的欢迎消息
# # @app.route("/user/<name>")
# # def user(name):
# # 	return "<h1>Hello, %s!</h1>" % name
#
#
# # 3. 使用实例的run方法来启动Flask集成的web服务器
# if __name__ == '__main__':
# 	# 3.1 启用了调试模式,可以为激活调试器和重载程序带来便利
# 	app.run(debug=True)


"""
2. 请求-响应循环
"""
# from flask import Flask
# from flask import request
#
# # 1. 初始化一个Flask对象,参数表明查询文件时应该访问的路径,即决定资源的根路径
# app = Flask(__name__)
#
#
# # 2. 使用装饰器声明路由,来处理url和函数的关系
# # 把index()函数注册为程序根地址的处理程序,即: 视图函数
# @app.route("/")
# def index():
# 	# flask使用上下文让临时让某些对象为全局的, 从而视图函数可以不必传参而访问请求对象
# 	# request 为请求上下文
# 	user_agent = request.headers.get("User-Agent")
# 	return "<p>您正在使用%s浏览器.</p>" % user_agent
#
#
# # 3. 使用实例的run方法来启动Flask集成的web服务器
# if __name__ == '__main__':
# 	# 3.1 启用了调试模式,可以为激活调试器和重载程序带来便利
# 	app.run(debug=True)


"""
2.1 创建响应对象
"""
# from flask import Flask
# from flask import make_response  # 导入创建响应模块
#
# # 1. 初始化一个Flask对象,参数表明查询文件时应该访问的路径,即决定资源的根路径
# app = Flask(__name__)
#
#
# # 2. 使用装饰器声明路由,来处理url和函数的关系
# # 把index()函数注册为程序根地址的处理程序,即: 视图函数
# @app.route("/")
# def index():
# 	# 创建了一个响应对象,可以将各种响应信息绑定上去
# 	response = make_response("<h1>This document carries a cookie.</h1>")
# 	# 设置响应对象的cookie
# 	response.set_cookie("answer", "42")
# 	return response
#
#
# # 3. 使用实例的run方法来启动Flask集成的web服务器
# if __name__ == '__main__':
# 	# 3.1 启用了调试模式,可以为激活调试器和重载程序带来便利
# 	app.run(debug=True)


"""
2.2 重定向响应对象
"""
# from flask import Flask
# from flask import redirect
#
# # 1. 初始化一个Flask对象,参数表明查询文件时应该访问的路径,即决定资源的根路径
# app = Flask(__name__)
#
#
# # 2. 使用装饰器声明路由,来处理url和函数的关系
# # 把index()函数注册为程序根地址的处理程序,即: 视图函数
# @app.route("/")
# def index():
# 	# 重定向的响应类型,这种响应没有页面文档,只告诉浏览器一个新的地址以加载页面
# 	return redirect("http://www.baidu.com")
#
#
# # 3. 使用实例的run方法来启动Flask集成的web服务器
# if __name__ == '__main__':
# 	# 3.1 启用了调试模式,可以为激活调试器和重载程序带来便利
# 	app.run(debug=True)


"""
3.1 使用渲染模板
"""
# from flask import Flask
# from flask import render_template
#
# app = Flask(__name__)
#
#
# @app.route("/")
# def index():
# 	# 渲染模板默认的查找路径为: /templates/xxx
# 	return render_template("index.html")
#
#
# if __name__ == '__main__':
# 	app.run(debug=True)


"""
4.2 表单类

一个简单的Web表单,包含一个文本字段和一个提交按钮
"""
from flask import Flask
from flask import render_template
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(Form):
	"""定义姓名表单类"""
	# 定义一个文本字段的类变量
	name = StringField("what's your name?", validators=[Required()])
	# 定义一个提交按钮的类变量
	submit = SubmitField("Submit")


app = Flask(__name__)
# 设置一个密钥,flask-wtf用该密钥生成加密令牌,保护表单免受跨站请求伪造(CSRF)攻击
app.config["SECRET_KEY"] = "hard to guess string"


@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template('index.html', form=form, name=name)


if __name__ == '__main__':
	app.run(debug=True)
