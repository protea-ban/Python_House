#!/usr/bin/u/ubv/a python
# -*- coding:utf-8 -*-

def isPalindrome1(text):
    '''
    循环，首尾检查
    :param text:
    :return:
    '''
    length = len(text)
    for i in range(length//2+1):
        if text[i] != text[-1-i]:
            return False

    return True

def isPalindrome2(text):
    '''
    递归，效率略低
    :param text:
    :return:
    '''
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False

    return isPalindrome2(text[1:-1])

def isPalindrome3(text, start=None, end=None):
    if start == None or end == None:
        start = 0
        end = len(text) - 1

    if start >= end:
        return True

    if text[start] != text[end]:
        return False

    return isPalindrome3(text, start+1, end-1)

sentences = ('deed', 'dad', 'need', 'rotor', 'civic', 'redivider', 'noon', 'his', 'difference', 'a')

for sentence in sentences:
    print(sentence)
    for func in (isPalindrome1, isPalindrome2, isPalindrome3):
        print('\t', func(sentence))