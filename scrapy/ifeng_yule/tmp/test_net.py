#!/usr/bin/env python
#coding:utf-8
 
import os
 
return1=os.system('ping www.d1000.net -c 2')
if return1:
    print 'ping fail'
else:
    print 'ping ok'
