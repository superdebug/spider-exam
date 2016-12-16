# -*- coding: utf-8 -*-
import re
import urllib.request
import random
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SecondPipeline(object):
    def process_item(self, item, spider):
        #print(item["url"])
        for i in range(0,len(item["url"])):
            try:
                thisurl=item["url"][i]
                #print(thisurl)
                pat="http://pic.qiantucdn.com/58pic/(.*?).jpg!qt"
                id=re.compile(pat).findall(thisurl)[0]
                thistrueurl="http://pic.qiantucdn.com/58pic/"+id+"_1024.jpg"
                #print(thistrueurl)
                #避免名字重复，名字再加上个随机数
                file="/python3-exam/pics/"+id[-7:]+str(int(random.random()*10000))+".jpg"
		print(file)
                urllib.request.urlretrieve(thistrueurl,filename=file)
            except Exception as e:
                pass
        return item

