"""
1. 基础知识

urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)

response为HTTPResponse类型的对象

包括以下方法：
read()
readinto()
getheader(name)
getheaders()
fileno()等

包括以下属性：
msg
version
status
reason
debuglevel
closed
"""
# import urllib.request
#
# # response = urllib.request.urlopen('https://www.python.org')
#
# response = urllib.request.urlopen('https://www.baidu.com/', timeout=0.0001)  # timeout参数用于设置超时时间，单位为秒，请求超过设置时间就会抛出异常
#
# print(response.read().decode('utf-8'))
#
# print(response.read())
#
# print(type(response))  # response的类型为<class 'http.client.HTTPResponse'>
#
# print(response.msg)  # OK
# print(response.version)  # 11
# print(response.status)  # 200，表示请求成功
# print(response.reason)  # OK
# print(response.debuglevel)  # 0
# print(response.closed)  # False


"""
2.
利用Request类可以构建更强大的请求，比如加入Headers等信息
class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)

url：请求url，必传参数
data：若传必须是bytes类型，若是字典类型，需用urllib.parse模块里的urlencode()编码
headers：是一个字典，是请求头，可在构造请求时直接构造，也可通过实例的add_header()方法添加
origin_req_host：请求方的host名称或IP地址
unverifiable：表示该请求是否是无法验证的，默认False，表示用户没有足够权限选择接受请求的结果
method：表示请求的方法，如GET,POST和PUT等
"""
# import urllib.request
# from urllib import parse
#
# request = urllib.request.Request('https://python.org')
# response2 = urllib.request.urlopen(request)
#
# print(response2.read().decode('utf-8'))
#
# url = 'http://www.zealer.com/'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
#     'Host':'www.zealer.com'
# }
# dict = {
#     'name':'Germey'
# }
#
# data = bytes(parse.urlencode(dict), encoding='utf-8')
#
# request = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
#
# response = urllib.request.urlopen(request)
#
# print(response.read().decode('utf-8'))


"""
3.
Handler工具：可理解为各种处理器，包括处理登录验证，Cookies，代理设置等HTTP请求中的所有事情
urllib.request.BaseHandler：BaseHandler类，为其他Handler的父类，提供基本的方法，包括：default_open()，protocol_open()等

BaseHandler类的子类：
1. HTTPDefaultErrorHandler：用于处理HTTP响应错误，错误都会抛出HTTPError类型的异常。
2. HTTPRedirectHandler：用于处理重定向。
3. HTTPCookieProcessor：用于处理Cookies。
4. ProxyHandler：用于设置代理，默认代理为空。
5. HTTPPasswordMgr：用于管理密码，它维护了用户名和密码的表。
6. HTTPBasicAuthHandler：用于管理认证，如果一个链接打开时需要认证，那么可以用它来解决认证问题。

其他Handler类可参考：https://docs.python.org/3/library/urllib.request.html  # urllib.request.BaseHandler


引入Opener：因为需要实现更高级的功能。之前使用的Request和urlopen()相当于类库为你封装好了极其常用的请求方法，
利用它们可以完成基本的请求，但是现在不一样了，我们需要实现更高级的功能，所以需要深入一层进行配置，使用更底层
的实例来完成操作，所以这里就用到了Opener。

Opener可以使用open()方法，返回的类型和urlopen()如出一辙。那么，它和Handler有什么关系呢？简而言之，就是利用
Handler来构建Opener。
"""

"""
4.
遇到需要输入用户名和密码，验证成功才能看到页面的情况
借助HTTPBasicAuthHandler类
"""
# from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
# from urllib.error import URLError
#
# username = 'username'
# password = 'password'
# url = 'http://localhost:5000/'
#
# p = HTTPPasswordMgrWithDefaultRealm()  # 构建该类，为一个密码管理对象，用来保存HTTP请求相关的用户名和密码
# p.add_password(None, url, username, password)  # 向该类中添加username和password
#
# auth_handler = HTTPBasicAuthHandler(p)  # 构建密码管理类的授权handler实例
# opener = build_opener(auth_handler)  # 构建opener
#
# try:
#     result = opener.open(url)  # 利用构建的opener代开url，该opener发送请求时就相当于验证成功了
#     html = result.read().decode('utf-8')  # 读取该url
#     print(html)
# except URLError as e:
#     print(e.reason)


"""
5.
代理
添加代理
"""
# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener
#
# proxy_handler = ProxyHandler({
#     'http': 'http://127.0.0.1:9743',  # 代理服务器运行在端口9743上
#     'https': 'https://127.0.0.1:9743'
# })  # 代理处理程序ProxyHandler设置使用代理服务器，且需要传入代理服务器的地址
#
# opener = build_opener(proxy_handler)  # 构建以代理类为打开方式额opener
#
# try:
#     response = opener.open('https://www.baidu.com')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)


"""
6.
Cookies
获取网站的Cookies
"""
# import http.cookiejar, urllib.request
#
# cookie = http.cookiejar.CookieJar()  # 构建一个CookieJar类
# handler = urllib.request.HTTPCookieProcessor(cookie)  # 构建一个HTTPCookieProcessor类，支持cookie的opener
# opener = urllib.request.build_opener(handler)  # 用build_opener函数创建一个opener类
#
# response = opener.open('http://www.baidu.com')  # 打开url
#
# # 依次输出每条Cookies的名称和值
# for item in cookie:
#     print(item.name+"="+item.value)


"""当需要将输出的Cookies保存为文本"""
# import http.cookiejar
# import urllib.request
# filename = 'cookie_test.txt'
#
# cookie = http.cookiejar.MozillaCookieJar(filename)  # MozillaCookieJar类可以处理Cookies和文件相关的事件，比如保存和读取，可以将Cookies保存为Mozilla型浏览器的Cookies格式
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
#
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)


if __name__ == "__main__":
    pass
