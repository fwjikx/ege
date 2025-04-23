def f(n):
    stra = ''
    while n > 0:
        stra += str(n % 3)
        n //= 3
    return stra[::-1]


a = 9 ** 18 + 3 ** 54 - 9
n3 = f(a)
print(n3.count('2'))
