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
LOG_FILE = 'toutiao_hotnews.log'
#定义日志文件信息并以追加模式记录日志
LOG_PATH_FILE= LOG_PATH+LOG_FILE
file_log = open(LOG_PATH_FILE, 'a')


class ToutiaoPipeline(object):
    def __init__(self):
        self.conn=pymysql.connect(host="127.0.0.1",user="root",passwd="123456",db="spiderdb",charset="utf8")

    def process_item(self, item, spider):
        try:
            title = item['title']
            #title =title_1.replace('娱乐频道_凤凰网',"D1000娱乐网") 
            url = item['url']
            content=item['content']
            keywords = title
            catalog = '待整理'
            image_url = item['image_url'] #原图片地址完整格式
            sp_name='toutiao头条热点'
            print(title)
            #print(content)
            #print(url)
            print('*******************************************************')
            sql="insert into news(title,url,catalog,image_url,content,sp_name) values('"+title+"','"+url+"','"+catalog+"','"+image_url+"','"+content+"','"+sp_name+"')"
            #print (sql)
            file_log.writelines('开始爬取今日头条-热点新闻--'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
            file_log.writelines('文章标题--'+title+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
            file_log.writelines('文章地址--'+url+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
            self.conn.query(sql)
            self.conn.commit()
            return item
        except Exception as err:
            file_log.writelines('数据插入失败--'+str(err)+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
            print(err)
            pass
        return item
