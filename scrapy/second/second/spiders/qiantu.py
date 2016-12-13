# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class QiantuSpider(scrapy.Spider):
    name = "qiantu"
    allowed_domains = ["58pic.com"]
    start_urls = ['http://58pic.com/']

    def parse(self, response):
        #获取所有栏目的链接
        #获取所有div下class名为moren-contend下 所有a标签下的href下的内容
        urldata = response.xpath("//div[@class='moren-content']//a/@href").extract()
        #print(urldata)
        for i in range(0,len(urldata)):
            #print(urldata[i])
            thisurldata = urldata[i]
            print(thisruldata)
            yield Request(url=thisurldata,callback=self.next)
    def next(self,response):
        pagelist = response.xpath("//div[@id='showpage']/a/text()").extract()
        print(pagelist)

        pass
