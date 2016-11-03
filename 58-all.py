from bs4 import BeautifulSoup
import requests
import time

url = 'http://zhuanzhuan.58.com/detail/769450608819126276z.shtml'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/7.2.0.12990'
}
#从列表页中获取url链接
def get_links_from(who_sells=0):
    urls = []
    #urls = get_links_from()
    list_view = 'http://bj.58.com/pingbandiannao/{}/pn2'.format(str(who_sells))
    wb_data = requests.get(list_view,headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    for link in soup.select('td.t a.t'):  # 或者是 td.t > a
        urls.append(link.get('href').split('?')[0])
    return urls


# 获取浏览量  目前该方法已经失效，仅供使用参考
def get_views(url):
    id = url.split('/')[-1].strip('z.shtml')  # 使用/进行分割，并获取最后一段内容，并将z.shtmls去掉
    api = 'http://jst1.58.com/counter?infoid={}'.format(id)
    js = requests.get(api)
    views = js.text.split('=')[-1]
    return views

def get_item_info(who_sells=0):
        urls = get_links_from(who_sells)
        for url in urls:
            wb_data=requests.get(url,headers=headers)
            soup = BeautifulSoup(wb_data.text,'lxml')
            data = {
                'title':soup.title.text.strip('\r\n '),  #这里的标题没有用selector方法，而是直接获取网页标题,
                'price':soup.select('div.price_li > span > i')[0].text,
                'area':list(soup.select('div.palce_li > span > i')[0].stripped_strings),
                'views':soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.box_left_top > p > span.look_time')[0].text.strip('次浏览'), #浏览量
                'cate':'个人' if who_sells==0 else '商家',
            }
            time.sleep(4)
            print(data)

#get_views('http://zhuanzhuan.58.com/detail/769450608819126276z.shtml')
#get_links_from()
get_item_info()  #最终调用的函数

