# -*- coding: utf-8 -*-
import scrapy
from huanqiu.items import HuanqiuItem
from scrapy.http import Request
import urllib.request

class YuleSpider(scrapy.Spider):
    name = "yule"
    allowed_domains = ["huanqiu.com"]
    start_urls = ['http://huanqiu.com/']

    def parse(self, response):
        listpage='http://ent.huanqiu.com/'
        yield Request(url=listpage,callback=self.next)

    def next(self,response):
        print("处理列表页")       
        #list_page=HuanqiuItem()
        #list_page['title'] = response.xpath("//dt//h3/text()").extract()
        list_page = response.xpath("//a[@class='list']/@href").extract()
        for i in range(0,len(list_page)):
            thisurl=(list_page[i])
            yield Request(url=thisurl,callback=self.page)

    def page(self,response):
        item=HuanqiuItem()
        item['title']=response.xpath('//title/text()').extract()
        #print(item['title'])
        item['url']=response.url
        #item['content']=response.xpath("//div[@class='conText']").extract()
        item['content']=response.xpath("//div[@class='text']").extract()
        #print(item['content'])
        #print('********************************************************************')
        #print(item['url'])
        return item
