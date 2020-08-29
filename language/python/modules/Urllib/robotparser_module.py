"""
1. Robots 协议

Robots协议也称作爬虫协议、机器人协议，它的全名叫作网络爬虫排除标准
（Robots Exclusion Protocol），用来告诉爬虫和搜索引擎哪些页面可以抓取，
哪些不可以抓取。它通常是一个叫作robots.txt的文本文件，一般放在网站的根目录下。

当搜索爬虫访问一个站点时，它首先会检查这个站点根目录下是否存在robots.txt文件，
如果存在，搜索爬虫会根据其中定义的爬取范围来爬取。如果没有找到这个文件，搜索爬虫
便会访问所有可直接访问的页面。


robots.txt样例为：

User-agent: WebCrawler
Disallow:
User-agent: *
Disallow: /

该样例表示只允许WebCrawler爬虫访问该网站。
"""

"""
2. 爬虫名称

爬虫名实际上是有固定的的名字的，常见对应关系如：

爬虫名称               名称                  网站
BaiduSpider           百度                  www.baidu.com
Googlebot             谷歌                  www.google.com
YodaoBot              有道                  www.youdao.com 
"""


"""
3. robotparser

使用robotparser模块来解析robots.txt了。
该模块提供了一个类RobotFileParser，它可以根据某网站的robots.txt文件来判断一个爬取爬虫是否有权限来爬取这个网页。

下面列出了这个类常用的几个方法：

1. set_url()：用来设置robots.txt文件的链接。如果在创建RobotFileParser对象时传入
了链接，那么就不需要再使用这个方法设置了。

2. read()：读取robots.txt文件并进行分析。注意，这个方法执行一个读取和分析操作，
如果不调用这个方法，接下来的判断都会为False，所以一定记得调用这个方法。这个方法
不会返回任何内容，但是执行了读取操作。

3. parse()：用来解析robots.txt文件，传入的参数是robots.txt某些行的内容，它会
按照robots.txt的语法规则来分析这些内容。

4. can_fetch()：该方法传入两个参数，第一个是User-agent，第二个是要抓取的URL。
返回的内容是该搜索引擎是否可以抓取这个URL，返回结果是True或False。

5. mtime()：返回的是上次抓取和分析robots.txt的时间，这对于长时间分析和抓取的
搜索爬虫是很有必要的，你可能需要定期检查来抓取最新的robots.txt。

6. modified()：它同样对长时间分析和抓取的搜索爬虫很有帮助，将当前时间设置为上次
抓取和分析robots.txt的时间。
"""

from urllib.robotparser import RobotFileParser

rp = RobotFileParser()  # 构建该类

rp.set_url('http://www.jianshu.com/robots.txt')  # 向rp类中添加url

rp.read()  # 读取内容

print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))
