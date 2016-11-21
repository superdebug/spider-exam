from multiprocessing import Pool
from page_parsing import get_item_info_from,url_list,item_info,get_links_from
from channel_extracing import channel_list
#断点续传
db_urls = [item['url'] for item in url_list.find()]
index_urls = [item['url'] for item in item_info.find()]
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
   # pool.map(get_item_info_from, rest_of_urls)

    pool.close()
    pool.join()
    
