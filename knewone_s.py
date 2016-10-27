from bs4 import BeautifulSoup
import requests

url = 'https://knewone.com/discover?page=7'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
'''
通过检查 selector中选取的原始数据为
div > section > div:nth-child > div.hits_group-things.clearfix > article:nth-child > header > a > img
div > section > div:nth-child > div.hits_group-things.clearfix > article:nth-child > section > h4 > a
注意这里放入soup之后要去掉冒号:以后的内容
'''
#imgs = soup.select('a.cover-inner > img')
imgs = soup.select('div > section > div > div.hits_group-things.clearfix > article > header > a > img')
#titles = soup.select('section.content > h4 > a')
titles = soup.select('div > section > div > div.hits_group-things.clearfix > article > section > h4 > a')
#links = soup.select('section.content > h4 > a')
links = soup.select('div > section > div > div.hits_group-things.clearfix > article > section > h4 > a')
#print (soup)

for img,title,link in zip(imgs,titles,links):
    data={
        'img':img.get('src'),
        'title':title.get('title'),
        'link':link.get('href')
    }
    print(data)

