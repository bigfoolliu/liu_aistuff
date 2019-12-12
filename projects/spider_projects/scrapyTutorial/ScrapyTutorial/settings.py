# -*- coding: utf-8 -*-

# Scrapy settings for ScrapyTutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ScrapyTutorial'

SPIDER_MODULES = ['ScrapyTutorial.spiders']  # Scrapy搜索spider的模块列表
NEWSPIDER_MODULE = 'ScrapyTutorial.spiders'  # 查找

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'ScrapyTutorial (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'

# 使用fake_useragent模块生成的User-Agent列表
USER_AGENT_LIST = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 \
    Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 \
    Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36',
    'Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17'
]

# Obey robots.txt rules
ROBOTSTXT_OBEY = False  # 不遵守robots.txt rules

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 设置下载延迟
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 除非特殊需要，禁用cookies，防止某些网站根据Cookie来封锁爬虫.
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'ScrapyTutorial.middlewares.ScrapytutorialSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# 激活下载器中间件组件, 键为中间件类的路径，值为其中间件的顺序(order)
DOWNLOADER_MIDDLEWARES = {
    'ScrapyTutorial.middlewares.ScrapytutorialDownloaderMiddleware': 543,
    # 'ScrapyTutorial.middlewares.RandomUserAgentMiddleware': 544,
    # 'ScrapyTutorial.middlewares.RandomProxyMiddleware': 545
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 为了启用自己写的管道,需要再次配置并启用,后面整型数值越低，组件的优先级越高(0-1000)
ITEM_PIPELINES = {
    # 'ScrapyTutorial.pipelines.ScrapytutorialPipeline': 300,
    'ScrapyTutorial.pipelines.ItcastPipeline': 300,
    'ScrapyTutorial.pipelines.TencentPipeline': 400,
    'ScrapyTutorial.pipelines.TencentCrawlSpiderPipeline': 500
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 西刺代理上选取的代理列表
PROXY_LIST = [
    'https://219.234.5.12:3128',
    'https://101.236.55.145:8866',
    'https://118.190.94.224:9001',
    'https://124.243.226.18:8888',
    'https://123.7.61.8:53281',
    'https://124.42.68.152:90',
    'https://58.52.171.159:808',
    'https://60.191.201.38:45461',
    'https://61.170.179.89:50799',
    'http://61.135.217.7:80',
    'http://58.53.128.83:3128',
    'http://101.236.57.99:8866',
    'http://218.79.86.236:54166',
    'http://121.31.193.97:8123',
    'http://144.123.94.34:8118',
    'http://115.46.97.204:8123'
]
