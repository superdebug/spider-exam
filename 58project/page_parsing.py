from bs4 import BeautifulSoup
import requests
import time
import pymongo

#创建数据库
client = pymongo.MongoClient('localhost',27017)
ceshi = client['ceshi'] #在ceshi数据库中下写入数据
url_list = ceshi['url_list3']
item_info = ceshi['item_info3']
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

def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    title=soup.title.text
    price =soup.select('div.price_li > span > i')[0].text
    #date = soup.select('look_time')[0].text
    #tag名称和属性的查找 soup.find_all('div','palce_li') 用于定位 <div class="palce_li">
    area = list(soup.select('div.palce_li > span > i')[0].stripped_strings) if soup.find_all('div','palce_li') else None
    #item_info.insert_one({'title':title,'price':price,'date':date,'area':area})
    print(area)

get_item_info("http://zhuanzhuan.58.com/detail/784993594887569412z.shtml")
#get_links_from('http://bj.58.com/shuma/',1)