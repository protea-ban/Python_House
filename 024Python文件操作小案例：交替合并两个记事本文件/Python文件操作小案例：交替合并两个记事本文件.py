#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: Python文件操作小案例：交替合并两个记事本文件.py 
@time: 2018/05/17
"""
'''
编写程序，接收两个记事本文件名字，然后交替把两个记事本文件中的行合并到result.txt文件中，
你一行来我一行，最后把行数较多的文件剩余内容全部写入目标文件。
'''
import sys
from os.path import isfile

txtFiles = sys.argv[1:]  # 这样的程序要在命令提示符环境执行
if len(txtFiles) != 2:
    print('请输入两个记事本文件。')
    sys.exit()
# 确保输入了两个记事本文件名
if all(map(lambda fn:isfile(fn) and fn.endswith('.txt'), txtFiles)):
    with open('result.txt', 'w') as fp:
        with open(txtFiles[0]) as fp1, open(txtFiles[1]) as fp2:
            while True:
                # 交替读取两个文件中的行，并标记哪个文件先结束
                line1 = fp1.readline()
                if line1:
                    fp.write(line1)
                else:
                    flag = False
                    break
                line2 = fp2.readline()
                if line2:
                    fp.write(line2)
                else:
                    flag = True
                    break
            fp3 = fp1 if flag else fp2  # 让fp3表示还有内容没读完的文件
            for line in fp3:    # 把剩余内容全部写入目标文件
                fp.write(fp3.readline())
else:
    print('请输入两个记事本文件。')
