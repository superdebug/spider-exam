import re 
'''   
html = """ 
  <h2>多云</h2> 
"""
   
if __name__ == '__main__': 
  p = re.compile('<[^>]+>') 
  print (p.sub("", html))
'''
#Python通过正则表达式取html中温度信息代码示例:
#!/usr/bin/env python 
#-*- coding: utf8 -*- 
import re 
   
html = """ 
  <div class="w-number"> <span class="tpte">14℃</span> </div> 
"""
   
if __name__ == '__main__': 
  p = re.compile('<[^>]+>') 
  print (p.sub("", html))

