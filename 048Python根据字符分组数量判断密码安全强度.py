from itertools import groupby

def rules(ch):
    if '0' <= ch <= '9':
        return 'digits'
    if 'a' <= ch<= 'z':
        return 'lowercase'
    if 'A' <= ch<= 'Z':
        return 'uppercase'
    if ch in ',._':
        return 'pub'


def check(pwd):
    grade = {1:'weak', 2:'below middle', 3:'upper middle', 4:'strong'}
    num = len(tuple(groupby(pwd, key=rules)))
    return grade.get(num, 'no suite')


if __name__ == '__main__':
    pwd = 'fads123A,'
    print(check(pwd))
