# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import re
from toutiao.items import ToutiaoItem


d_image_url = {'a':1}
class HotnewsSpider(scrapy.Spider):
    name = "hotnews"
    allowed_domains = ["www.toutiao.com"]
    start_urls = ['http://www.toutiao.com/']

    def parse(self, response):
        url = 'http://www.toutiao.com/'
        yield Request(url,callback=self.page_list)

    def page_list(self,response):
        body = response.body.decode("utf-8","ignore")
        
        #获取标题图片地址
        img_id='"image_url":"(.*?)"'
        img_tid=re.compile(img_id).findall(body)
        #获取文章url地址
        gid = '"group_id":"(.*?)"'
        tid = re.compile(gid).findall(body)  #获取所有的id

        for i in range(0,len(tid)):        
            thisid = tid[i]
            this_url = 'http://www.toutiao.com/a'+str(thisid)+'/'
            this_img_url = img_tid[i]
            image_url= this_img_url.replace('\\','')
            d_image_url[this_url]=image_url
            yield Request(url=this_url,callback=self.page)
        pass

    def page(self,response):
        item = ToutiaoItem()
        title = response.xpath("//h1[@class='article-title']/text()").extract()
        #如果标题有内容，说明是新闻页，进行爬去，否则不进行爬去 
        if len(title)==0 :
            pass
        else:
            item =  ToutiaoItem()
            item['title'] = title[0]
            #利用字典的键值对应关系，将文章url地址作为键，图片地址作为值
            item['image_url']=d_image_url[response.url]
            item['url'] = response.url
            content = response.xpath("//div[@class='article-content']").extract()
            item['content'] = content[0]
            yield item
