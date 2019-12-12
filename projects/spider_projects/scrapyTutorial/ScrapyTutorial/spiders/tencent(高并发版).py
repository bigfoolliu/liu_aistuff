#!-*-coding:utf-8-*-
# !@Date: 2018/11/25 8:54
# !@Author: Liu Rui
# !@github: bigfoolliu


import scrapy

from ScrapyTutorial.items import TencentItem


class TencentSpider(scrapy.Spider):
    """
    腾讯社招爬虫
    将所有请求的url地址全部放置在start_urls中,一次发给引擎请求
    """
    name = 'tencent2'
    allowed_domains = ['hr.tencent.com']
    # 除了使用列表推导式, 还可以读取文件的方式等
    start_urls = ['https://hr.tencent.com/position.php?&start=' + str(page) for page in range(0, 2861, 10)]

    def parse(self, response):
        """
        解析函数
        :param response:
        :return:
        """
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

        for node in node_list:
            item = TencentItem()
            item['position_name'] = node.xpath("./td[1]/a/text()").extract_first()  # 职位名
            item['position_link'] = "https://hr.tencent.com/" + node.xpath("./td[1]/a/@href").extract_first()  # 详情链接
            item['position_type'] = node.xpath("./td[2]/text()").extract_first()  # 职位类型
            item['people_number'] = node.xpath("./td[3]/text()").extract_first()  # 招聘人数
            item['work_location'] = node.xpath("./td[4]/text()").extract_first()  # 工作地点
            item['publish_times'] = node.xpath("./td[5]/text()").extract_first()  # 发布时间

            # 每次迭代提取一组数据item，通过yield 交给引擎-管道
            yield item

        # 判断是否是最后一页，如果不是最后一页，则正常提取下一页的链接并发送请求
        if not response.xpath("//a[@class='noactive' and @id='next']"):
            next_url = "https://hr.tencent.com/" + response.xpath("//a[@id='next']/@href").extract_first()

            yield scrapy.Request(next_url, callback=self.parse)
