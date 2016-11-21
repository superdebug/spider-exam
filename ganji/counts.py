import time
from page_parsing import url_list,item_info

while True:
    print('链接地址数:'+str(url_list.find().count()))
    print('采集网页数:'+str(item_info.find().count()))
    print('--------------------\n')
    time.sleep(5)
