# scrapy基础知识

**制作 Scrapy 爬虫 一共需要4步:**

1. 新建项目 (scrapy startproject xxx)：新建一个新的爬虫项目
2. 明确目标 （编写items.py）：明确你想要抓取的目标
3. 制作爬虫 （spiders/xxspider.py）：制作爬虫开始爬取网页
4. 存储内容 （pipelines.py）：设计管道存储爬取内容

**核心组件:**

1. 引擎(Engine), 和各组件交互
2. 管道(Item Pipeline), 接收并保存item数据
3. 爬虫(Spider), 第一批的url地址以及解析响应的方法
4. 下载器(Downloader), 并发发送请求返回响应
5. 调度器(Scheduler), 对每一个请求去重处理并将去重请求放入队列

*所有的组件都直接和引擎交互,从而降低耦合度,只需要编写爬虫和管道的代码!
一个项目可以有多个爬虫同时执行, 只要多开一个终端, 即可以多开一个进程...*

**三大对象:**

1. Request对象
2. Response对象
3. Item对象

**两大可选中间件:**

1. 下载中间件(Downloader Middleware)
2. 爬虫中间件(Spider Middleware)

*对失败的请求会重试, 当重试三次失败则会丢弃请求.*

相关命令:

```text
终端常用命令:
scrapy startproject projectName: 创建一个新的项目

scrapy genspider baidu "baidu.com": 创建一个使用默认模板的爬虫, 且爬取的域名有限制

scrapy list: 查看当前爬虫的列表

scrapy runspider baidu.py: 执行爬虫
scrapy crawl baidu: 执行爬虫(推荐,不必需要指定具体的文件)

scrapy crawl baidu -o data/baidu_result.json: 执行爬虫,并将结果保存指定目录下的json格式文件(还默认支持csv、xml、jl等)

scrapy shell "http://www.baidu.com/" -s USER_AGENT="xxx": 以指定的User-Agent访问一个网址返回响应
```

**Request对象和Response对象的属性:**

```text
Request对象的属性:
    request.url: 请求的url
    request.callback: 指定返回的response由哪个函数处理
    request.method: 请求方式一般不指定
    request.headers: 请求头,一般不需要
    request.meta: 在不同的请求之间传递数据使用的,为dict型
    request.encoding: 默认为utf-8
    request.errback: 指定错误处理函数
    request.dont_filter: 表名该请求不由调度器过滤, 即不做请求去重处理

Response对象的属性:
    response.url: 响应 url地址
    response.haeders: 响应报头
    response.body: 网页原始编码字符串
    response.text: 网页Unicode编码字符串

从response中提取字符串:
    response.xpath("//title/text()").extract()  # 返回所有结果的字符串列表,没有匹配到则返回空列表
    response.xpath("//title/text()").extract_first()  # 返回第一个匹配到的结果,没有匹配到则返回None

注意: scrapy中嵌入了xpath语法, 但是提取数据需要使用extract()和extract_first()函数!
```

**Scrapy处理翻页数据方式:**

1. 自增量拼接地址, 不依赖<a>标签, 可根据响应状态码和内容作为停止条件;
2. 根据"下一页"是否终止, 依赖<a>标签;
3. 将所有的start_urls保存在一个文件中, 作为第一批urls发送给下载器, 并发处理.

## Item Pipeline

**item pipeline的一些典型应用:**

- 验证爬取的数据(检查item包含某些字段，比如说name字段)
- 查重(并丢弃)
- 将爬取结果保存到文件或者数据库中

```python
"""
管道类的定义以及各方法的实现
"""
from ScrapyTutorial.items import TencentItem 


class TencentPipeline(object):
    def __init__(self):
        """
        可选实现，做参数初始化等
        """
        pass

    def process_item(self, item, spider):
        """
        这个方法必须实现，每个item pipeline组件都需要调用该方法，
        这个方法必须返回一个 Item 对象，被丢弃的item将不会被之后的pipeline组件所处理
        """
        if isinstance(item, TencentItem):
            pass
        return item

    def open_spider(self, spider):
        """
        可选实现，当spider被开启时，这个方法被调用。
        """
        pass

    def close_spider(self, spider):
        """
        可选实现，当spider被关闭时，这个方法被调用
        """
        pass


"""
同时需要在settings.py文件中启用该管道
之后在命令行中执行 scrapy crawl tencent 时就会自送调用该管道来对取得的数据进行处理
"""
ITEM_PIPELINES = {
    #'mySpider.pipelines.SomePipeline': 300,
    'ScrapyTutorial.pipelines.TencentPipeline':300
}
```

## Spider

Spider类就是您定义爬取的动作及分析某个网页(或者是有些网页)的地方.
适合一般的大部分的页面爬取.

```python
"""
爬虫类的定义和实现

主要的属性和方法:
tencent_spider = TencentSpider()

tencent_spider.name                     spider的名字
                allowed_domains         允许爬取的域名列表(可选)
                start_urls              初始url元组/列表,从该列表开始爬取
                start_requests(self)    该方法必须返回一个包含spider用于爬取的第一个Request的可迭代对象(iterable),
                parse(self, response)   处理网页的response以及生成item或者Request对象
                log(self, message[])    scrapy.log.msg() 方法记录(log)message.
"""
import scrapy


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = 'https://hr.tencent.com/position.php?&start=0'

    def parse(self, response):
        """
        必须要有
        解析response，并返回Item或Requests（需指定回调函数）。
        Item传给Item pipline持久化
        而Requests交由Scrapy下载，并由指定的回调函数处理（默认parse())，一直进行循环，直到处理完所有的数据为止。
        """
        pass
```

## CrawlSpider

Spider的派生类，Spider类的设计原则是只爬取start_url列表中的网页，
而CrawlSpider类定义了一些规则(rule)来提供跟进link的方便的机制，
从爬取的网页中获取link并继续爬取的工作, 即适合**多层爬取**.

```text
快速创建一个带有内部模板的CrawlSpider

scrapy genspider -t crawl baidu baidu.com
```

**属性rules:**

决定爬虫的爬取规则，并将匹配后的url请求提交给引擎.

```text
class scrapy.spiders.Rule(
        link_extractor,  # 一个Link Extractor对象，用于定义需要提取的链接
        callback = None,  # 从link_extractor中每获取到链接时，参数所指定的值作为回调函数，该回调函数接受一个response作为其第一个参数
        cb_kwargs = None,
        follow = None,  # True表示跟进从response中提取到的链接, False表示不跟进
        process_links = None,
        process_request = None
)
```

**由于CrawlSpider使用parse方法来实现其逻辑，如果覆盖了 parse方法，crawl spider将会运行失败.
即callback参数后面不能接parse, 可以定义改名为parse_page等.**

**LinkExtractors:**

目的很简单: 提取链接｡

```text
class scrapy.linkextractors.LinkExtractor(
    allow = (),  # 满足括号中的正则表达式将会被提取
    deny = (),  # 优先级高于allow, 满足的正则将不会被提取
    allow_domains = (),  # 会被提取的链接的domains
    deny_domains = (),  # 一定不会被提取链接的domains
    deny_extensions = None,
    restrict_xpaths = (),  # 使用xpath表达式，和allow共同作用过滤链接
    tags = ('a','area'),
    attrs = ('href'),
    canonicalize = True,
    unique = True,
    process_value = None
)
```

**小工具: fake_useragent:**

```python
"""
>>>pip install fake_useragent
可以通过该工具生成可用User-Agent
"""
from fake_useragent import UserAgent

ua_obj = UserAgent()

print(ua_obj.ie)  # 指定浏览器类型的User-Agent
print(ua_obj.Chrome)
print(ua_obj.Firefox)
print(ua_obj.safari)

print(ua_obj.random)  # 随机类型的
```

**模拟登录:**

```text
使用下面的命令发送POST请求:

yield scrapy.FormRequest(url, formdata, callback)

如果希望程序执行一开始就发送POST请求，可以重写Spider类的start_requests(self) 方法，
并且不再调用start_urls里的url。
```

**scrapy反爬主要是通过中间件middleware实现的, 通常防止反爬的策略:**

1. 动态设置User-Agent(模拟不同用户的浏览器信息)
2. 禁用cookies(不启用cookie middleware), 因为有些网站根据cookies判断爬虫
3. 设置延迟下载, 防止访问过于频繁
4. 使用谷歌/百度等搜索引擎服务器页面缓存(Google Cache, Baidu Cache)获取页面数据
5. 使用IP代理池: VPN和代理IP

    ```text
    抓取网上代理ip,测试其中可用的;
    代理供应商提供的代理(收费);
    ADSL拨号,每次重新拨号都会更换本地ip,但会有1-3秒延迟;
    VPN/VPS(翻墙);
    Tor网络(暗网), 洋葱浏览器
    ```

6. 使用Crawlera(专用于爬虫的代理组件, 但是需要花钱在维护scrapy的公司购买)

## 设置下载中间件

下载中间件是处于引擎(crawler.engine)和下载器(crawler.engine.download())之间的一层组件，
可以有多个下载中间件被加载运行。

**引擎向下载器传递request进行相关处理(添加http header, 或者代理proxy);
下载器向引擎传递response的时候进行相关处理(gzip解压等).**

```text
process_request(self, request, spider):
    每个request通过下载中间件的时候, 该方法被调用.
    必须返回下面之一:
        1. None                     之后scrapy继续处理该request,执行其他的中间件,直到合适的下载器处理函数被调用,
                                        该request被执行,response被下载
        2. Request对象               停止调用process_request,重新调度request
        3. Response对象              相应地中间件链将会根据下载的response被调用
        4. raise IgnoreRequest       安装的下载中间件的raise_exception()方法将被调用,
                                        否则Request.errback方法将会被调用,
                                        否则该异常将会被忽略且不记录.

process_response(self, response, spider):
    下载器完成http请求发响应给引擎时调用.
    必须返回下面之一:
        1. Response对象(与传入的相同或全新的)   由中间件链中的其他process_response处理
        2. Request对象                        中间价链停止,返回的request被重新调度
        3. raise IgnoreRequest               同process_request()中的raise IgnoreRequest
```

## Scrapyd远程部署和监控爬虫

[官方文档](http://scrapyd.readthedocs.org/en/latest/)

相关命令:

```text
# 安装scrapyd服务器端
>>>pip install scrapyd

# 安装scrapyd客户端工具
>>>pip install scrapy-client

# 启用scrapyd服务端
>>>scrapyd

# 打开并修改scrapyd配置文件（例）, 将bind_address修改为0.0.0.0, 从而任意的ip能访问
>>>sudo vi /usr/local/lib/python2.7/site-packages/scrapyd/default_scrapyd.conf

# 通过Scrapyd客户端工具挂载项目(指定scrapy.cfg中的deploy的配置名和项目名)
>>>scrapyd-deploy scrapy_tencent3 -p ScrapyTutorial

# 远程启动爬虫
>>>curl http://localhost:6800/schedule.json -d project=ScrapyTutorial -d spider=tencent
爬虫启动成功后, 会生成job值, 停止时需要通过job值停止

# 远程停止爬虫
>>>curl http://localhost:6800/cancel.json -d project=ScrapyTutorial -d job=fcb0cbx...
```

## scrapy-redis分布式爬虫组件

基于scrapy(不能独立运行), 将scrapy的队列换成redis数据库, 多个爬虫端都可以访问redis数据库. 
支持断点续爬(暂停后继续之前的请求爬取).

自带四种组件(即对scrapy原有进行更改):

1. Scheduler(调度器, 入列和出列)
2. Duplication Filter(去重, 不操作重复的request)
3. Item Pipeline(将item存入redis的items queue)
4. Base Spider(不使用原有Spider类, 改用RedisSpider)

在redis数据库里提供:

1. 请求指纹集合(同一个数据库里判重, 不重复的请求放到请求队列)
2. 请求队列(同一个数据库放置请求, 以供分布式爬取, 主服务器爬第一个网址, 其他从服务器依次从队列里选取请求)
3. item队列(同一个数据库保存所有的结果)

**编写scrapy-redis分布式爬虫的步骤:**

1. 现将代码写成scrapy版本
2. 修改settings.py文件的配置
3. 修改spider文件

    - 导入并继承RedisSpider, RedisCrawlSpider
    - 删除start_urls, 避免多个爬虫端发送重复请求
    - 添加redis_key, 表示数据库接收第一批url的键

4. 启动爬虫, 数据库通过lpush添加第一批请求url地址
5. 从端中连接主服务器的redis数据库并启动爬虫, 实现分布式

    ```text
    $redis-cli -h 192.168.37.65  # 从机连接主机redis,从机甚至不需要安装redis
    ```

**配置:**

```python
"""
在settings.py文件中做出配置
可以做些小修改直接使用
"""
# 1(必须). 使用了scrapy_redis的去重组件，在redis数据库里做去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 2(必须). 使用了scrapy_redis的调度器，在redis里分配请求
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 3(必须). 在redis中保持scrapy-redis用到的各个队列，从而允许暂停和暂停后恢复，也就是不清理redis queues
SCHEDULER_PERSIST = True

# 4(必须). 通过配置RedisPipeline将item写入key为 spider.name : items 的redis的list中，供后面的分布式处理item
# 这个已经由 scrapy-redis 实现，不需要我们写代码，直接使用即可
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 100
}

# 5(必须). 指定redis数据库的连接参数
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

# 6.如果不启用则按scrapy默认的策略
#  -1. 默认的 按优先级排序(Scrapy默认)
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
#  -2. 可选的 按先进先出排序（FIFO）
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'
#  -3. 可选的 按后进先出排序（LIFO）
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderStack'

# 7. LOG等级
#LOG_LEVEL = 'DEBUG'
```

## 自定义爬虫框架

可以自己增加修改功能, 使用已有的框架需要熟读源码, 且修改源码可能带来不可预料的错误.
