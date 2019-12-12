# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import json

from ScrapyTutorial.items import ItcastItem, TencentItem, TencentCrawlSpiderItem


class ScrapytutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class ItcastPipeline(object):
    """
    ItcastSpider的管道,用来对解析后的数据进行存储
    运行爬虫时,输入命令: scrapy crawl itcast -o data/itcast.json则可以生成文件至指定目录
    """
    def open_spider(self, spider):
        """
        定义爬虫开始运行时的行为, 执行一次, 类似于__init__(self)函数
        :param spider:
        :return:
        """
        self.f = open('data/itcast.json', 'w')

    def process_item(self, item, spider):
        """
        将item传入,执行具体的保存策略, 可以执行多次, 传入一个item则执行一次
        :param item:
        :param spider:
        :return:
        """
        # TODO: 根据item的类型来告诉引擎将爬虫产生的items传入哪一个管道
        if isinstance(item, ItcastItem):
            item['spider'] = spider.name
            item['time'] = str(datetime.datetime.now())

            item['img'] = 'http://www.itcast.cn/' + dict(item)['img']

            json_str = json.dumps(dict(item)) + '\n'
            self.f.write(json_str)  # 写入json字符串

        # 注意一定要将item返回,因为不是传到该管道的时候, 需要传入下一个管道
        return item

    def close_spider(self, spider):
        """
        定义爬虫结束运行后的行为, 执行一次
        :param spider:
        :return:
        """
        self.f.close()


class TencentPipeline(object):
    """
    scrapy crawl itcast -o data/tencent.json则可以生成文件至指定目录
    """
    def open_spider(self, spider):
        self.f = open('data/tencent.json', 'w')

    def process_item(self, item, spider):
        """
        处理item容器
        :param item:
        :param spider:
        :return:
        """
        if isinstance(item, TencentItem):
            json_str = json.dumps(dict(item)) + '\n'
            self.f.write(json_str)  # 写入json字符串

        return item

    def close_spider(self, spider):
        self.f.close()


class TencentCrawlSpiderPipeline(object):
    """
    TencentCrawlSpiderSpider的管道
    """

    def open_spider(self, spider):
        self.f = open('data/tencent_crawlspider.json', 'w')

    def process_item(self, item, spider):
        if isinstance(item, TencentCrawlSpiderItem):
            json_str = json.dumps(dict(item)) + '\n'
            self.f.write(json_str)

        return item

    def close_spider(self, spider):
        self.f.close()
