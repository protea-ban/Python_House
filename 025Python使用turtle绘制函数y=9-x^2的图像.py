#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
"""
@file: Python使用turtle绘制函数y=9-x^2的图像.py 
@time: 2018/05/22
"""  
import turtle

turtle.setup(width=700, height=900) #设置绘图窗口大小
turtle.hideturtle() #隐藏笔尖形状
turtle.speed(6) # 设置绘图速度
turtle.Turtle().screen.delay()  # 取消屏幕延迟
turtle.color(1,0,0) #设置画笔颜色
turtle.up() # 抬起画笔，不绘图
turtle.goto(-300, -450) # 移动画笔
turtle.down()   # 落下画笔，开始绘图
for x in range(-300, 301):# 自变量x的取值范围
    y = (9 - (x*3/300)**2)*100 - 450# 计算函数值
    turtle.goto(x, y)   # 依次连接多个点，形成曲线
turtle.up() # 抬起画笔，结束绘图
turtle.mainloop()   # 启动事件主循环