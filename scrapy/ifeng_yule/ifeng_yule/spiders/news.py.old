# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import urllib.request
from ifeng_yule.items import IfengYuleItem 
import datetime

#日志路径
LOG_PATH='/opt/log/spider_log/'
#日志文件
LOG_FILE = 'ifeng_news.log'

#定义日志文件信息并以追加模式记录日志
LOG_PATH_FILE= LOG_PATH+LOG_FILE
file_log = open(LOG_PATH_FILE, 'a')


#抓取凤凰网新闻栏目，作为国内新闻
class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["ent.ifeng.com"]
    start_urls = ['http://news.ifeng.com/mainland/']

    def parse(self, response):
        listpage='http://news.ifeng.com/mainland/'
        yield Request(url=listpage,callback=self.next)

    def next(self,response):
        print("处理列表页下url地址")
        #"//a[@class='list']/@href"
        list_page = response.xpath("//div[@class='box_list clearfix']/h2/a/@href").extract()
        for i in range(0,len(list_page)):
            thisurl=(list_page[i])
            yield Request(url=thisurl,callback=self.page)

    def page(self,response):
        item=IfengYuleItem()
        item['title']=response.xpath('//title/text()').extract()
        item['url']=response.url
        item['catalog']='国内'
        item['content']=response.xpath("//div[@class='js_selection_area']").extract()
        file_log.writelines('爬取文章标题--'+item['title'][0]+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
        yield item
