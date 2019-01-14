#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: Python实现中英文混排时行号对齐.py 
@time: 2018/06/09
@software: PyCharm  
"""  
sentences = [
'Readability counts.',
'1900页Python系列PPT分享五：函数设计与应用',
'1900页Python系列PPT分享六：面向对象程序设计',
'1900页Python系列PPT分享七：文件操作',
'1900页Python系列PPT分享八：异常处理结构与程序调试、测试',
'报告PPT：基于Python语言的课程群建设探讨与实践'
]

longestSentence = max(sentences, key=lambda s:len(s.encode('gbk'))) # 最长一行的内容
maxLength = len(longestSentence.encode('gbk'))# 最长一行的长度
for index, sentence in enumerate(sentences):# 在GBK编码中，一个汉字占两个英文字符宽度
    print(sentence + ''*(maxLength - len(sentence.encode('gbk'))) + '#{}'.format(index))
