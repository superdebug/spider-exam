from bs4 import BeautifulSoup
import requests

url='http://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
#向页面进行请求
wb_data=requests.get(url) 
#解析请求地址
soup=BeautifulSoup(wb_data.text,'lxml')
#print(soup)

#获取标题信息
#titles = soup.select('#ATTR_ENTRY_105127 > div.property_title > a')
titles = soup.select('div.property_title > a[target="_blank"]')

#图片搜索条件是宽和高都是160的图片 通过标签+方括号+特定属性值的方法来寻找需要的元素
imgs = soup.select('img[width="160"]')

#分类标签 由于标签有多个，存在多对一的关系，因此需要寻找其父级标签
cates = soup.select('div.p13n_reasoning_v2')

#将数据装入字典中
for title,img,cate in zip(titles,imgs,cates):
    data = {
        'title':title.get_text(),
        'img':img.get('src'),
        'cate':list(cate.stripped_strings),
    }        
    print(data)


'''
为了寻找不带有聚合信息的标题，这里抓取了带聚合信息的链接地址(上) 和不带聚合信息的链接地址(下)进行对比
<a href="/Attractions-g60763-Activities-c58-t111-New_York_City_New_York.html" data-params="cnk0Xy9BdHRyYWN0aW9ucy1nNjA3NjMtQWN0aXZpdGllcy1jNTgtdDExMS1OZXdfWW9ya19DaXR5X05ld19Zb3JrLmh0bWxfS3pv" onclick="ta.servlet.Attractions.narrow.setEvtCookieWrapper('Attraction_List_Click', 'Rollup_click', 'name', 11, 'b3BOXy9BdHRyYWN0aW9ucy1nNjA3NjMtQWN0aXZpdGllcy1jNTgtdDExMS1OZXdfWW9ya19DaXR5X05ld19Zb3JrLmh0bWxfRGpC'); ta.call('ta.servlet.Attractions.narrow.ajaxifyLink', event, this)">百老汇歌舞剧 (170)</a>

<a href="/Attraction_Review-g60763-d107466-Reviews-Frick_Collection-New_York_City_New_York.html" onclick="ta.setEvtCookie('Attraction_List_Click', 'POI_click', 'name', 10, '/Attraction_Review')" target="_blank">弗里克美术收藏馆</a>
发现不带聚合信息的地址中含有target="_blank"作为区别标志

'''

'''
向服务器提交伪造的cookie信息
账号登录后在调试器中network中点击任意链接，然后在header中寻找cookie信息

'''
