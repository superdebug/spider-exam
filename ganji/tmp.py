from multiprocessing import Pool
from page_parsing import get_item_info_from,url_list,item_info,get_links_from
from channel_extracing import channel_list
#断点续传
db_urls = [item['url'] for item in url_list.find()]
index_urls = [item['title'] for item in item_info.find()]
x = set(db_urls)
#print(x)
y = set(index_urls)
#print (y)
rest_of_urls = x-y

print(rest_of_urls)

