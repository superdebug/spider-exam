#!/bin/sh 
#适合CentOS
. ~/.bash_profile 

#适合ubunut
#. ~/.bashrc  
#export PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin
cd /opt/spider-exam/scrapy/jgdqedu_shehui
/usr/local/bin/scrapy crawl shehui --nolog

