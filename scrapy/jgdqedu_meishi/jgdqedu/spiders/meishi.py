# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import urllib.request
from jgdqedu.items import JgdqeduItem 
import  configparser
config =  configparser.ConfigParser()
config.read('/opt/spider-exam/scrapy/jgdqedu/config.ini')



class MeishiSpider(scrapy.Spider):
    name = "meishi"
    allowed_domains = ["jgdqedu.cn"]
    start_urls = ['http://www.jgdqedu.cn/']

    def parse(self, response):
        listpage='http://www.jgdqedu.cn/food/'
        yield Request(url=listpage,callback=self.next)

    def next(self,response):
        print('处理列表页地址:')
        #list_page = response.xpath("//div[@class='list-text']/ul/li/a/@href").extract()
        ini_list=config.get("jgdqedu","list_page")
        list_page =response.xpath(ini_list).extract()

        for i in range(0,len(list_page)):
            thisurl=('http://www.jgdqedu.cn'+list_page[i])
            #print(thisurl)
            yield Request(url=thisurl,callback=self.page)
    def page(self,response):
        item = JgdqeduItem()
        #item['title'] = response.xpath('//h1/text()').extract()
        ini_title=config.get("jgdqedu","title")
        item['title'] =response.xpath(ini_title).extract()
        item['url']=response.url
        item['catalog']='美食'
        #item['content']=response.xpath("//div[@class='content']").extract()
        ini_content=config.get("jgdqedu","content")
        item['content']=response.xpath(ini_content).extract()
        yield item
