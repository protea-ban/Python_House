#!/usr/bin/u/ubv/a python
# -*- coding:utf-8 -*-

from random import randrange

def checkLucky1(num):
    '''
    递归法
    :param num:
    :return:
    '''
    if num == 0:
        return False
    quoient, lastDigit = divmod(num, 10)
    if lastDigit == 8:
        return True
    return checkLucky1(quoient)

def checkLucky2(num):
    return '8' in str(num)

#使用大量随机数测试两个函数
for i in range(100000):
    num = randrange(10**80)
    if checkLucky1(num) != checkLucky2(num):
        print(num)