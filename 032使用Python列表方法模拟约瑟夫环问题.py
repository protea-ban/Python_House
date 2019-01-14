def demo(lst, k):
    # 复制列表，避免影响原来的数据
    t_lst = lst[:]

    while len(t_lst) > 1:
        print(t_lst)
        # 关于报数
        for i in range(k-1):
            t_lst.append(t_lst.pop(0))
        t_lst.pop(0)

    # 只剩最后一人，游戏结束
    return t_lst[0]


lst = list(range(1, 11))
print(demo(lst, 3))

