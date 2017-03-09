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
LOG_FILE = 'jgdqedu_体育.log'
#定义日志文件信息并以追加模式记录日志
LOG_PATH_FILE= LOG_PATH+LOG_FILE
file_log = open(LOG_PATH_FILE, 'a')

#读取同义词库文件
tongyici_file=r"/opt/seo/synonym/mySeoWord.txt"
with open(tongyici_file, "rt") as handle:
    tongyici_data = [ln.replace('\n','').split(',') for ln in handle]


class JgdqeduPipeline(object):
    def __init__(self):
        self.conn=pymysql.connect(host="127.0.0.1",user="root",passwd="123456",db="spiderdb",charset="utf8")

    def process_item(self, item, spider):
        try:
            title = item['title'][0]
            for i in range(0,len(tongyici_data)): #对标题进行同义词替换
                title = title.replace(tongyici_data[i][0],tongyici_data[i][1])
            url = item['url']
            content=item['content'][0]
            for i in range(0,len(tongyici_data)): #对正文进行同义词替换
                content = content.replace(tongyici_data[i][0],tongyici_data[i][1])
            keywords = title
            catalog = item['catalog']
            sp_name = 'jgdqedu体育'
            desc_text = title
            print(title) 
            file_log.writelines('开始爬取jgdqedu网-体育栏目--'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
            file_log.writelines('文章标题--'+title+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
            file_log.writelines('文章地址--'+url+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
            print('*******************************************************')
            sql="insert into news_2(title,url,desc_text,catalog,content,sp_name) values('"+title+"','"+url+"','"+desc_text+"','"+catalog+"','"+content+"','"+sp_name+"')"
            self.conn.query(sql)
            self.conn.commit()
            return item
        except Exception as err:
            print('数据插入错误--'+err)
            file_log.writelines('数据插入错误--'+str(err)+'--'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
            pass
        return item

