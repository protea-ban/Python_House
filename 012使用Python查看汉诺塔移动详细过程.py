#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: 使用Python查看汉诺塔移动详细过程.py 
@time: 2018/04/18
"""  
def hannoi(num, src, dst, temp=None):   #递归算法
    global times    #声明用来记录移动次数的变量为全局变量
    if num == 1: #只剩下最后一个或者只有一个盘子需要移动
        print('The {0} Times move:{1}==>{2}'.format(times, src, dst))
        towers[dst].append(towers[src].pop())
        for tower in 'ABC': #输入3根柱子上的盘子
            print(tower, ':', towers[tower])
        times += 1
    else:
        # 递归调用函数自身，先把除最后一个盘子之外的所有盘子移动到临时柱子上
        hannoi(num-1, src, temp, dst)
        hannoi(1, src, dst) # 把最后一个盘子直接移动到目标柱子上
        #把除最后一个盘子之外的其他盘子从临时柱子上移动到目标柱子上
        hannoi(num-1, temp, dst, src)

times = 1   #用来记录移动次数的变量
n = 3   #盘子数量
towers = {
    'A':list(range(n, 0, -1)),
    'B':[],
    'C':[]
}
#A表示最初放置盘子的柱子，C是目标柱子，B是临时柱子
hannoi(n, 'A', 'C', 'B')