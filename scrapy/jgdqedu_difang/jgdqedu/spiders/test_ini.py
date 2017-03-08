#!/usr/bin/env python3
#coding:utf-8
import  configparser 
config =  configparser.ConfigParser()
config.read('/opt/spider-exam/scrapy/jgdqedu/config.ini')

x=config.get("jgdqedu","content")
print (x)
