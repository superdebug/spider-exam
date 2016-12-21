# -*- coding: utf-8 -*-
import re
import requests
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SecondPipeline(object):
    def process_item(self, item, spider):
        print(item['url'])
        for i in range(0,len(item['url'])):
            thisurl = item["url"][i]
            print(thisurl)
            print(item['url'][i])

        return item
