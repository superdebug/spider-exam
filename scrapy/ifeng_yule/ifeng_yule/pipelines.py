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
LOG_FILE = 'ifeng_yule.log'
#定义日志文件信息并以追加模式记录日志
LOG_PATH_FILE= LOG_PATH+LOG_FILE
file_log = open(LOG_PATH_FILE, 'a')
    
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
            file_log.writelines('开始爬取凤凰网-娱乐栏目--'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
            file_log.writelines('文章标题--'+title+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
            file_log.writelines('文章地址--'+url+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
            #print(url)
            print('*******************************************************')
            sql="insert into news(title,url,catalog,content,sp_name) values('"+title+"','"+url+"','"+catalog+"','"+content+"','"+sp_name+"')"
            print (sql)
            self.conn.query(sql)
            self.conn.commit()
            return item
        except Exception as err:
            #print(err)    
            file_log.writelines('数据插入错误--'+str(err)+'--'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n') 
            pass
#        file_log.close()
        return item
