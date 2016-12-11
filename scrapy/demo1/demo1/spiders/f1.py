# -*- coding: utf-8 -*-
import scrapy


class F1Spider(scrapy.Spider):
    name = "f1"
    allowed_domains = ["baidu.com"]
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
