# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import re
import datetime

#日志路径
LOG_PATH='/opt/log/spider_log/'
#日志文件
LOG_FILE = 'jgdqedu_美食.log'
#定义日志文件信息并以追加模式记录日志
LOG_PATH_FILE= LOG_PATH+LOG_FILE
file_log = open(LOG_PATH_FILE, 'a')

class JgdqeduPipeline(object):
    def __init__(self):
        self.conn=pymysql.connect(host="127.0.0.1",user="root",passwd="123456",db="spiderdb",charset="utf8")

    def process_item(self, item, spider):
        try:
            title = item['title'][0]
            url = item['url']
            content=item['content'][0]
            keywords = title
            catalog = item['catalog']
            sp_name = 'jgdqedu美食'
            desc_text = title
            print(title) 
            file_log.writelines('开始爬取jgdqedu-美食栏目--'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
            file_log.writelines('文章标题--'+title+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
            file_log.writelines('文章地址--'+url+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
            print('*******************************************************')
            sql="insert into news(title,url,desc_text,catalog,content,sp_name) values('"+title+"','"+url+"','"+desc_text+"','"+catalog+"','"+content+"','"+sp_name+"')"
            self.conn.query(sql)
            self.conn.commit()
            return item
        except Exception as err:
            print('数据插入错误--'+err)
            file_log.writelines('数据插入错误--'+str(err)+'--'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
            pass
        return item

