

def digitSum1(n):
    ''' 函数式编程 '''
    return sum(map(int, str(n)))

def digitSum2(n):
    ''' 递归 '''
    if n == 0:
        return 0

    # 先计算除最后一位的其他位之和
    # 再加上最后一位
    return digitSum2(n // 10) + n % 10


if __name__ == "__main__":
    # 测试 程序运行无任何输出，表示两个函数结果一致。
    from random import randrange
    for _ in range(100000):
        n = randrange(1e20)
        if digitSum1(n) != digitSum2(n):
            print(n)
