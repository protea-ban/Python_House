"""
下面的代码实现任意进制的按权展开式，把指定数字按指定进制转换为十进制数。代码主要演示嵌套函数定义增强reduce()函数功能的思路，如果仅仅是为了进制转换，完全可以直接使用int()函数。
"""

from functools import reduce

def myReduce(num, c):
    num = str(num)
    if not all(map(lambda i:0<=int(i)<c, num)):
        return 'Error'

    def func(x, y):
        return x*c + y

    return reduce(func, map(int, num))


if __name__ == '__main__':
    print(myReduce(111, 2))
