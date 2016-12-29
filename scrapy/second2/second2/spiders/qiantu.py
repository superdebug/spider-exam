# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from second2.items import Second2Item


class QiantuSpider(scrapy.Spider):
    name = "qiantu"
    allowed_domains = ["www.58pic.com"]
    start_urls = ['http://www.58pic.com/']

    def parse(self, response):
        urldata=response.xpath("//div[@class='moren-content']//a/@href").extract()
        #print(urldata)
        #len(urldata)
        for i in range(0,len(urldata)):
            thisurldata=urldata[i]
            #print(thisurldata)
            yield Request(url=thisurldata,callback=self.next)
        pass
    def next(self,response):
        thisurl=response.url
        #print(thisurl)
        pagelist=response.xpath("//div[@id='showpage']/a/text()").extract()
        if(len(pagelist)>=2):
            page=pagelist[-2]
            #int(page) + 1
            for j in range(1,int(page) + 1):
                pageurl=thisurl+"id-"+str(j)+".html"
                #print(pageurl)
                yield Request(url=pageurl,callback=self.next2)
        else:
            pass
    def next2(self,response):
        print("此时正爬取页面---"+response.url+"----")
        item=Second2Item()
        #print("xx")
        item["url"]=response.xpath("//a[@class='thumb-box']/img/@src").extract()
        yield item

