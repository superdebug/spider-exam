# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import re
from taobao.items import TaobaoItem

class TbSpider(scrapy.Spider):
    name = "tb"
    allowed_domains = ["taobao.com"]
    start_urls = ['https://taobao.com/']

    def parse(self, response):
        key='零食' #建立一个变量存储关键词

        #设置爬取的分页数量
        for i in range(0,3):
        # 构造爬取的网址
            #url="https://s.taobao.com/search?q=%E9%9B%B6%E9%A3%9F&s=88"
            url = "https://s.taobao.com/search?q="+str(key)+"&s="+str(44*i)
            #print(url)
            #发送一个请求，指定地址为url，设置回调函数是当前类下的page函数
            yield Request(url,callback=self.page)

    def page(self,response):
        body = response.body.decode("utf-8","ignore")
        #获取列表页中商品的链接，首先获取商品的id
        #使用正则查找所有以"nid":开头的所有字符，并以双引号""作为开头和结尾的标志，开启惰性模式(非贪婪模式)
        pitid = '"nid":"(.*?)"'
        allid=re.compile(pitid).findall(body)  #获取所有的id
        #print(allid)
        #遍历所有的id
        for j in range(0,len(allid)):
            thisid=allid[j]
            #构建需要爬取的商品详情页信息
            url1 = "https://item.taobao.com/item.htm?id="+str(thisid)
            #print(url1)
            yield Request(url=url1,callback=self.next)

    #提取商品的详细信息
    def next(self,response):
        item=TaobaoItem()
        '''
        <h3 class="tb-main-title" data-title="怡润狗狗零食鳕鱼牛肉粒方220g宠物比熊博美金毛泰迪小狗幼犬零食">
            怡润狗狗零食鳕鱼牛肉粒方220g宠物比熊博美金毛泰迪小狗幼犬零食
        </h3>
        '''
        item['title']=response.xpath("//h3[@class='tb-main-title']/@data-title").extract()
        item['link']= response.url
        '''
        <em class="tb-rmb-num">28.00</em>
        '''
        item['price']=response.xpath("//em[@class='tb-rmb-num']/text()").extract()
        print(item['price'])
        pass
