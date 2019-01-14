#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
"""
@file: 矩形分割问题.py 
@time: 2018/05/12
"""  


'''
给出一个矩形，求该矩形最少能被分割成几个正方形，并以列表的格式返回各正方形的边长;如果给出的初始矩形本身就是正方形，则返回None。
'''
def sqInRect(a, b):
    if a == b:
        return None
    res = []
    while b:
        b, a = sorted([a, b])
        res += [b]
        a, b = b, a-b
    return res

if __name__ == '__main__':
    res = sqInRect(3, 3)
    print(res)