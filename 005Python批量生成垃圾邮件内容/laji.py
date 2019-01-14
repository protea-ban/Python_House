#!/usr/bin/u/ubv/a python
# -*- coding:utf-8 -*-

from random import choice, randrange

names = ('张三', '李四', '王五', '赵六', '周七', '刘八')
words = ('发票', '加我微信', '垃圾邮件', '广告', '联系方式')
textCharacters = '''
你卡号是打工后购买是拿了健康好噶地方卡拉涉及到覅发动机了卡经历过尿热火感恩高多功能卡看你没打过那地方了看偶然和工期华容曲蔚然的叫法文化了客人可能是绝对是发泡没有坏燃气管了思考对方哈维我偶尔会光谱噢那三大盒价位高回复精选库存高的合格了开放型的客人恭喜啊对此事东方银座哦啊了固特异是结构性都没我想干戈破甲弓发大水天气我很骄傲该地块很拉风的是偶发大水口理发店时空裂缝多撒谎范德萨我聊天佛为儿童观爱打架是否请问而且阿斯顿发收款打发士大夫撒地方撒旦法斯柯达福建安徽是那就是大黄蜂东方丽景阿克苏的房间爱上了沪电股份发动机奥斯卡了对方发生的认同服务器儿童额问题完全而已玩儿有问题偶的法师大神
'''

for i in range(30):
    with open(str(i)+'.txt', 'w', encoding='utf8') as fp:
        fp.write('亲爱的【' + choice(names) + '】：\n')
        # 生成随机邮件内容
        text = ''.join(choice(textCharacters) for _ in range(randrange(200, 500)))
        # 随机插入一些垃圾邮件中经常出现的词
        for i in range(randrange(len(words))):
            position = randrange(len(text))
            text = text[:position] + choice(words) + text[position:]
        # 写入文件
        fp.write(text)
        fp.write('\n\n\n我是。。。')
