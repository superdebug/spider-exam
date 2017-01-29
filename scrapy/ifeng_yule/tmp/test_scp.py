import paramiko
import os
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
except Exception as e:
    print('upload exception:',e)

sf.close()
