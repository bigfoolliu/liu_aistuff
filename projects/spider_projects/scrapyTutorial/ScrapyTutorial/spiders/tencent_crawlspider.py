# -*- coding: utf-8 -*-
# !@Date: 2018/11/24 21:49
# !@Author: Liu Rui
# !@github: bigfoolliu


import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ScrapyTutorial.items import TencentCrawlSpiderItem


class TencentCrawlSpiderSpider(CrawlSpider):
    """
    腾讯社招爬虫CrawlSpider版
    可以通过一级页面获取到链接, 进而爬取到二级页面的详细信息
    """
    name = 'tencent3'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0']

    # TODO: 注意此处正则表达式对特殊符号的转义
    rules = [
        Rule(LinkExtractor(allow=r'start=\d+'), follow=True),  # 解析的列表页
        Rule(LinkExtractor(allow=r'position_detail\.php\?id=\d+'), callback='parse_page', follow=False)  # 解析的详情页
    ]

    def parse_page(self, response):
        """
        解析提取到的详情链接
        :param response:
        :return:
        """
        item = TencentCrawlSpiderItem()

        item['position_duty'] = response.xpath('//ul[@class="squareli"]')[0].xpath('./li/text()').extract()
        item['position_requirement'] = response.xpath('//ul[@class="squareli"]')[1].xpath('./li/text()').extract()

        yield item

