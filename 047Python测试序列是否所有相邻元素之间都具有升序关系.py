# 循环比较
def lessThan1(seq):
    for index, value in enumerate(seq[:-1]):
        if value >= seq[index+1]:
            return False

    return True


# 匿名函数比较
def lessThan2(seq):
    func = lambda x,y : x < y
    return all(map(func, seq[:-1], seq[1:]))

if __name__ == '__main__':
    test = ('abcdef', [1,2,3,5,4], [1,3,4,5])
    for item in test:
        print(lessThan1(item), lessThan2(item))
