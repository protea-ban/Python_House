def crypt(source, key):
    from itertools import cycle
    # ord函数返回一个字符的Unicode编码
    # chr函数返回一个Unicode编码对应的字符
    func = lambda x, y: chr(ord(x)^ord(y))
    # cylce函数在这用来自适应文本长度
    return ''.join(map(func, source, cycle(key)))

source = 'Beautiful is better than ugly'
key = 'Python'

print('Before Encypted:' + source)
encrypted = crypt(source, key)
print('After Encrypted:' + encrypted)
decrypted = crypt(encrypted, key)
print('After Decrypted:' + decrypted)
