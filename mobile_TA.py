from bs4 import BeautifulSoup
import requests
#模拟手机浏览器下图盘的链接地址，只是目前该网站已经进行防御了，无法正常抓取了
headers = {
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}        
url = 'http://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
mb_data = requests.get(url,headers=headers)
soup = BeautifulSoup(mb_data.text,'lxml')
imgs = soup.select('div.thumb.thumbLLR.soThumb ')
for i in imgs:
    #print(i.get('data-thumburl'))
    print (i)
