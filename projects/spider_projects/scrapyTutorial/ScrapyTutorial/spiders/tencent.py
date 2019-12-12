#!-*-coding:utf-8-*-
# !@Date: 2018/11/22 21:49
# !@Author: Liu Rui
# !@github: bigfoolliu


import scrapy

from ScrapyTutorial.items import TencentItem


class TencentSpider(scrapy.Spider):
    """
    腾讯社招爬虫
    """
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    page = 0
    base_url = 'https://hr.tencent.com/position.php?&start='
    start_urls = [base_url + str(page)]

    def parse(self, response):
        """
        解析函数
        :param response:
        :return:
        """
        # 根据下一页的属性 class="noactive"来终止
        if response.xpath('//a[@id="next"]/@class').extract_first() == 'noactive':
            return

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

        # 重新构建新的请求并回调至该解析函数
        self.page += 10
        yield scrapy.Request(url=self.base_url + str(self.page), callback=self.parse)



