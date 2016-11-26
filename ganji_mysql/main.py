from multiprocessing import Pool
from page_parsing import get_item_info_from,url_list,item_info,get_links_from
from channel_extracing import channel_list
import pymysql

#获取数据库url_list及iteminfo表中的数据
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='ganji',charset='utf8')
cursor = conn.cursor() 
t_url_list=conn.cursor()
t_url_list.execute("select url from url_list")


#游标归零，默认mode='relative'  
#cursor.scroll(0,mode='absolute')
t_item_info = conn.cursor()
t_item_info.execute("select url from item_info")
#t_item_info = cursor.execute("select url from item_info")


#断点续传
db_urls = []
for item in t_url_list.fetchall():
    db_urls.append(('%s' % item))
print(db_urls)

#index_urls = [item['url'] for item in t_item_info.fetchall()]
index_urls =[]
for item in t_item_info.fetchall():
    index_urls.append(('%s' % item))
print(index_urls)    


x = set(db_urls)
y = set(index_urls)
rest_of_urls = x-y

def get_all_links_from(channel):
    for i in range(1,100):
        get_links_from(channel,i)

rest_of_urls

if __name__ == '__main__':
    pool = Pool(processes=1)
    # pool = Pool()

    #步骤一 先执行下面的这个函数，用来爬取所有的链接 
    pool.map(get_all_links_from,channel_list.split())

    #步骤二 后执行这个函数用来爬取所有详情页 
    #pool.map(get_item_info_from, rest_of_urls)

    pool.close()
    pool.join()
    
