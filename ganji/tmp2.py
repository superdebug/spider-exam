from bs4 import BeautifulSoup
import requests
import time
import pymongo
import random



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

# spider 2
def get_item_info_from(url,data=None):
    wb_data = requests.get(url,headers=headers)
    if wb_data.status_code == 404:  #如果返回码是404的话  网络调试 network->doc status
        pass
    else:
        soup = BeautifulSoup(wb_data.text, 'lxml')
        areas =list( soup.select('div.info_lubotu.clearfix > div.info_massege.left > div.palce_li > span > i')[0].stripped_strings) if soup.find_all('div','palce_li') else None
        print(areas)
        data = {
#            'area': [area.text.strip() for area in areas if area.text!= '-'] 
        }
        print(data)

get_item_info_from('http://zhuanzhuan.ganji.com/detail/780298574148124676z.shtml')
