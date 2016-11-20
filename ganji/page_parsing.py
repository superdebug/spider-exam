from bs4 import BeautifulSoup
import requests
import time
import pymongo
import random


client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
url_list = ganji['url_list']
item_info = ganji['item_info']

#随机UA
userAgent = random.choice(['Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36', 
                           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36', 
                           'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36', 
                           'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36',  
                           'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',   
                           'Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
                            ])


headers  = {
    'User-Agent':userAgent,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept - Encoding': 'gzip, deflate, sdch',
    'Accept - Language': 'zh - CN, zh;q = 0.8, en;q = 0.6',
    'Cache - Control': 'max - age = 0',
    'Connection': 'keep - alive'
}

# http://cn-proxy.com/
proxy_list = [
    'http://117.79.93.39:8808',
    ]
proxy_ip = random.choice(proxy_list) # 随机获取代理ip
proxies = {'http': proxy_ip}



# spider 1
def get_links_from(channel, pages, who_sells='o'):
    # http://bj.ganji.com/ershoubijibendiannao/o3/
    # o for personal a for merchant
    list_view = '{}{}{}/'.format(channel, str(who_sells), str(pages))
    print(list_view)
    #wb_data = requests.get(list_view,headers=headers,proxies=proxies)
    wb_data = requests.get(list_view,headers=headers) #暂时不用代理ip
    #随机访问延时
    i = random.randrange(0, 3)
    time.sleep(i)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if soup.find('ul', 'pageLink'): #判断是否有分页标识代码 ： <ul class="pageLink clearfix">
        for link in soup.select('tr > td.t > a'):
            item_link = link.get('href')
            url_list.insert_one({'url': item_link})
            print(item_link)
            # return urls
    else:
        # It's the last page !
        print('pass')
        pass
#get_links_from('http://bj.ganji.com/ershoubijibendiannao/','3')


# spider 2
def get_item_info_from(url,data=None):
    wb_data = requests.get(url,headers=headers)
    if wb_data.status_code == 404:  #如果返回码是404的话  网络调试 network->doc status
        pass
    else:
        soup = BeautifulSoup(wb_data.text, 'lxml')
        data = {
            'title':soup.title.text.strip(),
            'price':soup.select('div.price_li > span > i')[0].text.strip(),
            #'pub_date':soup.select('.pr-5')[0].text.strip().split(' ')[0],
            'area':list(map(lambda x:x.text,soup.select('div.palce_li > span > i'))),
            #'cates':list(soup.select('div.biaoqian_li > span')[0].stripped_strings),
            'url':url
        }
        print(data)
        item_info.insert_one(data)

#get_item_info_from('http://zhuanzhuan.ganji.com/detail/780298574148124676z.shtml')
