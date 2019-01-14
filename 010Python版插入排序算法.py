#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: Python版插入排序算法.py 
@time: 2018/04/13
"""  

from random import randrange

def selectionSort(values):
    # 切片，不影响原来的列表
    values = values[:]
    length = len(values)
    # 处理第i个元素
    for i in range(1, length):
        value = values[i]
        j = i - 1
        # 为第i个元素寻找合适的插入位置
        while j >= 0 and values[j] > value:
            values[j+1] = values[j]
            j -= 1
        # 把第i个元素插入到合适的位置
        values[j+1] = value
    # 返回排序后的新列表
    return values

for _ in range(1000000):
    values = [randrange(1, 1000) for _ in range(20)]
    if sorted(values) != selectionSort(values):
        print(values)