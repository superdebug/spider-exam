# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HuanqiuPipeline(object):
    def process_item(self, item, spider):
        title = item['title'][0]
        url = item['url']
        content=item['content'][0]
        print(title)
        print(content)
        print(url)
        return item
