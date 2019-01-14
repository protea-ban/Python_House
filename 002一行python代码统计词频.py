from collections import Counter
from string import punctuation
from jieba import cut

text = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

result = Counter(cut(text))# 分词后进行词频统计
f = lambda item : not(item[0].isspace() or item[0] in punctuation)
result = sorted(filter(f, result.items()), key = lambda item : item[1], reverse=True)

for item in result[:5]:
    print(item)
