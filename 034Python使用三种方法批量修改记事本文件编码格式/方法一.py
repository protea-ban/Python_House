#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: 方法一.py
@time: 2018/06/15
@software: PyCharm  
"""  
######方法一
import os

# 获取当前文件夹中所有记事本文件清单
fns = (fn for fn in os.listdir() if fn.endswith('.txt'))

for fn in fns:
    try:
        # 首先尝试使用UTF8编码打开并读取文件内容
        # 如果失败会抛出异常
        with open(fn, encoding="utf8") as fp:
            fp.read()
    except:
        # 以默认的GBK编码读取原文件内容
        # 以UTF8编码写入新文件
        with open(fn) as fp1:
            with open("t.txt", 'w', encoding="utf8") as fp2:
                fp2.write(fp1.read())
            # 删除原文件，把新文件重命名为原文件
            os.remove(fn)
            os.rename('t.txt', fn)