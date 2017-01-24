# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import re

class IfengYulePipeline(object):
    def __init__(self):
        self.conn=pymysql.connect(host="127.0.0.1",user="root",passwd="123456",db="spiderdb",charset="utf8")

    def process_item(self, item, spider):
        try:
            title_1 = item['title'][0]
            title =title_1.replace('娱乐频道_凤凰网',"D1000娱乐网") 
            url = item['url']
            content=item['content'][0]
            keywords = title
            print(title)
            print(content)
            print(url)
            print('*******************************************************')
            sql="insert into news(title,url,content) values('"+title+"','"+url+"','"+content+"')"
            self.conn.query(sql)
            self.conn.commit()
            return item
        except Exception as err:
            print(err)     
            pass
        return item