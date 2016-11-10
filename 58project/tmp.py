#coding:utf-8
from bs4 import BeautifulSoup
import requests
#判断404页面是否存在
url = 'http://bj.58.com/shouji/24605954621114x.shtml'  #不存在的页面 404
#url= 'http://zhuanzhuan.58.com/detail/784993594887569412z.shtml'  #存在的页面
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
htmlsrc=str(soup.getText)
#查找网页源代码中是否有字符topbar404.js
if "topbar404.js" in htmlsrc:
    print ("It's 404 page")
else:
    print ("no 404")
