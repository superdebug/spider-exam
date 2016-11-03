from bs4 import BeautifulSoup
import requests
url = 'http://zhuanzhuan.58.com/detail/769450608819126276z.shtml'
#获取url地址列表
def get_links_from(who_sells=0):
    urls = []
    list_view = 'http://bj.58.com/pingbandiannao/{}/'.format(str(who_sells))
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text,'lxml')
    for link in soup.select('td.t a.t'): #或者是 td.t > a
        urls.append(link.get('href').split('?')[0])
    return urls

#get_links_from()

#获取浏览量  目前该方法已经失效，仅供使用参考
def get_views(url):
    id = url.split('/')[-1].strip('z.shtml')#使用/进行分割，并获取最后一段内容，并将z.shtmls去掉
    api = 'http://jst1.58.com/counter?infoid={}'.format(id)
    js = requests.get(api)
    views = js.text.split('=')[-1]
    print(views)
    return views

get_views(url)    
