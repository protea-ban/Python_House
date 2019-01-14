#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: 人名问题.py 
@time: 2018/05/12
"""  
'''
以固定格式给出一系列名字:[ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]，要求以“Bart, Lisa & Maggi”的格式输出:
*如果只有两个名字，则以“Lisa & Maggi”的格式输出
*如果只有一个名字，则以“Maggi”的格式输出
*如果给出的名字列表为空，则返回空值('')
'''
def namelist(names):
    nums = len(names)
    if nums == 0:
        return ''
    elif nums == 1:
        return (names[0]['name'])
    elif nums == 2:
        return (names[0]['name'] + ' & ' + names[1]['name'])
    else:
        name_last = names[-2]['name'] + ' & ' + names[-1]['name']
        name_li = ''
        for i in range(nums - 2):
            name_li = name_li + names[i]['name'] + ', '
        name_li += name_last
        return name_li

def namelist2(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''


if __name__ == '__main__':
    names = [{'name':'Bart'},{'name':'Lisa'},{'name':'Maggie'}]
    res = namelist2(names)
    print(res)