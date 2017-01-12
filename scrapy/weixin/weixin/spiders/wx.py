# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from weixin.items import WeixinItem
import urllib.request


class WxSpider(scrapy.Spider):
    name = "wx"
    allowed_domains = ["sogou.com"]
    start_urls = ['http://www.sogou.com/']

    def parse(self, response):
        #设置关键词
        key="python"
        #构建关键词各页(分页)的网址
        for i in range(1,4):
            thispage="http://weixin.sogou.com/weixin?query="+str(key)+"&type=2&page="+str(i)
            yield Request(url=thispage,callback=self.page)

    def page(self, response):
        print("在处理列表搜索页，得到文章地址")
        page_list = response.xpath("//div[@class='txt-box']/h3/a/@href").extract()
        print(page_list)
        print(len(page_list))
        for j in range(0,len(page_list)):
            # 构建列表页源码中的微信文章url链接地址
            print(page_list[j])
            page_url = page_list[j]
            print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
            yield Request(url=page_url,callback=self.next,dont_filter=True)

    def next(self,response):
        item = WeixinItem()
        print("*********************************************")
        yield item




'''
    def next2(self, response):
        print("此时正爬取页面----------------------------------")
        # item = WeixinItem()
        # item['title']=response.xpath("/title/text()").extract()
        # item['link']= response.url
        # item['price']=response.xpath("//em[@class='tb-rmb-num']/text()").extract()
 #       print(item['title'])
#        yield item
'''