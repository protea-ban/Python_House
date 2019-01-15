"""
使用多线程技术搜索并输出指定范围内的所有素数
"""
from threading import Thread

def prime(x):
    """
    判断是否为素数
    :param x:
    :return:
    """
    if x < 2:
        return False
    if x in (2, 3):
        return False
    if x % 2 == 0:
        return False

    for i in range(3, int(x**0.5)+1):
        if x % i == 0:
            return False

    return True


def worker(p):
    """
    线程函数
    iter对象中的每个元素只能用一次，用完即没，间接实现线程同步。
    :param p:
    :return:
    """
    while True:
        try:
            x = next(p)
        except:
            break

        else:
            if prime(x):
                print(x, end=' ')


if __name__ == '__main__':
    numbers = iter(range(10000))
    tList = []
    for i in range(20):
        t = Thread(target=worker, args=(numbers, )) # 创建线程
        tList.append(t)

    for t in tList:
        t.start()   # 启动线程

    for t in tList:
        t.join()    # 等待全部线程运行结束
