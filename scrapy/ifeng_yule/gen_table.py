#!/usr/bin/env python
#coding:utf-8
import pymysql
import datetime
import os
import sys
import zipfile
import paramiko

#程序目录
BASE_PATH = '/opt/spider-exam/scrapy/ifeng_yule/'
#生成的数据文件名
SQL_FILE = 'd1000_sp_posts.sql'
#日志路径
LOG_PATH='/opt/log/'
#日志文件
LOG_FILE = 'd1000.log'

#定义日志文件信息并以追加模式记录日志
LOG_PATH_FILE= LOG_PATH+LOG_FILE 
file_log = open(LOG_PATH_FILE, 'a')

#进入程序目录
os.chdir(BASE_PATH)

#检查是否可以访问目标网站
'''
return1=os.system('ping www.d1000.net -c 2')
if return1:
    print ('ping fail')
    file_log.writelines('连接网络失败---'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n') 
    sys.exit(0)
'''
file_log.writelines('连接网络成功---'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')

#数据库连接配置
conn=pymysql.connect(host="127.0.0.1",user="root",passwd="123456",db="spiderdb",charset="utf8")
cursor = conn.cursor()

#定义生成的数据库文件路径及文件名
LAST_SQL_FILE = BASE_PATH+SQL_FILE
file_object = open(LAST_SQL_FILE, 'w')

#娱乐栏目的id是15
file_object.writelines('##15\n')
file_object.writelines('use d1000db;\n')
file_object.writelines('set names utf8;\n')

try:
    #按时间排序 抽选出5条记录
    sql="select url,title,desc_text,content from news where url not in (select url from tb_d1000) order by create_time limit 0,5;"
    cursor.execute(sql)
    row=cursor.fetchall()
    for i in range(len(row)):
        url = row[i][0]
        title = row[i][1]
        desc_text = row[i][2]
        content = row[i][3]
        dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_sp_posts="insert into sp_posts (post_author,post_keywords,post_date,post_title,post_content,post_excerpt,post_modified,post_hits) values (1,'"+title+"','"+dt+"','"+title+"','"+content+"','"+title+"','"+dt+"',1);\n"
        file_object.writelines(sql_sp_posts)
        file_log.writelines('写入数据---'+title+'---'+url+'---'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
except Exception as err:
    print(err)
    file_log.writelines('写入数据库失败---'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
conn.close()
file_object.close( )

print('数据生成完毕!')
file_log.writelines('数据生成完毕---'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')

#压缩sql文件为zip格式
zip_file =zipfile.ZipFile('d1000_sp_posts.zip','w',zipfile.ZIP_DEFLATED)
zip_file.write(SQL_FILE)
zip_file.close;
file_log.writelines('压缩数据完成---'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')

#复制压缩sql的zip文件到服务器端
rhost = '10.1.101.202'#主机
rport = 22 #端口
rusername = 'yc' #用户名
rpassword = '123456' #密码
local_file = '/opt/spider-exam/scrapy/ifeng_yule/d1000_sp_posts.zip'#本地文件或目录
remote_path = '/alidata/receive/d1000/' #远程文件或目录
remote_file = 'd1000_sp_posts.zip' #远程文件或目录
sf = paramiko.Transport((rhost,rport))
sf.connect(username=rusername,password=rpassword)
sftp = paramiko.SFTPClient.from_transport(sf)
try:
    #判断本地文件及远程目录是否存在
    if (os.path.isfile(local_file) and sftp.stat(remote_path)):
        sftp.put(local_file,remote_path+remote_file)#上传文件
        print('文件上传完成!')
        file_log.writelines('上传至服务器成功---'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
except Exception as e:
    file_log.writelines('上传至服务器成功---'+e+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
    print('upload exception:',e)
sf.close()

#更新数据库中对应的本地网站表
conn=pymysql.connect(host="127.0.0.1",user="root",passwd="123456",db="spiderdb",charset="utf8")
cursor = conn.cursor()
for i in range(len(row)):
    try:
        #将发送服务器的数据更新到本地网站表内
        sql="insert into tb_d1000 values ('"+row[i][0]+"','"+row[i][1]+"');"
        cursor.execute(sql)
        conn.commit
        file_log.writelines('数据写入表成功---'+sql+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
    except Exception as err:
        print('错误信息如下')
        print(err)
        file_log.writelines('数据写入本地表tb_d1000失败---'+err+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
#关闭日志文件
file_log.close()
file_object.close()

#删除生成的sql文件及zip文件
os.remove('d1000_sp_posts.sql')
#os.remove('d1000_sp_posts.zip')
