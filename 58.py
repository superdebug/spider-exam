from bs4 import BeautifulSoup
import requests

url='http://zhuanzhuan.58.com/detail/764814909242654724z.shtml'
wb_data=requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
#imgs = soup.select('div.infocon > tiable > tbody > tr > td.img > a > img')
title = soup.title.text  #这里的标题没有用selector方法，而是直接获取网页标题
price = soup.select('span.price_now ') #这里可以案中案唯一定位获取
'''解析结果
[<span class="price_now">现价：<i>240</i>元   </span>]
'''
area = soup.select('.palce_li')
'''解析结果 [<div class="palce_li">
<span>区域：<i>北京-丰台</i></span>
</div>]
'''
#print(price)
#infos = soup.select('div.infocon > table > tbody > tr > td.t > span.desc')
data = {
    'title':title,
    'price':price[0].text,
    'area':list(area[0].stripped_strings)

}        
print(data)

