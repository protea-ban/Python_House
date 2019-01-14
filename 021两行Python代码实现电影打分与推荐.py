#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
"""
@file: 两行Python代码实现电影打分与推荐.py 
@time: 2018/05/12
"""  
from random import randrange

# 历史观影数据
data = {
    'user'+str(i):{
        'film'+str(randrange(1, 15)):randrange(1, 6) for _ in range(randrange(3, 10))
    }
    for i in range(10)
}
# 用户观影数据
user = {'film'+str(randrange(1, 15)):randrange(1, 6) for _ in range(5)}
# 最相似的用户及其对电影打分情况
# 两个用户共同打分的电影最多
# 并且所有电影打分差值的平方和最小
similarUser, films = min(data.items(),
                         key=lambda item:(-len(item[1].keys()&user),
                                          sum(((item[1].get(film)-user.get(film))**2
                                               for film in user.keys()&item[1].keys()
                                               ))))

print('know data'.center(50, '='))
for item in data.items():
    print(len(item[1].keys()&user.keys()),
          sum(((item[1].get(film)-user.get(film))**2
               for film in user.keys()&item[1].keys())),
          item,
          sep=':')

print('current user'.center(50, '='))
print(user)
print('most similar user and his films'.center(50, '='))
print(similarUser, films, sep=':')
print('recommended film'.center(50, '='))
# 在当前用户没看过的电影中选择打分最高的进行推荐
print(max(films.keys()-user.keys(), key=lambda film:films[film]))









