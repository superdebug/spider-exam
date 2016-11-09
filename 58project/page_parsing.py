from bs4 import BeautifulSoup
import requests
import time
import pymongo

#创建数据库
client = pymongo.MongoClient('localhost',27017)
ceshi = client['ceshi'] #在ceshi数据库中下写入数据
url_list = ceshi['url_list3']

#spider 1 爬取选定频道下所有商品的链接
def get_links_from(channel,pages,who_sells=0): #默认0表示个人
    #http://bj.58.com/diannao/1/pn2/
    list_view = '{}{}/pn{}/'.format(channel,str(who_sells),str(pages))
    print(list_view)
    wb_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text,'lxml')
    #判断列表页是否含有td元素，如果有，则证明有内容，否则表示没有内容了，将不再抓取
    if soup.find('td','t'): #如果查找td样式的标签,返回的结果是真(t),则接着往下解析
        for link in soup.select('td.t a.t'):
            item_link = link.get('href').split('?')[0]
            #url_list.insert_one({'url':item_link}) #向数据库中的插入链接数据
            print(item_link)
    else:
        pass
        #Nothing
get_links_from('http://bj.58.com/shuma/',1)