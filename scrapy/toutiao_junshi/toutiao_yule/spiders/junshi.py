# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from selenium import webdriver
import time
from lxml import etree
from toutiao_yule.items import ToutiaoYuleItem
import datetime
import shutil
import os

class JunshiSpider(scrapy.Spider):
    name = "junshi"
    allowed_domains = ["www.toutiao.com"]
    start_urls = ['http://www.toutiao.com/']

    def parse(self, response):
        shutil.rmtree('/root/.local/share/') #每一次启动phantomjs之前都要删除其缓存
        os.mkdir('/root/.local/share/') 
        driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
        #executable_path为phantomjs可执行文件路径
        #打开头条'娱乐'频道
        driver.get("http://www.toutiao.com/news_military/")
        data = driver.page_source
        driver.quit
        #将获取的页面结果传递给变量并用xpaht解析
        selector = etree.HTML(data)
        #在栏目首页获取当前页面新闻页id
        #<a class="link title" href="/group/6382164011500175874/"
        links = selector.xpath('//a[@class="link title"]/@href')
        #<a class="img-wrap" target="_blank" href="/grou1761/"> <img alt="" src="http://p1.pstatp.9579dac2a"> 
        image_url =selector.xpath('//a[@class="img-wrap"]/img/@src')
        urls=[]
        for i in range(0,len(links)):
            if links[i].find('/group/')==-1:
                pass
            else:
                #构造完整的url地址
                #urls.append('http://www.toutiao.com'+link)
                urls.append('http://www.toutiao.com'+links[i])

        for j in range(0,len(urls)):
            this_url=urls[j]                
            #print(this_url)
            yield Request(url=this_url,callback=self.next)

    def next(self,response):
        item = ToutiaoYuleItem()
        #print(response.url)
        if response.url.find('toutiao.com')==-1:
            pass 
        else:
            title = response.xpath("//h1[@class='article-title']/text()").extract()
            content = response.xpath("//div[@class='article-content']").extract()
            item['url'] =response.url
            item['catalog'] ='军事'
            item['title']=title[0]
            item['content']=content
            item['url'] =response.url
            #item['catalog'] ='娱乐'
            yield item
'''
            #driver2 = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
            #driver2.manage().window().maximize()
            #driver2.get(response.url)
            #data2 = driver2.page_source
            #driver2.quit
            #print(data.decode('utf-8'))
            #print(data)
            #selector2 = etree.HTML(data2)
            #
            title = selector2.xpath("//h1[@class='article-title']/text()").extract()
            print('********/*/*/*/*')
            print(title)
            #title = response.xpath("//h1[@class='article-title']/text()").extract()
            titles = response.xpath("//h1[@class='article-title']/text()").extract()
            content = response.xpath("//div[@class='article-content']").extract()
            print(response.body.decode('utf8'))
            print(titles)
        title = response.xpath("//h1[@class='article-title']/text()").extract()
        #image_urls=response.xpath("//div[@class='article-content']/img/@src").extract() #如果使用会导致新闻数量减少
        content = response.xpath("//div[@class='article-content']").extract()
        #print(title[0])
        print('--------------------------------****************----------------------------')
        print(response.url)
        print(title)
        item['title']=title[0]
        item['content']=content
        item['url'] =response.url
        item['catalog'] ='娱乐'
        ##item['image_url']=image_urls  #如果使用会这个字段会导致缺少爬取内容
        #print(title[0])
        yield item
'''
