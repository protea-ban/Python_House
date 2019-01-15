"""

"""


from functools import reduce

def interset(x, y):
    return x & y

def union(x, y):
    return x | y


if __name__ == '__main__':
    sets = [{1, 2, 3, 4, 5}, {2, 5, 7}, {3, 2, 5, 8}]
    # 使用函数方式
    # result = reduce(interset, sets)
    # result = reduce(union, sets)

    # 使用labmda方式
    # result = reduce(lambda x, y: x & y, sets)
    result = reduce(lambda x, y: x | y, sets)
    print(result)
