#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: 单词非两端字符改为小写.py 
@time: 2018/05/12
"""  
import re
def check(s):
    return re.sub(r'\b(\w)(\w+)(\w)\b',
                  lambda x:x.group(1)+x.group(2).lower()+x.group(3),
                  s
                  )

if __name__ == '__main__':
    print(check('abc ABBC'))