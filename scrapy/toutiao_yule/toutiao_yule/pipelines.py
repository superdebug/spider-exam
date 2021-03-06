# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import datetime

#日志路径
LOG_PATH='/opt/log/spider_log/'
#日志文件
LOG_FILE = 'toutiao_yule.log'
#定义日志文件信息并以追加模式记录日志
LOG_PATH_FILE= LOG_PATH+LOG_FILE
file_log = open(LOG_PATH_FILE, 'a')


class ToutiaoYulePipeline(object):
    def __init__(self):
        self.conn=pymysql.connect(host="127.0.0.1",user="root",passwd="123456",db="spiderdb",charset="utf8")
    def process_item(self, item, spider):
        try:
            title = item['title']
            print(title)
            url = item['url']
            print(url)
            content=item['content'][0]
            content=content.replace('本文为头条号作者发布，不代表今日头条立场。','') #替换代码无效？？？
            content=content.replace('204c433878d5cf9size1_w16_h16.png','')
            content=content.replace('本文为立方娱乐团队原创，未经授权禁止转载，版权沟通微信：fjoy0726','')
            content=content.replace('本文为头条号作者原创，未经授权，不得转载','')
            #content=content.replace('','')
          	
            keywords = title
            catalog = item['catalog']
            sp_name ='toutiao_shehui头条-娱乐'
            sql="insert into news(title,url,catalog,content,sp_name) values('"+title+"','"+url+"','"+catalog+"','"+content+"','"+sp_name+"')"
            self.conn.query(sql)
            self.conn.commit()
            file_log.writelines('开始爬取今日头条-娱乐栏目--'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
            file_log.writelines('文章标题--'+item['title']+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
            file_log.writelines('文章地址--'+item['url']+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
            return item
        except Exception as err:
            print(str(err))
            file_log.writelines('入库失败--'+str(err)+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
            pass
        return item
