from random import choice, randrange

lst = [(str(randrange(3)), ''.join(choice('abcdefg') for _ in range(5))) for _ in range(5)]
print(lst)
lst.sort(key=lambda item: (item[0], tuple(map(lambda x: -ord(x), item[1]))))
print(lst)
