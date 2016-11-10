#coding:utf-8
from bs4 import BeautifulSoup
import requests
#判断404页面是否存在
url = 'http://bj.58.com/shouji/24605954621114x.shtml'  #不存在的页面 404
#url= 'http://zhuanzhuan.58.com/detail/784993594887569412z.shtml'  #存在的页面
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
htmlsrc=str(soup)
is_404 = "topbar404.js" in htmlsrc
#查找网页源代码中是否有字符topbar404.js
if is_404:
    print ("It's 404 page")
else:
    print ("no 404")


#判断页面是否是否是404页面 这个验证不成功
#url = 'http://bj.58.com/shouji/24605954621114x.shtml'  #不存在的页面 404
# url= 'http://zhuanzhuan.58.com/detail/784993594887569412z.shtml'  #不存在的页面 404
# wb_data = requests.get(url)
# soup = BeautifulSoup(wb_data.text,'lxml')
# print(soup.prettify())
# no_longer_exist = 'tracklog.58.com' in soup.find('script',type="text/javascript").get('src').split('/')
# print(no_longer_exist)
#在文档的script标签中查找内容为type="text/javascript"，并在src中用/进行拆分为列表，并在列表中查找是否有404