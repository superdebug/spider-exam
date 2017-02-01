from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
#executable_path为你的phantomjs可执行文件路径
driver.get("http://www.toutiao.com")
data = driver.page_source
driver.quit

soup = BeautifulSoup(data)
#或得js变量的值
#r = driver.execute_script("return newsJason")
print (soup)
#参考网址 http://blog.csdn.net/pushiqiang/article/details/51290509
'''
pip install selenium
wget http://npm.taobao.org/mirrors/phantomjs/phantomjs-2.1.1-linux-x86_64.tar.bz2
tar -jxvf phantomjs-2.1.1-linux-x86_64.tar.bz2 
cd phantomjs-2.1.1-linux-x86_64/bin
mv phantomjs /usr/local/bin/phantomjs
'''
#可以参考
'''
ttp://p3.pstatp.com/large/1191000bdd08ed235a6d"/> </a> </div> </div> </li><li ad_id="" ad_track="" class="item " ga_event="article_item_click" qihu_ad_id=""> <span id="ad_extra" style="display:none;"></span> <div class="item-inner y-box"> <div class="normal rbox "> <div class="rbox-inner"> <div class="title-box" ga_event="article_title_click"> <a class="link title" href="/group/6382004858555810050/" target="_blank"> 绝不寻常！特朗普首次打破惯例，没给华人拜年 </a> </div> <div class="y-box footer"> <div class="y-left"> <a class="lbtn tag tag-bg-other" ga_event="article_tag_click" href="news_world" target="_blank">国际</a> <div class="y-left"> <a class="lbtn media-avatar" ga_event="article_avatar_click" href="/m5954781019/" target="_blank"> <img alt="" src="http://p1.pstatp.com/large/4d00054b126ceaf920"/> </a> <a class="lbtn source" ga_event="article_name_click" href="/m5954781019/" target="_blank"> 环球网 ⋅</a> <a class="lbtn comment" ga_event="article_comment_click" href="/group/6382004858555810050//#comment_area" target="_blank"> 评论 ⋅</a> </div> <span class="lbtn"> 30分钟前</span> </div> <div class="y-right"> <span class="dislike" data-groupid="6382004858555810050" ga_event="article_dislike_click"> 不感兴趣 <i class="y-icon icon-dislikenewfeed"></i> </span> </div> </div> </div> </div> <div class="lbox" ga_event="article_img_click"> <a class="img-wrap" href="/group/6382004858555810050/" target="_blank"> <img alt="" src="http://p3.pstatp.com/list/190x124/15df001097566f851555"/> </a> </div> </div> </li><li ad_id="" ad_track="" class="item " ga_event="video_item_click" qihu_ad_id=""> <span id="ad_extra" style="display:none;"></span> <div class="item-inner y-box"> <div class="normal rbox "> <div class="rbox-inner"> <div class="title-box" ga_event="video_title_click"> <a class="link title" href="/group/6381806206944952578/" target="_blank"> 亚洲第一巨人身高2.42米，将27岁袖珍人放在手掌上 </a> 
'''

