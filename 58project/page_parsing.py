from bs4 import BeautifulSoup
import requests
import time
import pymongo

#创建数据库
client = pymongo.MongoClient('localhost',27017)
ceshi = client['ceshi']
url_list = client['url_list3']

#spider 1 爬取所有商品的链接
def get_links_from(channel,pages,who_sells=0): #默认0表示个人
    #http://bj.58.com/diannao/1/pn2/
    print('!!')