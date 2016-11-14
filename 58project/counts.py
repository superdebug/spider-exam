import time
from page_parsing import url_list

#爬取监控程序,计数监控程序
while True:
    print (url_list.find().count()) #从数据库的表url_list(url_list3)中查找数据记录数
    time.sleep(5)

