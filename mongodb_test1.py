import pymongo

client = pymongo.MongoClient('localhost',27017)
walden = client['walden']
sheet_lines = walden['sheet_lines']

path = '/python3-exam/spider-exam/walden.txt'
with open(path,'r') as f:
    lines = f.readlines()
    for index,line in  enumerate(lines):
        data ={
                'index':index,
                'line':line,
                'words':len(line.split())
               }
        print(data)
