import urllib.request
url = "http://quote.stockstar.com/stock"  #打算抓取内容的网页
proxy_ip={'http': '139.199.198.71:1080',
        'http': '111.185.163.44:8888'

        }  #想验证的代理IP
proxy_support = urllib.request.ProxyHandler(proxy_ip)
opener = urllib.request.build_opener(proxy_support)
opener.addheaders=[("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64)")]
urllib.request.install_opener(opener)
print(urllib.request.urlopen(url).read())
