# -*- coding: utf-8 -*-
import pymysql

class TaobaoPipeline(object):
    def __init__(self):
        #在默认的方法中开启/关闭数据库
        self.conn=pymysql.connect(host="127.0.0.1",user="root",passwd="123456",db="csdn",charset="utf8")
    def process_item(self, item, spider):
        try:
            title = item['title'][0]
            link = item['link']
            price = item['price'][0]
            comment=item['comment'][0]
            print(title)
            print(link)
            print(price)
            print(comment)
            sql="insert into taob(title,link,price,comment) values('"+title+"','"+link+"','"+price+"','"+comment+"')"
            self.conn.query(sql)
            self.conn.commit()
            return item
        except Exception as err:
            print(err)     
            pass
    def close_spider(self):
        self.conn.close()
