# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Fst1Pipeline(object):
    def process_item(self, item, spider):
        for i in range(0,len(item["title"])):
            print('第'+str(i+1)+'篇文章是')                
            print(item["title"][i])       
            print(item["detail"][i])
            print(item["links"][i]) 
            print('------------------')
        return item
