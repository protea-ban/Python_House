#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
"""
@file: Python生成器函数案例一则：理财收益计算.py 
@time: 2018/05/11
"""  
def balance(base, rate):
    while True:
        base += base*rate
        yield base

base = 10
rate = 0.02

for year, current in enumerate(balance(base, rate), start=1):
    if current > 2*base:
        print(year, current)
        break