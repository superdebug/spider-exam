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
            #title =title_1.replace('娱乐频道_凤凰网',"D1000娱乐网") 
            title =title_1.replace('娱乐频道_凤凰网',"") 
            url = item['url']
            #去掉原网站logo及链接
            content=item['content'][0].replace('<span class="ifengLogo"><a href="http://www.ifeng.com/" target="_blank"><img src="http://p2.ifengimg.com/a/2016/0810/204c433878d5cf9size1_w16_h16.png"></a></span>','')
            content=item['content'][0]
            keywords = title
            catalog = item['catalog']
            sp_name = 'ifeng_yule凤凰娱乐' 
            #catalog = '娱乐'
            print(title)
            print(content)
            print(url)
            print('*******************************************************')
            #sql="insert into news(title,url,content,catalog) values('"+title+"','"+url+"','"+content+"')"
            #sql="insert into news(title,url,catalog,content) values('"+title+"','"+url+"','"+catalog+"','"+content+"')"
            sql="insert into news(title,url,catalog,content,sp_name) values('"+title+"','"+url+"','"+catalog+"','"+content+"','"+sp_name+"')"
            print (sql)
            self.conn.query(sql)
            self.conn.commit()
            return item
        except Exception as err:
            print(err)     
            pass
        return item
