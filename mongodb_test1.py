import pymongo

client = pymongo.MongoClient('localhost',27017)
walden = client['walden']
sheet_tab = walden['sheet_tab']

# path = '/python3-exam/spider-exam/walden.txt'
# with open(path,'r') as f:
#     lines = f.readlines()
#     for index,line in  enumerate(lines):
#         data ={
#                 'index':index,
#                 'line':line,
#                 'words':len(line.split())
#                }
#         #sheet_tab.insert_one(data)  #写入mongodb中

# for item in sheet_tab.find(): #查找数据库中所有的内容
#     print(item)

# for item in sheet_tab.find({'words':0}): #查找word值为0的内容，即line为0的
#     print(item)

# for item in sheet_tab.find(): #显示line的内容
#     print(item['line'])

# $lt/$let/$gt/$get/$e/$ne 依次是 </<=/>/>=/=/<>
for item in sheet_tab.find({'words':{'$lt':5}}): #显示line的内容
    print(item['line'])