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
LOG_FILE = 'toutiao_shehui.log'
#定义日志文件信息并以追加模式记录日志
LOG_PATH_FILE= LOG_PATH+LOG_FILE
file_log = open(LOG_PATH_FILE, 'a')
class ToutiaoShehuiPipeline(object):
    def __init__(self):
        self.conn=pymysql.connect(host="127.0.0.1",user="root",passwd="123456",db="spiderdb",charset="utf8")

    def process_item(self, item, spider):
        #print(item['image_url'][0]) #不能调用标题图片，否则会少新闻
        try:
            title = item['title']
            print(title)
            #title =title_1.replace('娱乐频道_凤凰网',"")
            url = item['url']
            content=item['content'][0]
            keywords = title
            catalog = item['catalog']
            sp_name ='toutiao_shehui头条-社会'
            sql="insert into news(title,url,catalog,content,sp_name) values('"+title+"','"+url+"','"+catalog+"','"+content+"','"+sp_name+"')"
            self.conn.query(sql)
            self.conn.commit()
            file_log.writelines('开始爬取今日头条-社会栏目--'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
            file_log.writelines('文章标题--'+item['title']+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
            file_log.writelines('文章地址--'+item['url']+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
            return item
        except Exception as err:
            print(str(err))
            file_log.writelines('入库失败--'+str(err)+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
            pass
        
        file_log.close()
        return item
