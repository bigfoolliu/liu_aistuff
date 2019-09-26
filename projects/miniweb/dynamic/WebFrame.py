#!-*-coding:utf-8-*-
# !@Date: 2018/8/26 15:05
# !@Author: Liu Rui
# !@github: bigfoolliu


"""
框架

1. 主要用来处理动态文件请求
2. 用模板来实现基本页面的显示
	因为页面显示时,显示框架基本相同,只是显示的内容不同

"""
import re
from pymysql import connect

# 路由字典,通过装饰器将路径和响应函数自动加入
router_dict = {}


def application(environ, start_response):
	"""
	实现WSGI协议中application接口方法
	:param environ: dict, 服务器传递过来的包含请求路径的信息
	:param start_response: func, 回调函数, 将
	:return:
	"""
	url_path = environ["PATH_INFO"]

	# 通过回调函数来返回状态码和响应头信息
	start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])

	# 根据对应的地址来调用不同的函数进行页面处理
	# 默认调用other()函数
	func = other
	if url_path in router_dict:
		func = router_dict[url_path]

	file_content = func()

	# 回调start_response函数,将响应状态信息回传给服务器
	start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

	# 返回响应数据内容
	return file_content


# TODO:,需要加深这一装饰器的作用的理解
def router(url_path):
	"""
	带参的装饰器
	:param url_path: 请求路径
	:return:
	"""

	def set_func(func):
		def wrapper(*args, **kwargs):
			return func(*args, **kwargs)

		# 将 wrapper 的引用存入字典入,以 url_path 参数做为 key,wrapper 指向就是被装饰函数本身
		router_dict[url_path] = wrapper
		return wrapper

	return set_func


@router("/index.html")
def index():
	path = "./templates/index.html"
	# 读取模板文件中的内容
	with open(path, "r", encoding="utf-8") as f:
		content = f.read()

	# 替换的一条假数据(之后从数据库读取将其替换)
	row_str = """ 
						<tr>
							<td>%s</td>
							<td>%s</td>
							<td>%s</td>
							<td>%s</td>
							<td>%s</td>
							<td>%s</td>
							<td>%s</td>
							<td>%s</td>
							<td>
								<input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007">
							</td>
						</tr>  """
	# 1. 准备连接数据库
	conn = connect(host="localhost", port=3306, database="stock_db", user="tonyliu", password="liu941103",
				   charset="utf8")
	# 2. 获得游标
	cur = conn.cursor()
	# 3. 执行语句
	sql_str = "SELECT * FROM info;"
	cur.execute(sql_str)

	# 4. 获取所有的表格数据,返回的是元组类型的数据
	sql_result = cur.fetchall()

	# 5. 遍历结果并拼接数据至上面的html语段
	all_data = ""
	for t in sql_result:
		all_data += row_str % (t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7])

	# 6. 关闭游标以及连接
	cur.close()
	conn.close()

	# 替换掉index.html模板中的占位符
	content = re.sub(r"\{%content%\}", all_data, content)

	response_body = content
	return response_body


@router("/center.html")
def center():
	path = "./templates/center.html"

	with open(path, "r", encoding="utf-8") as f:
		content = f.read()

	row_str = """ 
						<tr>
							<td>%s</td>
							<td>%s</td>
							<td>%s</td>
							<td>%s</td>
							<td>%s</td>
							<td>%s</td>
							<td>%s</td>
							<td>
								<a type="button" class="btn btn-default btn-xs" href="/update/000426.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
							</td>
							<td>
								<input type="button" value="删除" id="toDel" name="toDel" systemidvaule="000426">
							</td>
						</tr> """

	# 同上读取数据库中的内容
	conn = connect(host="localhost", port=3306, database="stock_db", user="tonyliu", password="liu941103",
				   charset="utf8")
	cur = conn.cursor()
	sql_str = "SELECT info.code, info.short, info.chg, info.turnover, info.price, info.highs, stock_db.focus.note_info FROM info INNER JOIN focus WHERE info.id = focus.info_id;"

	cur.execute(sql_str)
	sql_result = cur.fetchall()

	# 遍历结果拼接数据
	all_data = ""
	for t in sql_result:
		all_data += row_str % (t[0], t[1], t[2], t[3], t[4], t[5], t[6])

	cur.close()
	conn.close()

	content = re.sub(r"\{%content%\}", all_data, content)

	response_body = content
	return response_body


def other():
	file_content = "other page..."
	response_body = file_content
	return response_body
