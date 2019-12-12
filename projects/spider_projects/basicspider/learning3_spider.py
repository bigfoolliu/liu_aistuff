# 爬取特定网页的图片并保存到本地

from urllib import request
import bs4
import re
import time


# 获取url
url = r'https://www.zhihu.com/question/66313867'
# 获取头文件，以模仿浏览器打开
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
# 获取页面
page = request.Request(url, headers=headers)
# 读取页面并解码
page_info = request.urlopen(page).read().decode('utf-8')
# 标准化格式
soup = bs4.BeautifulSoup(page_info, 'html.parser')

# BeautifulSoup和正则表达式结合，提取出所有图片的链接(img标签中，class = 'Avatar AuthorInfo-avatar' ，以'.jpg'结尾)
links = soup.find_all('img', "Entry-body", src=re.compile(r'.jpg$'))
# 设置本地保存路径
local_path = r'beauty2'

# 保存图片
for link in links:
    print(link.attrs['src'])
    # 保存链接并命名，time防止命名冲突
    request.urlretrieve(link.attrs['src'], local_path + r'\\%s.jpg' % time.time())


'''
url = r'https://www.baidu.com/top/pic1.zhimg.com/50'
# 获取头文件，以模仿浏览器打开
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
# 获取页面
page = request.Request(url, headers=headers)
# 读取页面并解码
page_info = request.urlopen(page).read().decode('utf-8')
# 标准化格式
soup = bs4.BeautifulSoup(page_info, 'html.parser')

print(soup.prettify())
'''
