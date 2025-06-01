a = []
for N in range(1, 200):
    chisl = bin(N)[2:]
    chisl += chisl[-1]
    chisl += str(chisl.count('1') % 2)
    r = int(chisl, 2)
    if r > 97:
        a.append(r)
print(min(a))

for n in range(100, 1000):
    s = str(n)
    r = int(s[0])+int(s[1])
    f = int(s[1])+int(s[2])
    first = str(min(r,f))
    second = str(max(r,f))
    d = first + second
    if d == '1115':
        print (n)
        break

for n in range(100,1,-1): #чтобы найти наибольшее начинаем отсчет от 100 с шагом -1
    R = bin(n)[2:]
    R = R[::-1] # отзеркаливаем число
    R = R[R.find('1'):] #срез до первой 1
    if int(R,2)==13:
        print(n)
        break


#функция перевода числа в любую систему счисления до 10
#вместо X ставите любое число, например "3"
def f(n):
    s = ''
    while n > 0:
        s = str(n % X) + s
        n = n // X
    return s
 
#Питоновская функция перевода в 2,8,16

x = bin(n)[2:]
x = oct(n)[2:]
x = hex(n)[2:]
 
#обратно в 10 сс

r = int(n,2) # вместо "2" - та система из которой переводим обратно в 10 сс

#сумма единиц или нулей
if x.count('1') or x.count('0'):

#Срезать 2 первых или 2 последних знака

x = x[2:]
x = x[:-2]

#Добавить единицу в конец

x = x + '1'

#добавить единицу в начало

x = '1' + x

#убрать 3 первых знака и вставить туда единицу

x = '1' + x[3:]

#Поменять последний и первый разряд местами
x = x[-1] + x[1:-1] + x[0]

#Сумма цифр числа
s = sum(map(int,s)) #s - строка


#произведение цифр числа
from math import *
s = prod(map(ints))
