"""
URLError类

来自urllib库的error模块，它继承自OSError类，是error异常模块的基类，由request模块生
的异常都可以通过捕获这个类来处理。它具有一个属性reason，即返回错误的原因。
"""
# import urllib.error, urllib.request
#
# # 打开一个网址，返回错误的原因
# try:
#     response = urllib.request.urlopen('http://cuiingcai.com/index.htm')  # 试着打开一个不存在的网址
# except urllib.error.URLError as e:
#     print(e.reason)  # 输出错误的原因


"""
HTTPError类

它是URLError的子类，专门用来处理HTTP请求错误，比如认证请求失败等。它有如下3个属性。

code：返回HTTP状态码，比如404表示网页不存在，500表示服务器内部错误等。
reason：同父类一样，用于返回错误的原因。
headers：返回请求头。
"""
# import urllib.error, urllib.request
#
# try:
#     response = urllib.request.urlopen('http://cuiqingcai.com/index.htm')
# except urllib.error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')


"""
URLError是HTTPError的父类，所以可以先选择捕获子类的错误，再去捕获父类的错误，所以
上述代码更好的写法如下：
"""
# from urllib import request, error
#
# try:
# 	response = request.urlopen('http://cuiqingcai.com/index.htm')
# except error.HTTPError as e:
# 	print(e.reason, e.code, e.headers, sep='\n')
# except error.URLError as e:
# 	print(e.reason)
# else:
# 	print('Request Successfully')
