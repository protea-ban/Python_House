#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: Python监视电子邮箱并提示收到新邮件.py 
@time: 2018/06/03
@software: PyCharm  
"""  
import time
import datetime
from poplib import POP3_SSL

popServerAddress = 'pop.163.com'
emailAddress = input('请输入邮箱地址：')
pwd = input('请输入密码：')

lastNumber = 1

while True:
    # 建立连接
    server = POP3_SSL(popServerAddress, timeout=3)
    # 不显示与服务器之间的交互信息
    server.set_debuglevel(0)
    # 登录
    server.user(emailAddress)
    server.pass_(pwd)
    # 获取全部邮件的编号，mails的格式为['mesg_num octets',...]
    _, mails,_ = server.list()
    # 退出
    server.quit()
    # 获取最新邮件的ID
    newestNumber = int(mails[-1].split()[0])
    if newestNumber != lastNumber:
        print('{}--您有{}封邮件未读'.format(str(datetime.datetime.now())[:19],
                        newestNumber-lastNumber))
        lastNumber = newestNumber
    # 一分钟后重新检查
    time.sleep(60)


