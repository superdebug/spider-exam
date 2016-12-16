# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from second.items import SecondItem

class QiantuSpider(scrapy.Spider):
    name = "qiantu"
    allowed_domains = ["58pic.com"]
    start_urls = ['http://58pic.com/']

    def parse(self, response):
        #获取首页所有栏目的链接
        #获取所有div下class名为moren-contend下 所有a标签下的href下的内容
        urldata = response.xpath("//div[@class='moren-content']//a/@href").extract()
        #for i in range(0,len(urldata)):
        for i in range(0,1):
            thisurldata = urldata[i]
            yield Request(url=thisurldata,callback=self.next)  #callback的功能是指定回调函数,即下一次的函数名

    def next(self,response):
        thisurl = response.url
        #print(thisurl)
        #获取列表页链接
        pagelist = response.xpath("//div[@id='showpage']/a/text()").extract()
        #print(pagelist);
        if (len(pagelist)>=2):
            page=pagelist[-2]
            #print(page)
            #for j in range(j,int(page)+1):
            for j in range(1,2):
                #分页页面的网址
                pageurl = "http://www.58pic.com/psd/0/id-"+str(j)+".html"
                #print(pageurl)
                #在分页页面中需要进入内页去访问 ,通过yield跳转到next2函数
                yield Request(url = pageurl,callback = self.next2 )
        else:
            pass
    def next2(self,response):
        print("此时正爬取页面---"+response.url+"----")
        item=SecondItem()
        #print("xx")
        item["url"]=response.xpath("//a[@class='thumb-box']/img/@src").extract()
        yield item    
