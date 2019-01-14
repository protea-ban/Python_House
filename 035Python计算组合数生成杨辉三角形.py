#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: Python计算组合数生成杨辉三角形.py 
@time: 2019/01/13
@software: PyCharm  
"""  
from functools import lru_cache

# 修饰器lru_cache的作用是给函数cni增加缓存，
# 减少重复计算，从而提高运行速度。
@lru_cache(maxsize=64)
def cni(n, i):
    if n == i or i == 0:
        return 1
    return cni(n-1, i) + cni(n-1, i-1)


def yanghui(num):
    for n in range(num):
        for i in range(n+1):
            # str 有格式化功能
            print(str(cni(n, i)).ljust(4), end=' ')

        print()


if __name__ == '__main__':
    yanghui(8)
