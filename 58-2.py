from bs4 import BeautifulSoup
import requests

url='http://zhuanzhuan.58.com/detail/764814909242654724z.shtml'

def get_item_info(who_sells):
    wb_data=requests.get(who_sells)
    soup = BeautifulSoup(wb_data.text,'lxml')
    #imgs = soup.select('div.infocon > tiable > tbody > tr > td.img > a > img')
    title = soup.title.text  #这里的标题没有用selector方法，而是直接获取网页标题
    #price = soup.select('span.price_now ') #这里可以案中案唯一定位获取
    price = soup.select('div.price_li > span > i') #这里可以案中案唯一定位获取
    '''解析结果
    [<i>240</i>]
    '''
    area = soup.select('div.palce_li > span > i')
    '''解析结果 [<div class="palce_li">
    [<i>北京-丰台</i>]
    '''
    #print(price)
    #infos = soup.select('div.infocon > table > tbody > tr > td.t > span.desc')
    data = {
        'title':title,
        'price':price[0].text,
        'area':list(area[0].stripped_strings)
    }        
    print(data)

get_item_info(url)
