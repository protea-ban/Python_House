#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: Python内置函数sorted()和列表方法sort()的排序原理.py 
@time: 2018/04/13
"""  

from random import randrange, shuffle

class Country:
    # 构造函数，初始化对象
    def __init__(self, name, area):
        self.__setName(name)
        self.__setArea(area)

    def __setName(self, name):
        assert isinstance(name, str), '国家名称必须是字符串'
        self.__name = name

    def __setArea(self, area):
        assert isinstance(area, int), '面积必须是整数'
        self.__area = area

    # 返回国家名称
    def getName(self):
        return self.__name

    def getArea(self):
        return self.__area

    # 支持<运算符
    def __lt__(self, otherCountry):
        return self.__area < otherCountry.__area

    def __str__(self):
        return str((self.__name, self.__area))

# 创建国家对象并添加至列表
countries = []
countryNames = list('abcdefghij')
shuffle(countryNames)#  这个shuffle是干嘛用的
for name in countryNames:
    country = Country(name, randrange(10**2, 10**5))
    countries.append(country)

# 输出原始数据，不做任何排序
print('原始数据'.center(20, '='))
for country in countries:
    print(country)

# 使用内置函数sorted()函数排序，默认调用对象的__lt__()方法
print('默认函数'.center(20, '='))
for country in sorted(countries):
    print(country)

# 按国家名字进行排序，自定义排序规则
print('按国家名字排序'.center(20, '='))
for country in sorted(countries, key=lambda c:c.getName()):
    print(country)

# 按国家面积进行排序，自定义排序规则
print('按国家面积排序'.center(20, '='))
for country in sorted(countries, key=lambda c:c.getArea()):
    print(country)