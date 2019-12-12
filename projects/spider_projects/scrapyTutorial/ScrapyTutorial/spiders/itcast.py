#!-*-coding:utf-8-*-
# !@Date: 2018/11/22 19:40
# !@Author: Liu Rui
# !@github: bigfoolliu


"""
抓取网页中的讲师的信息
网址: http://www.itcast.cn/channel/teacher.shtml

老师姓名: //div[@class="li_txt"]/h3
老师职称: //div[@class="li_txt"]/h4
老师介绍: //div[@class="li_txt"]/p
老师头像: http://www.itcast.cn + //div[@class="li_img"]/img/@data-original
"""
import scrapy

from ScrapyTutorial.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    """
    抓取爬虫
    """
    # 定义三个类属性(所有的对象共享同一个)
    name = 'itcast'  # 爬虫名(必须有且唯一)
    allowed_domains = ['itcast.cn']  # 允许进行爬取的域名列表,防止胡乱爬取(非必需)
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']  # 爬虫入口url列表

    def parse(self, response):
        """
        解析函数, 每一个请求都会进入此函数进行解析
        :param response:
        :return:
        """
        node_list = response.xpath("//div[@class='li_txt']")

        for node in node_list:
            # item = {}
            # 每个item表示一组数据
            item = ItcastItem()

            item['name'] = node.xpath("./h3/text()").extract_first()
            item['level'] = node.xpath("./h4/text()").extract_first()
            item['info'] = node.xpath("./p/text()").extract_first()
            item['img'] = 'http://www.itcast.cn' + node.xpath('../div[@class="li_img"]/img/@data-original').\
                extract_first()

            # 每次循环返回item数据给引擎，由引擎交给管道处理
            yield item  # 使得该函数成为一个生成器
