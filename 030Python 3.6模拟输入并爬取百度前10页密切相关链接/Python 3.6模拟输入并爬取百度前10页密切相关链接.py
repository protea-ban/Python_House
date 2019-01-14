#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
"""
@file: Python 3.6模拟输入并爬取百度前10页密切相关链接
@time: 2018/06/09
@software: PyCharm  
"""  
import mechanicalsoup

# python小屋文章清单
with open('list.txt', encoding="utf8") as fp:
    articles = fp.readlines()
#=> 使用map函数，去掉从文本当中读取时的字符，并放入元组中
articles = tuple(map(str.strip, articles))

# 模拟打开指定网址，模拟输入并提交输入的关键字
browser = mechanicalsoup.StatefulBrowser()  #=> 新建一个对象
browser.open(r'http://www.baidu.com')#=> 模拟打开百度
browser.select_form("#form")#=> 根据class指定一个表单
browser['wd'] = 'Python小屋'#=> 根据表单的id指定表单中输入的内容
browser.submit_selected()#=> 提交，模拟搜索

# 获取百度前十页
top10Urls = []
#=> get_current_page得到本页网页，得到a标签对象
for link in browser.get_current_page().select('a'):
    if link.text in tuple(map(str, range(2, 11))):
        #=> link.attrs['href] a标签中的属性得到值
        top10Urls.append(r'http://www.baidu.com'+ link.attrs['href'])

# 与微信公众号里的文章标题进行比对，如果非常相似就返回True
def check(text):
    for article in articles:
        # 使用切片，防止网站转发公众号文章时标题不完整
        if article[2:-2].lower() in text.lower():
            return True
    return False

# 只输出密切相关的链接
def getLinks():
    for link in browser.get_current_page().select('a'):
        text = link.text
        if 'Python小屋' in text or '董付国' in text or check(text):
            print(link.text, '-->', link.attrs['href'])

# 输出第一页
getLinks()
# 处理后面的9页
for url in top10Urls:
    browser.open(url)
    getLinks()