#coding:utf8
#压缩包文件名及路径定义
zip_file=''
#解压后文件名及路径定义
unzip_file='/opt/spider-exam/scrapy/ifeng_yule/tmp/file1.txt'


file = open(unzip_file)
file.read(2)#先读取2个字符

s=file.read(2)
catalog=s.replace(' ','') #去除多余空格
print(s)
print(catalog)
