from bs4 import BeautifulSoup
import requests
import time

url_saves = 'http://www.tripadvisor.cn/Saves#527016'
url='http://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
#使用列表解析式来遍历出url地址
urls = ['http://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'.format(str(i)) for i in range(30,930,30)]
headers = {
      'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/7.2.0.12990',
      'Cookie':'TAUnique=%1%enc%3AVopJqm1GEIaVmhAwItGeLKcHNOOPLSpOIXQ%2Be4bTfHV9i1%2B2aew%2BBQ%'
} 

def get_attractions(url,data=None):
	wb_data=requests.get(url) 
	time.sleep(4) #请求一次停2秒
	soup=BeautifulSoup(wb_data.text,'lxml')
	titles = soup.select('div.property_title > a[target="_blank"]')
	imgs = soup.select('img[width="160"]')
	cates = soup.select('div.p13n_reasoning_v2')
	for title,img,cate in zip(titles,imgs,cates):
	    data = {
	        'title':title.get_text(),
        	'img':img.get('src'),
	        'cate':list(cate.stripped_strings),
   		 }        
	    print(data)
#抓取内页暂时无效
def get_favs(url,data=None):
	wb_data = requests.get(url_saves,headers=headers)
	soup = BeautifulSoup(wb_data.text,'lxml')
	titles = soup.select('#BODYCON > div.modules-saves-single-trip-view > div > div.trip_content > div.items > div > div.info > div.location_summary > div.title > a')
	images = soup.select('div.modules-saves-single-trip-view > div > div.trip_content > div.items > div:nth-child > div.info > div.thumbnail')
	for title,images in zip(titles,images):
	    data = {
	            'title':title.get_text(),
	            'image':image.get('src'),   
	    }
	    print(data)
	
#get_attractions(url,)
#get_favs(url_saves)

#将所有地址进行遍历爬取数据
for single_url in urls:
    get_attractions(single_url)

