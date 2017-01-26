#coding:utf8
import zipfile
import pymysql
import os
import sys
#python2.7版本下运行


#定义压缩包文件名及路径
zip_file='/opt/spider-exam/scrapy/alidata/receive/d1000/d1000_sp_posts.zip'

#定义解压后文件名及路径
unzip_file='/opt/spider-exam/scrapy/alidata/receive/d1000/d1000_sp_posts.sql'

#判断压缩包是否存在 如果文件不存在，则终止程序运行
if os.path.exists(zip_file):
    print ("zip文件存在")
else:
    print("zip文件不存在")
    sys.exit(0)

#解压缩文件
file_zip = zipfile.ZipFile(zip_file, 'r')
for file in file_zip.namelist():
    file_zip.extract(file, r'.')
file_zip.close()


#打开sql文本文件
file = open(unzip_file)
file.read(2)#先读取2个字符

s=file.read(2)
catalog=s.replace(' ','') #去除多余空格
print('栏目id是:'+catalog)

#数据库连接配置 正式库运行在阿里云的服务器上
conn=pymysql.connect(host="127.0.0.1",user="root",passwd="123456",db="spiderdb",charset="utf8")
cursor = conn.cursor()
sql = ''

lines = file.readlines()
for line in lines:
    #print line
    sql=sql+line

cursor.execute(sql)
conn.close()

#比较并插入表sp_term_relationships数据 未完成
#select id from sp_posts where id not in (select tid from sp_term_relationships);

#删除压缩文件及sql文本文件
os.remove(zip_file)
os.remove(unzip_file)
