# -*- coding: utf-8 -*-
import scrapy
#导入类items
from  fst1.items import Fst1Item

class CsdnSpider(scrapy.Spider):
    name = "csdn"
    allowed_domains = ["csdn.net"]
    start_urls = ['http://blog.csdn.net/']

    def parse(self, response):
        it=Fst1Item() #实例化对象
        it["title"]=response.xpath('//h3[@class="tracking-ad"]/a/text()').extract() #获取标题的信息
        #title文章名网页代码信息 <h3 class="tracking-ad" style="display: none;"><a href="http://blog.csdn.net/iwanghang/article/details/8766" ">Android开发-准备~</a></h3>
        #//*[@id="listBot"]/dl/dd/h3/a/text() 从浏览器获取的信息不完整
        it["detail"]=response.xpath('//div[@class="blog_list_c"]/text()').extract()
        #文章内容信息是<div class="blog_list_c">  提取规则是所有div标签，class属性是blog_list_c的
        it["links"] = response.xpath('//h3[@class="tracking-ad"]/a/@href').extract()
        yield it
        pass
