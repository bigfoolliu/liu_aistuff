# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


"""
Item 是保存爬取到的数据的容器, 其使用方法和python字典类似,
并且提供了额外保护机制来避免拼写错误导致的未定义字段错误。
"""
import scrapy


class ScrapytutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ItcastItem(scrapy.Item):
    """
    ItcastSpider的, 定义需要抓取的结构化数据字段
    """
    name = scrapy.Field()  # 姓名
    level = scrapy.Field()  # 职称
    info = scrapy.Field()  # 介绍
    img = scrapy.Field()  # 头像


class TencentItem(scrapy.Item):
    """
    TencentSpider的字段容器
    """
    position_name = scrapy.Field()  # 职位名
    position_link = scrapy.Field()  # 职位链接
    position_type = scrapy.Field()  # 职位类别
    people_number = scrapy.Field()  # 招聘人数
    work_location = scrapy.Field()  # 工作地点
    publish_times = scrapy.Field()  # 发布时间


class TencentCrawlSpiderItem(scrapy.Item):
    """
    TencentCrawlSpiderSpider的字段容器
    记录详情页面的字段
    """
    position_duty = scrapy.Field()  # 工作职责
    position_requirement = scrapy.Field()  # 工作要求
