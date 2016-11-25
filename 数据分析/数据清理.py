import pymongo
import charts
from string import punctuation
'''
作用：对数据进行清洗
将数据中区域中的符号-剔除掉
同时将区域中的空值设置为"不明"
'''

client = pymongo.MongoClient('localhost',27017)
ganji = client['ganji']
item_info=ganji['item_info']

for i in item_info.find().limit(600):
        print(i['area'])

#对数据进行清洗，将符号去掉，并将None替换为“不明”
for i in item_info.find():
    if i['area']:  #如果i['area']的值不为空
       area =[i for i in i['area'] if i not in punctuation] #查找i['area'] 中不包含标点符号的内容 放入are这个列表中
    else:
        area=['不明']
    item_info.update_one({'_id':i['_id']},{'$set':{'area':area}}) #将数据库中的内容按照循环进行逐个替换   
    print(area)

for i in item_info.find().limit(30):
    print(i['area'])

series = [{
        'name':'OS X',
        'data':[11],
        'type':'column'
    },{
        'name':'Ubunut',
        'data':[8],
        'type':'column'
    },{
      'name':'Windows'  ,
      'data':[12],
        'type':'column'
    },{
        'name':'Ohters',
        'data':[29],
        'type':'column'
    }
    
]
series2 = [{'names':'John','data':[5],'type':'column'},{'names':'John','data':[5],'type':'column'}]

charts.plot(series,show='inline',options=dict(title=dict(text='Charts are AWESOME')))

