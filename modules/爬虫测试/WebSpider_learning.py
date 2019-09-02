'''
python爬虫(网络爬虫：web spider)

使用chrome浏览器自带的开发者工具查看http头的方法
1.在网页任意地方右击选择审查元素或者按下 shift+ctrl+c, 打开chrome自带的调试工具;
2.选择network标签, 刷新网页(在打开调试工具的情况下刷新);
3.刷新后在左边找到该网页url,点击 后右边选择headers,就可以看到当前网页的http头了;

请求Header(HTTP request header )
Host 请求的域名
User-Agent 浏览器端浏览器型号和版本
Accept 可接受的内容类型
Accept-Language 语言
Accept-Encoding 可接受的压缩类型 gzip,deflate
Accept-Charset 可接受的内容编码 UTF-8,*

服务器端的响应Header(response header)
Date 服务器端时间
Server 服务器端的服务器软件 Apache/2.2.6
Etag 文件标识符
Content-Encoding传送启用了GZIP压缩 gzip
Content-Length 内容长度
Content-Type 内容类型

'''
# encoding = 'utf-8'
# 爬取百度首页或更改url等任何网页的源代码
import urllib.request

import io

import sys

# 将爬取得数据存放在txt文件中后期处理起来会比较麻烦，很不方便，如果数据
# 量比较大的情况下，查找更加麻烦，所以我们通常会把爬取的数据存储到数据库
# 中便于后期分析利用
import pymysql

# BeautifulSoup是一个可以从HTML或XML文件中提取数据的库，能够通过
# 你喜欢的转换器实现惯用的文档导航,查找,修改文档的方式
from bs4 import BeautifulSoup

'''
url = "http://www.baidu.com"#确定网络地址

#urllib.request.urlopen()方法实现了打开url,并返回一个 
#http.client.HTTPResponse对象,通过http.client.HTTPResponse的read()方法,
#获得response body,转码最后通过print()打印出来.
page_info = urllib.request.urlopen(url).read()
page_info = page_info.decode('utf-8')#将页面转至utf-8的编码形式，否则会乱码

print(page_info)
'''

# 网站通常会用判断访问是否带有头文件来鉴别该访问是否为爬虫，用来作为反爬取的一种策略
# Python中urllib中的request模块提供了模拟浏览器访问的功能
# 访问头信息(headers，字典类型)中显示了浏览器以及系统的信息，加入该信息可将爬虫模拟成浏览器对网站进行访问

url = 'https://www.baidu.com'

# 访问头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

# 获取页面
page = urllib.request.Request(url, headers=headers)
# 打开并转码页面为utf-8格式
page_info = urllib.request.urlopen(page).read().decode('utf-8')

# 将获取的内容page_info转换为BeautifulSoup格式，并以html.parser为解析器
# html.parser为pyton标准库中的解析器，还有第三方解析器用以解析网页信息
soup = BeautifulSoup(page_info, 'html.parser')
# 以格式化的形式打印html
print(soup.prettify())

'''
# 方式一
# 以写的方式创建文件baidu_page.txt
f = open('baidu_page.txt', 'w', encoding='utf-8')
# 将页面信息写入文件
f.write(page_info)
# 关闭文件
f.close()
'''

# 方式二
# windows环境下，新建的.txt文件默认为gbk编码，因此需要改变目标文件的编码
with open('baidu_page.txt', 'a', encoding='utf-8') as f:  # 将w改为a，可以在不清空之前文本的情况下，添加内容
    f.write('\n\n\n分割线----------------------------------------------------------\n\n\n')
    for i in page_info:
        f.write(i)
# 打开的文件一定要关闭，否则会占用相当大的系统资源，但是with语句会帮我们自动调用close()
# f.close()
