from bs4 import BeautifulSoup
import requests

#获取url地址列表
def get_links_from(who_sells=0):
    urls = []
    list_view = 'http://bj.58.com/pingbandiannao/{}/'.format(str(who_sells))
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text,'lxml')
    for link in soup.select('td.t a.t'): #或者是 td.t > a
        urls.append(link.get('href').split('?')[0])
    return urls
get_links_from()

#获取浏览量
def get_views(url):
    id = url.split('/')[-1].strip('z.shtml')
    print(id)

get_views('http://zhuanzhuan.58.com/detail/782150207541690372z.shtml?fullCate=5%2C38484%2C23094&fullLocal=1&from=pc&PGTID=0d305a36-0000-13d4-9b36-763cf12fd369&ClickID=2')    
