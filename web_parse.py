from bs4 import BeautifulSoup
'''    
            以下内容是通过网页中的审查元素的selector获取的                  
            body > div.main-content > ul > li:nth-child(1) > div.rate > span
            body > div.main-content > ul > li:nth-child(1) > div.article-info > p.description
            body > div.main-content > ul > li:nth-child(1) > div.article-info > h3 > a
            body > div.main-content > ul > li:nth-child(1) > img
            body > div.main-content > ul > li:nth-child(2) > div.article-info > p.meta-info > span:nth-child(2)
''' 
info = []
with open('/python3-exam/pachong/web/new_index.html','r') as wb_data:
    Soup = BeautifulSoup(wb_data,'lxml')
    # print(Soup)
    #这里注意去掉所有冒号:后面的内容
    images = Soup.select('body > div.main-content > ul > li > img')
    titles = Soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    descs = Soup.select('body > div.main-content > ul > li > div.article-info > p.description')
    rates = Soup.select('body > div.main-content > ul > li > div.rate > span')
    #cates = Soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info > span')
    #由于标签与文章是多对一的关系，因此应该在标签的父级元素停止，而不是到子节点上
    cates = Soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info')
#    print(images,titles,descs,rates,cates,sep='\n---------------------------------------------\n')




#利用for循环获取所有title信息 get_text方法可以获取标签中的文本信息
#for title in titles:
#    print(title.get_text())

#for desc in descs:
#    print(desc.get_text())

#使用zip函数对所有元素进行循环，并进行字典构造
for title,image,desc,rate,cate in zip(titles,images,descs,rates,cates):
    data={
            'title':title.get_text(),
            'rate':rate.get_text(),
            'desc':desc.get_text(),
            'cate':list(cate.stripped_strings), #获取父级标签下的所有子标签,并进行列表化处理
            'image':image.get('src')  #提取图片链接地址
    }
   # print(data)
    info.append(data)
