from string import digits
from itertools import combinations

# Python标准库itertools中的combinations函数可以用来
# 返回从指定分布总体中任选k的元素的所有组合。
for item in combinations(digits, 4):
    times = 0
    while True:
        big = int(''.join(sorted(item, reverse=True)))
        little = int(''.join(sorted(item)))
        difference = big - little
        times += 1
        if difference == 6174:
            if times > 7:
                print(times)
            break
        else:
            item = str(difference)
