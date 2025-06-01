#cпособ 1 - на слабых компах не потянет
from sys import *
setrecursionlimit(1000000)

def f(n):
    if n < 5:
        return n
    if n >= 5:
        return 2 * n * f(n - 4)

print((f(13766) - 9 * f(13762)) // f(13758))

#2 способ - кэшируем результаты
from functools import *
@lru_cache(10000) - "None лучше не ставить"

def f(n):
    if n < 5:
        return n
    if n >= 5:
        return 2 * n * f(n - 4)

for i in range(14000): #заполняем кэш
    f(i)

print((f(13766) - 9 * f(13762)) // f(13758))

#3 способ - мемоизация через список
f = [0] * 14000
for n in range(len(f)):
    if n < 5:
        f[n] = n
    if n >= 5:
        f[n] = 2 * n * f[n - 4]
print((f[13766]- 9 * f[13762]) // f[13758])
