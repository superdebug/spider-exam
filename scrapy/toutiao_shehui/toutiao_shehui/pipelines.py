# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ToutiaoShehuiPipeline(object):
    def process_item(self, item, spider):
        #print(item['image_url'][0]) #不能调用标题图片，否则会少新闻
        print(item['title'])
        print(item['url'])
        return item
