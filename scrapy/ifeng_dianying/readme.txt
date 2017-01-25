凤凰娱乐-电影
http://ent.ifeng.com/listpage/6/1/list.shtml


计划任务
#每10分钟抓取一次凤凰娱乐电影栏目内容
*/10 * * * *  /opt/spider-exam/scrapy/ifeng_dianying/ifeng_dianying.sh


select title,catalog,create_time from news where catalog='电影';
