# -*- coding: utf-8 -*-
import scrapy
from  fst1.items import Fst1Item

class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        item=Fst1Item()
        item["title"]=response.xpath('/html/head/title/text()').extract()
        yield item				
        #print(item["title"])
        #pass
