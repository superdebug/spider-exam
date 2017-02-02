# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import time
from lxml import etree


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
        #print(links)
        urls=[]
        for link in links:
            if link.find('/group/')==-1:
                pass
            else:
                #构造完整的url地址
                urls.append('http://www.toutiao.com'+link)
        print(urls)
        pass
