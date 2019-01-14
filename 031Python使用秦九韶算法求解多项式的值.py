#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
"""
@file: Python使用秦九韶算法求解多项式的值.py 
@time: 2018/06/14
@software: PyCharm  
"""  
def func(factors, x):
    result = factors[0]
    for factor in factors[1:]:
        result += result*x + factor
    return result