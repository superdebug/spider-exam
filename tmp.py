#表达式方式循环url地址
urls = ['http://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'.format(str(i)) for i in range(30,930,30)]
print(urls)        
print('\n')

#字符串截取
print('字符串截取')
x='123456789'
print(x[-2:])

