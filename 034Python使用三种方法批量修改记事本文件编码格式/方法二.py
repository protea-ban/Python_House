#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: 方法二.py 
@time: 2018/06/15
@software: PyCharm  
"""  
from os import listdir

fns = (fn for fn in listdir() if fn.endswith('.txt'))

for fn in fns:
    #=> 用字节方式打开文件
    with open(fn, 'rb+') as fp:
        content = fp.read()
        try:
            # 尝试使用UTF8解码
            content.decode('utf8')
        except:
            # 使用GBK解码后再使用UTF8编码，写回文件
            content = content.decode('gbk').encode('utf8')
            #=> 回溯到文件开始地方
            fp.seek(0)
            fp.write(content)