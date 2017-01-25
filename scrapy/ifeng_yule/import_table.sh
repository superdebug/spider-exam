#!/bin/sh 
. ~/.bash_profile
#export PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin
cd /opt/spider-exam/scrapy/ifeng_yule
/usr/bin/mysql -uroot -p123456 < tb_d1000.sql
