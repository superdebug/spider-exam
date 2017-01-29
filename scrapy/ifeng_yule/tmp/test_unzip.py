#coding:utf8
import zipfile
zfile = zipfile.ZipFile('d1000_sp_posts.zip','r')
for filename in zfile.namelist():
    data = zfile.read(filename)
    file = open(filename, 'w+b')
    file.write(data)
    file.close()
