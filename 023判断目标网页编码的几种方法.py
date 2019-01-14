#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: 判断目标网页编码的几种方法.py 
@time: 2018/05/16
"""  
from urllib.request import urlopen
from chardet import detect
from bs4 import BeautifulSoup

def checkEncoding1(url):
    # 通过头部获取编码信息
    fp = urlopen(url)
    try:
        header = fp.headers['content-type']
        index = header.rindex('charset=')
        return (1, header[index+8:])
    except:
        fp.close()

def checkEncoding2(url):
    # 通过网页参数获取编码格式
    with urlopen(url) as fp:
        try:
            charset = fp.info().get_param('charset')
            if charset:
                return (2, charset)
        except:
            pass

def checkEncoding3(url):
    # 通过扩展库chardet判断网页编码
    with urlopen(url) as fp:
        content = fp.read()
        try:
            return (3, detect(content)['encoding'])
        except:
            pass

def checkEncoding4(url):
    # 通过扩展库bs4判断网页编码
    with urlopen(url) as fp:
        content = fp.read()
        try:
            return (4, BeautifulSoup(content, 'lxml').original_encoding)
        except:
            pass

def checkEncoding5(url):
    with urlopen(url) as fp:
        content = fp.read().decode('latin_1')
        if 'encoding=' in content:
            index = content.index('encoding=')
            resContent = content[index+9:]
            return (5, resContent[:resContent.index('"')])
        elif 'charset=' in content:
            index = content.index("charset=")
            resContent = content[index+8:]
            return (5, resContent[:resContent.index('"')])


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    char = checkEncoding5(url)
    print(char)