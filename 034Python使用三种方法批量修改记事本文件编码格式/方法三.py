#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
"""
@file: 方法三.py 
@time: 2018/06/15
@software: PyCharm  
"""  
from os import listdir
from chardet import detect

fns = (fn for fn in listdir() if fn.endswith('.txt'))

for fn in fns:
    with open(fn, 'rb+') as fp:
        content = fp.read()
        # 判断编码格式
        #=> 获取编码格式
        encoding = detect(content)['encoding']
        # 格式转换
        #=> 将文件内容先按自身编码格式解码后，再以UTF8编码
        content = content.decode(encoding).encode('utf8')
        # 写回文件
        fp.seek(0)
        fp.write(content)