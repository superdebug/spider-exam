# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from selenium import webdriver
import time
from lxml import etree
from toutiao_shehui.items import ToutiaoShehuiItem
class ShehuiSpider(scrapy.Spider):
    name = "shehui"
    allowed_domains = ["www.toutiao.com"]
    start_urls = ['http://www.toutiao.com/']
    def parse(self, response):
        driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
        #executable_path为你的phantomjs可执行文件路径
        #打开头条军事频道
        driver.get("http://www.toutiao.com/news_society/")
        data = driver.page_source
        driver.quit
        
        #将获取的页面结果传递给变量并用xpaht解析
        selector = etree.HTML(data)
        #在栏目首页获取当前页面新闻页id
        #<a class="link title" href="/group/6382164011500175874/"
        links = selector.xpath('//a[@class="link title"]/@href')
        #<a class="img-wrap" target="_blank" href="/grou1761/"> <img alt="" src="http://p1.pstatp.9579dac2a"> 
        image_url =selector.xpath('//a[@class="img-wrap"]/img/@src')
        #urls=[]
        #for link in links:
        for i in range(0,len(links)+2):
            if links[0].find('/group/')==-1:
                x=9 
                #pass
            else:
                #构造完整的url地址
                #urls.append('http://www.toutiao.com'+link)
                this_url=('http://www.toutiao.com'+links[i])
                #print(this_url)
                yield Request(url=this_url,callback=self.next)

    def next(self,response):
        item = ToutiaoShehuiItem()
        title = response.xpath("//h1[@class='article-title']/text()").extract()
        image_urls=response.xpath("//div[@class='article-content']/img/@src").extract() #如果使用会导致新闻数量减少
        content = response.xpath("//div[@class='article-content']").extract()
        item['title']=title[0]
        item['content']=content[0]
        item['url'] =response.url
        item['image_url']=image_urls  #如果使用会这个字段会导致缺少爬取内容
        yield item        

