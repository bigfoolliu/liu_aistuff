#!-*-coding:utf-8-*-
# !@Date: 2018/8/26 14:49
# !@Author: Liu Rui
# !@github: bigfoolliu


"""
实现功能的分离

即服务器程序和请求处理分开

1. WebServer 文件只用来提供请求的接收和响应
2. WebFrame 文件只用来提供请求数据的处理和返回
3. 文件之间利用一个函数来传递请求数据和返回的信息
"""
import socket
import re
import multiprocessing
from dynamic import WebFrame


LOCAL_IP = ""
PORT = 2018


class WebServer(object):
	"""服务器类"""
	def __init__(self):
		# 1. 创建tcp套接字通信
		self.__tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# 重新启用占用的端口
		self.__tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		# 2. 绑定IP和端口号
		self.__tcp_server_socket.bind((LOCAL_IP, PORT))

		# 3. 设置套接字最大连接数
		self.__tcp_server_socket.listen(128)

	def service_client(self, new_socket):
		"""
		为客户端返回数据
		:return:
		"""
		# 1. 接收浏览器发来的http请求
		request = new_socket.recv(1024).decode("utf-8")

		# 2. 按行分解请求并存到列表中
		request_lines = request.splitlines()

		# print(request_lines[0])  # 测试
		# GET /index.html HTTP/1.1
		file_name = ""

		# 3. 正则匹配请求的路径,如/index.html
		ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])

		# 如果匹配结果不为none说明结果正确
		if ret:
			# 利用分组得到请求地址的文件名,正则的分组从索引1开始
			file_name = ret.group(1)
			print("file_name: ", file_name)
		# 如果请求地址为/,则默认设为index.html
		if file_name == "/":
			file_name = "/index.html"

		# 如果请求的为"动态页面"
		# TODO 页面为静态还是动态的区分
		if file_name.endswith(".html"):

			# 定义一个字典变量来存放客户端请求的信息
			env = {"PATH_INFO": file_name}

			# 通过导入WebFrame文件,调用模块里的application函数,实现响应文件分离
			response_body = WebFrame.application(env, self.start_response)

			# 拼接响应报文
			# 响应行
			response_line = "HTTP/1.1 %s \r\n" % self.__status

			# 响应头
			response_header = ""

			# 遍历params里的内容,进行拼接
			for t in self.__params:
				response_header += "%s:%s\r\n" % t

			# 拼接响应报文
			response_data = response_line + response_header + "\r\n" + response_body

			# 发送响应报文
			new_socket.send(response_data.encode("utf-8"))

		else:
			# 4. 返回http格式的数据给浏览器
			try:
				# 拼接路径
				f = open("./static" + file_name, "rb")
			except:
				# 没有找到请求路径
				response = "HTTP/1.1 404 NOT FOUND\r\n"
				response += "\r\n"
				response += "file not exist."
				new_socket.send(response.encode("utf-8"))
				print("请求不存在的路径.")
			else:
				# 找到请求路径,读取文件的内容
				html_content = f.read()
				f.close()
				# 准备发送给浏览器的数据,header
				response = "HTTP/1.1 200 OK\r\n"
				response += "\r\n"

				# 如果想在响应体中直接发送文件内的信息,那么在上面读取文件时就不能用rb模式,只能使用r模式,所以下面将响应头和响应体分开发送
				# response += html_content

				# 发送数据头,response header
				new_socket.send(response.encode("utf-8"))

				# 发送response body
				new_socket.send(html_content)

		new_socket.close()

	def start_response(self, status, params):
		"""作为回调使用,保存框架文件返回的数据处理状态和响应头的信息"""
		# 保存状态码
		self.__status = status
		# 保存响应头中的信息
		self.__params = params

	def run(self):
		while True:
			# 4. 等待新客户端的连接
			new_socket, client_addr = self.__tcp_server_socket.accept()

			# 5. 为连接上的客户端创建一个新的进程去运行
			p = multiprocessing.Process(target=self.service_client, args=(new_socket,))
			p.start()
			# 因为新进程在创建过程中会完全复制父进程的运行环境,所以父线程中关闭的只是自己环境中的套接字对象
			# 而新进程中因为被复制的环境中是独立存在的,所以不会受到影响
			new_socket.close()

		# 6. 关闭监听套接字
		self.__tcp_server_socket.close()  # TODO 关闭与否(强迫症)


def main():
	web_server = WebServer()
	web_server.run()


if __name__ == '__main__':
	main()
