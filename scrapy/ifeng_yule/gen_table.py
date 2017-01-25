import pymysql
import datetime

#数据库连接配置
conn=pymysql.connect(host="127.0.0.1",user="root",passwd="123456",db="spiderdb",charset="utf8")
cursor = conn.cursor()

#定义生成的数据库文件路径及文件名
sql_file='/opt/spider-exam/scrapy/ifeng_yule/d1000_sp_posts.sql'
file_object = open(sql_file, 'w')
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
        sql_str="insert into sp_posts (post_author,post_keywords,post_date,post_title,post_content,post_excerpt,post_modified) values (1,'"+title+"','"+dt+"','"+title+"','"+content+"','"+title+"','"+dt+"');\n"
        file_object.writelines(sql_str)

except Exception as err:
    print(err)

conn.close()
file_object.close( )
