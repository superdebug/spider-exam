# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import urllib.request
from jiemian.items import JiemianItem 
import  configparser
config =  configparser.ConfigParser()
config.read('/opt/spider-exam/scrapy/jgdqedu/config.ini')

class YuleSpider(scrapy.Spider):
    name = "yule"
    allowed_domains = ["jiemian.com"]
    start_urls = ['http://www.jiemian.com/']

    def parse(self, response):
        listpage='http://www.jiemian.com/lists/25.html'
        yield Request(url=listpage,callback=self.next)

    def next(self,response):
        print('处理列表页地址:')
        ini_list=config.get("jiemian","list_page")
        list_page =response.xpath(ini_list).extract()    
        for i in range(0,len(list_page)-3):
            thisurl=list_page[i]
            yield Request(url=thisurl,callback=self.page)

    def page(self,response):
        item = JiemianItem()
        ini_title=config.get("jiemian","title")
        t_title=response.xpath(ini_title).extract()
        if (t_title[0]!=''): #将非新闻页面全部过滤掉
            item['title'] =response.xpath(ini_title).extract()
            print(item['title'])
            item['url']=response.url
            item['catalog']='娱乐'
            ini_content=config.get("jiemian","content")
            content=response.xpath(ini_content).extract()
            item['content']=content[0].replace('<!--------------------- 来源 --------------------><p>更多专业报道，请<a href="http://a.jiemian.com/index.php?m=app&amp;a=redirect" style="color:#113a65;" target="_blank">点击下载“界面新闻”APP</a></p>','')
            #正文中的#会导致插入数据库报错
            item['content']=item['content'].replace('#','')    
            #由于爬取的代码中含有单引号，所以需要替换成双引号，否则会报错        
            item['content']=item['content'].replace('\'','\"')            
            yield item
        else:
            pass
