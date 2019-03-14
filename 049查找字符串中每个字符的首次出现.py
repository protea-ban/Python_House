"""
查找字符串中每个字符的首次出现。给定一个任意字符串，要求得到一个新字符串，重复字符只保留一个，并且新字符串中的字符保持在原字符串中首次出现的先后顺序。例如，abcdaaabe处理后应得到abcde。
"""

from re import findall
from random import choice
from string import digits

def func1(text):
    # 转成集合，去重
    result = set(text)
    result = ''.join(sorted(result, key=lambda ch:text.index(ch)))
    return result

def func2(text):
    result = []
    for ch in text:
        if ch not in result:
            result.append(ch)

    return ''.join(result)


def func3(text):
    return ''.join(findall(r'(\w)(?!.*\1)', text[::-1][::-1]))


if __name__ == '__main__':
    text = ''.join(choice(digits) for _ in range(30))
    print(text)
    print(func1(text))
    print(func2(text))
    print(func3(text))
