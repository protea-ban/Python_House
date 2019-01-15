"""
研究发现，男人在候车厅之类的场合选择长椅上的座位休息时，
一般倾向于选择最长空座位串的中间位置。
"""

# 列表方法
def arrangeOrderOne(n):
    seats = [0] * n

    for _ in range(n):
        span = (0, 0)
        for pos in range(n):
            if seats[pos] == 0 and (pos == 0 or seats[pos-1] == 1):
                start = pos
            elif seats[pos] == 1 and seats[pos-1] == 0 and pos-start>span[1]-span[0]:
                span = (start, pos-1)

        if seats[pos] == 0 and pos-start>=span[1]-span[0]:
            span = (start, pos)

        seats[(span[1]+span[0]) // 2] =1
        print(''.join(map(str, seats)).translate(''.maketrans('01', '_x')))


def arrangeOrderTwo(n):
    import re
    seats = '_' * n
    for _ in range(n):
        # 将seats字符串截取为'_'的字符串，取其中最长的那个
        t = max(re.findall('_+', seats), key=len)
        # 取上述t的中间点，占座
        index = seats.index(t) + len(t) // 2
        seats = seats[:index] + 'x' + seats[index+1:]
        print(seats)


if __name__ == "__main__":
    arrangeOrderTwo(18)
