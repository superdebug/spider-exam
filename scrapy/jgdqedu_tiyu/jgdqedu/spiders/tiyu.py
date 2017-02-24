# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import urllib.request
from jgdqedu.items import JgdqeduItem 

class TiyuSpider(scrapy.Spider):
    name = "tiyu"
    allowed_domains = ["jgdqedu.cn"]
    start_urls = ['http://jgdqedu.cn/']

    def parse(self, response):
        listpage='http://www.jgdqedu.cn/sports/'
        yield Request(url=listpage,callback=self.next)

    def next(self,response):
        print('处理列表页地址:')
        list_page = response.xpath("//div[@class='list-text']/ul/li/a/@href").extract()
        for i in range(0,len(list_page)):
            thisurl=('http://jgdqedu.cn'+list_page[i])
            #print(thisurl)
            yield Request(url=thisurl,callback=self.page)
    def page(self,response):
        item = JgdqeduItem()
        item['title'] = response.xpath('//h1/text()').extract()
        item['url']=response.url
        item['catalog']='体育'
        item['content']=response.xpath("//div[@class='content']").extract()
        yield item
