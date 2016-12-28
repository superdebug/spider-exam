# -*- coding: utf-8 -*-
import re
import urllib
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


'''
缩略图
http://pic.qiantucdn.com/58pic/25/55/86/25H58PICTgE.jpg!qtwebp226
高清图
http://pic.qiantucdn.com/58pic/25/55/86/25H58PICTgE_1024.jpg
'''

class SecondPipeline(object):
    def process_item(self, item, spider):
        for i in range(0,len(item['url'])):
            thisurl = item["url"][i] #将列表中的图片url地址赋值给thisurl
            #使用正则表达式匹配图片地址
	    pat='http://pic.qiantucdn.com/58pic/(.*?).jpg!qt'
            id=re.compile(pat).findall(thisurl)[0]
	    thistrueurl = "http://pic.qiantucdn.com/58pic/"+id+"_1024.jpg"
            print(thistrueurl)	 
            file="/python3-exam/rst2/"+id[-7:]+".jpg"  #设置图片文件存储路径 并将id的后7位作为文件名
            urllib.urlretrieve(thistrueurl,filename=file)	
        return item
