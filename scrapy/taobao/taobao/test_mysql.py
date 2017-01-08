import pymysql
conn=pymysql.connect(host="127.0.0.1",user="root",passwd="123456",db="csdn",charset="utf8")
cursor = conn.cursor()
sql="insert into taob(title,link,price,comment) values('kisses好时之吻水滴牛奶巧克力500g约100个结婚庆喜糖果零食年货','https://item.taobao.com/item.htm?id=537731017941','45.00','1')"
cursor.execute(sql)
conn.commit()
