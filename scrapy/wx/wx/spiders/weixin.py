# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from wx.items import WxItem
class WeixinSpider(scrapy.Spider):
    name = "weixin"
    allowed_domains = ["sogou.com"]
    start_urls = ['http://weixin.sogou.com/']

    def parse(self, response):
        #设置关键词
        key="python"
        #构建关键词各页(分页)的网址
        for i in range(1,2):
            #http://weixin.sogou.com/weixin?query=python&type=2&page=2
            thispage="http://weixin.sogou.com/weixin?query="+str(key)+"&type=2&page="+str(i)
            yield Request(url=thispage,callback=self.page)

    def page(self,response):
        #创建Item对象
        item=WxItem()
        print("在处理列表搜索页，得到文章地址")
        item['title']=response.xpath("//div[@class='txt-box']/h3/a/text()").extract()
        '''<div class="txt-box"> <h3> <a target="_blank" href='.....'''
        item['link'] = response.xpath("//div[@class='txt-box']/h3/a/@href").extract()
        #描述信息样式 <p class="txt-info" id="sogou_vr_11002601_summary_0">来源:思诚之道链接
        item['describe'] = response.xpath("//p[@class='txt-info']/text()").extract()
        print(len(item['link']))

        yield item