# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import urllib.request
from ifeng_yule.items import IfengYuleItem 


class YuleSpider(scrapy.Spider):
    name = "yule"
    allowed_domains = ["ent.ifeng.com"]
    start_urls = ['http://ent.ifeng.com/']

    def parse(self, response):
        listpage='http://ent.ifeng.com/listpage/3/1/list.shtml'
        yield Request(url=listpage,callback=self.next)

    def next(self,response):
        print("处理列表页下url地址")
        #"//a[@class='list']/@href"
        list_page = response.xpath("//div[@class='box_list clearfix']/h2/a/@href").extract()
        for i in range(0,len(list_page)):
            thisurl=(list_page[i])
            yield Request(url=thisurl,callback=self.page)

    def page(self,response):
        item=IfengYuleItem()
        item['title']=response.xpath('//title/text()').extract()
        item['url']=response.url
        item['content']=response.xpath("//div[@class='js_selection_area']").extract()
        yield item
