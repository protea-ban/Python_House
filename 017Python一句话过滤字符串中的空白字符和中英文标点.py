#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: Python一句话过滤字符串中的空白字符和中英文标点.py 
@time: 2018/05/09
"""  
from random import choice
from jieba import cut

def delPuncs(s):
    return ''.join(filter(lambda word: len(word)>1, cut(s)))

if __name__ == '__main__':
    text = '''
    东边来个小朋友叫小松，手里拿着一捆葱。
    西边来个小朋友叫小丛，手里拿着小闹钟。
    小松手里葱捆得松，掉在地上一些葱。
    小丛忙放闹钟去拾葱，帮助小松捆紧葱。
    小松夸小丛像雷锋，小丛说小松爱劳动。
    '''
    print(delPuncs(text))