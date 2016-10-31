#coding:utf-8 
import requests,urllib.request
from bs4 import BeautifulSoup

url = 'http://jandan.net/pic/page-217'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
          'Cookie':'LDID=9165D662D4613E79286601C0731DB446:FG=1; BAIDUID=BEB94DB46FCDCB89606811E49DA19F29:FG=1; CPROID=BEB94DB46FCDCB89606811E49DA19F29:FG=1; BIDUPSID=BEB94DB46FCDCB89606811E49DA19F29; PSTM=1477557429; BDUSS=lKYm1CZG1Vdi0ybU9Md2YySFVGY0s4ZS1wM2xUeTRMUE51Ym02SG9JMXRLanBZSVFBQUFBJCQAAAAAAAAAAAEAAABh~q5Uy67B6WJhYnlnaXJsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG2dElhtnRJYSG; cflag=15%3A3; FCID=BEB94DB46FCDCB89606811E49DA19F29:FG=1'
        }
source_code = requests.get(url,headers=header) #get html
#print(source_code) #状态码200 success, 403 fail
plain_text = source_code.text
#print(plain_text)

Soup = BeautifulSoup(plain_text)

download_links = []
floder_path = '/python3-exam/pachong/spider-exam/pics/'
for pic_tag in Soup.find_all('img'):
    #print(pic_tag)
    pic_link = pic_tag.get('src')
    print(pic_link)
    download_links.append(pic_link)
    
    
for item in download_links:
    urllib.request.urlretrieve(item,floder_path+item[-10:]) #下载图片，并将下载图片重新命名，命名规则是截取后10个字符串
    print('Done')




