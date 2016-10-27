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
    #print(data)


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
#构造向服务器提交的参数
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/7.2.0.12990',
    'Cookie':'TAUnique=%1%enc%3AVopJqm1GEIaVmhAwItGeLKcHNOOPLSpOIXQ%2Be4bTfHV9i1%2B2aew%2BBQ%3D%3D; TASSK=enc%3AANo7j%2BFyjEH%2FD2ymySXvZa8B6z%2FY5sZ3%2FelDU%2BAX5L3tA%2F%2BYl9sfJAuv%2FD2TQZI2%2Fzc%2FjOkIcg%2BxkuY5d1cNthbG2FnTBdmgjNF94xJwgwkHEe8cj96LgrRVn9OfLfvjeg%3D%3D; TAPD=tripadvisor.cn; _smt_uid=580f08be.2c01d1a4; ki_u=16773db5-07f4-33d2-b26c-40a9; ki_s=167106%3A2.0.0.1.2; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.60763_299l105127_299*RS.1; bdshare_firstime=1477385866437; CommercePopunder=SuppressAll*1477385872369; TAAuth2=%1%3%3A4c8255fe55079ae883f608b465880e81%3AADnHFEzvAgdg8976M%2B7kBQ67ccJb%2BUGznRpNWp%2F7CPNTPoqTBRhuXMKki7QKAgSADRB1vQbYRZQq1YWB%2FAi4xX4d4p%2BLapI0Q4n9bxPiHYOexclW8bybXCcoFGs8do7RqQi6MpI%2FfZ2FpdpNMZc9OSgPxg%2FO91l8%2BOakgzxuuv5N8GDYjJPLPWS55b9IJfS%2BAFQ%2BtpTf74c2mzuul3XCZEXyt%2Bi1H2X6w8gcWEBTr6De; CM=%1%HanaPersist%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CFtrPers%2C%2C-1%7CHomeASess%2C1%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7Csesscoestorem%2C%2C-1%7CCpmPopunder_1%2C1%2C1477472406%7CCCSess%2C%2C-1%7CCpmPopunder_2%2C1%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C3%2C-1%7Csessamex%2C%2C-1%7Cperscoestorem%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7Csh%2C%2C-1%7CLastPopunderId%2C137-1859-null%2C-1%7Cpssamex%2C%2C-1%7C2016sticksess%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7C2016stickpers%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAReturnTo=%1%%2FAirAsia; roybatty=TNI1625!ACbkRU27U2fQu0Od0Q9S%2BiScAHHgZwuCxCtkPdBbdanxf5nt9d2Gt16ovdtX4tiKyWo8%2Be0qfeEi8nJGT9wJ3IjRiBqsgM8Jjue86qyJ98vmaKrBCYuPJiVqshbXj1wN2RO8q4gQGng5BM8i7v5aRZTdNYUxbsfdhZJ6zk9He1IB%2C1; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1477380286; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1477452785; ki_t=1477380289344%3B1477451068851%3B1477452785261%3B2%3B18; ki_r=; TASession=%1%V2ID.4B8A628DAC68048FB76A817DFE4314C7*SQ.80*LP.%2FLangRedirect%3Fauto%3D3%26origin%3Dzh%26pool%3DX%26returnTo%3D%252F*PR.427%7C*LS.ModuleAjax*GR.34*TCPAR.93*TBR.19*EXEX.99*ABTR.33*PPRP.42*PHTB.70*FS.17*CPU.74*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.3CF68A45C857AEAC9C4775B5C2C08BDD*LF.zhCN*FA.1*DF.0*IR.3*OD.zh*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.105127; TAUD=LA-1477380409058-1*LG-72523387-2.1.F.*LD-72523388-.....; NPID='
}        
url_saves = 'http://www.tripadvisor.cn/Saves#527016'
wb_data = requests.get(url_saves,headers=headers)
soup = BeautifulSoup(wb_data.text,'lxml')
#titles = soup.select('location-name') #网站已经改版做了防御，这个不能用了
titles = soup.select('#BODYCON > div.modules-saves-single-trip-view > div > div.trip_content > div.items > div > div.info > div.location_summary > div.title > a')
images = soup.select('img[width="54"]')
for title,images in zip(titles,images):
    data = {
            'title':title.get_text(),
            'image':image.get('src'),   
    }

    print(data)
#print (titles.get_text())
#print(soup)


