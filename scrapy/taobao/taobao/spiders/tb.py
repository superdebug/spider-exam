# -*- coding: utf-8 -*-
import scrapy


class TbSpider(scrapy.Spider):
    name = "tb"
    allowed_domains = ["taobao.com"]
    start_urls = ['http://taobao.com/']

    def parse(self, response):
        key='零食' #建立一个变量存储关键词
                


        pass
