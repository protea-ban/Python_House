#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: Python字符串index()方法应用案例一则.py 
@time: 2018/05/09
"""  
text = '''
东边来个小朋友叫小松，手里拿着一捆葱。
西边来个小朋友叫小丛，手里拿着小闹钟。
小松手里葱捆得松，掉在地上一些葱。
小丛忙放闹钟去拾葱，帮助小松捆紧葱。
小松夸小丛像雷锋，小丛说小松爱劳动。
'''

for index, ch in enumerate(text):   
# 内置函数enumerate可对有序序列中的元素进行枚举，常用来获取元素下标
    if index == text.index(ch): #index方法返回指定字符串首次出现的位置
        print((index, ch), end='')