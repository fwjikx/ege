#Функция для перевода числа в любую систему счисления:
def my_convert(number: int, system: int) -> str:
    alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    result = ''
    while number > 0:
        result += alphabet[number % system]
        number //= system
    return result[::-1]

#определить кол-во цифр больше 9 в 27 сс
a = 3 * 5103 **2020 + 3 * 729 ** 2021 - 2 * 343 ** 2022 + 27 ** 2023- 4 * 7 ** 2024 - 2029
k = 0
while a > 0:
    if a % 27 > 9:
        k+=1
    a = a // 27
print(k)

#alphabet можно собрать другим способом:
from string import *
alphabet = digits + ascii_uppercase

#❗️Шаблон для первого типа:
x = тут ваше выражение
base = система счисления
n = число поиска
M = []
while x > 0:
    M.append(x % base)
    x //= base
M.reverse()
print(M.count(т))

#❗️Шаблон для второго типа:
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
base = ваша система счисления
M = []
for x in alphabet[:base]:
    A = int(f'1{x}51', base)
    B = int(f'3{x}2', base)
    if (A - B) % 4 == 0:  # тут поменять выражение
        M.append((A - B) // 4)
print(max(M))

alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
M = []
for x in alphabet[:8]:
    for y in alphabet[:8]:
        A = int(f'{x}01{y}4', 9)
        B = int(f'{x}{y}544', 8)
        if (A + B) % 89 == 0:
            M.append((A + B) // 89)
print(min(M))

alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for p in range(10, 36 + 1):
    for x in alphabet[:p]:
        for y in alphabet[:p]:
            if int(f'24{x}9', p) + int(f'{y}{x}{y}3', p) == int(f'{x}4{y}0', p):
                print(int(x + y + y, p))

#если не знаете алфавит системы СС то делаем как кодом ниже
for x in range(100):
    a =3 * 100 ** 0 + 2 * 100 ** 1 + 1 * 100 ** 2 + 0 * 100 ** 3 + x * 100 ** 4 + 10 * 100 ** 5 + 7 * 100 ** 6
    b =x * 100 ** 0 + 4 * 100 ** 1 + 6 * 100 ** 2 + 10 * 100 ** 3 + 11 * 100 ** 4 + 1 * 100 ** 5
    c =12 * 100 ** 0 + 2 * 100 ** 1 + 1 * 100 ** 2 + 0 * 100 ** 3 + 8 * 100 ** 4 + 9 * 100 ** 5 + x * 100 ** 6
    if (a - b + c) % 21 == 0:
        print(x)

#cвежий тип 2024 года
#20960
def f(n):
    s = ''
    while n > 0:
        s = str(n % 5) + s
        n = n // 5
    return s
m = 0
for x in range(1,2006):
    a = 5 ** 150 + 5 ** 98 - x
    #m = max(f(a).count('0'), m)
    if f(a).count('0') == 56:
        print(x)



####
def f(n):
    stra = ''
    while n > 0:
        stra += str(n % 3)
        n //= 3
    return stra[::-1]


a = 9 ** 18 + 3 ** 54 - 9
n3 = f(a)
print(n3.count('2'))
