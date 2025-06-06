'''Определите в прилагаемом файле максимальное количество
идущих подряд символов, среди которых ни одна буква не стоит рядом с буквой,
 а цифра — с цифрой.'''


f = open('24_9845.txt')
s = f.readline()
b = 'ABC'
c = '89'
k = 0
m = 0
for i in range(len(s)-1):
    if (s[i] in b and s[i+1] not in b) or (s[i] in c and s[i+1] not in c):
        k+=1
        m = max(k,m)
    else:
        k = 0
print(m+1)

#2ой способ

f = open('24_9845.txt')
s = f.readline()
s = s.replace('A','*').replace('B','*').replace('C','*').replace('8','?').replace('9','?')
k = m = 0
for i in range(len(s) -1 ):
    if s[i] + s[i+1] != '**' and s[i] + s[i+1] != '??':
        k+=1
        m = max(k,m)
    else:
        k = 0
print(m+1)



'''макс длинна подстроки в которой "А" встречается ровно 2024 раза'''

f = open('24var01.txt')
s = f.readline()

m = 10001101011010
a = []
for i in range(len(s)):
    if s[i] == 'A':
        a.append(i)

for i in range(2023, len(a)):
    m = min(m , a[i] - a[i - 2023] + 1)
print(m)


'''Определите в прилагаемом файле максимальное количество идущих подряд 
символов (длину непрерывной подпоследовательности), среди которых 
символ Y встречается не более 150 раз.'''
f = open('24_9753.txt')
s = f.readline()

s = s.split('Y')
m = 0
for i in range(len(s) - 151):
    k = 'Y'.join(s[i:i+151])
    m = max(m, len(k))
print(m)

'''макс длинна подстроки в которой два нуля не стоят рядом'''
f = open('24var09-12.txt')
s = f.readline()
k = m = 0
for i in range(len(s)-1):
    if s[i] + s[i+1] != '00':
        k +=1
        m = max(k,m)
    else:
        k = 0
print(m+1)


'''Текстовый файл состоит из символов A, C, D, F и U.
Определите максимальное количество идущих подряд пар символов вида
согласная + гласная
в прилагаемом файле.'''
f = open('24_7094.txt').readline()
s=f.readline
k=m=0
s = f.replace('A','1').replace('U','1').replace('C','0').replace('D','0').replace('F','0')
for i in range(len(s)-1):
    if s[i]+s[i+1]!='11' and s[i]+s[i+1]!='00':
        k=k+1
        m =max(m,k)
    else:
        k=0
print(m+1)


'''Определите максимальное 
количество идущих подряд символов, 
среди которых никакие две буквы из 
набора букв N, O и P (с учетом повторений) не записаны подряд.'''
s = open('24_8510.txt').readline()
k = m = 0
bad = ['NN','NO','NP','PP','PO','PN','OO','ON','OP']
for i in range(len(s)-1):
    if s[i] + s[i+1] not in bad:
        k+=1
        m = max(k,m)
    else:
        k = 0
print(m+1)

'''Определите максимальное количество идущих подряд пар символов 
AB или CB в прилагаемом файле.
Искомая подпоследовательность должна состоять только из пар AB, 
или только из пар CB, или только 
из пар AB и CB в произвольном порядке следования этих пар.'''
s = open('24_7272.txt').readline()

k = m = 0
s = s.replace('AB','*').replace('CB','*')

for i in range(len(s)):
    if s[i] == '*':
        k+=1
        m = max(k,m)
    else:
        k = 0
print(m)

#РЕГУЛЯРКИ!!!

'''Текстовый файл состоит из цифр 0, 7, 8, 9 и знаков арифметических операций «-» и «*» (вычитание и умножение).
Определите максимальное количество символов в непрерывной последовательности, 
которая является корректным арифметическим выражением с целыми неотрицательными числами.
В этом выражении никакие два знака арифметических операций не стоят рядом, в записи чисел отсутствуют незначащие (ведущие) нули и число 0 не имеет знака.
В ответе укажите количество символов.'''
from re import *
f = open("24_20813.txt").readline()
number = r'(?:[1-9][0-9]*|0)'
pattern = rf'{number}(?:[-*]{number})*'
print(max(map(len, findall(pattern, f))))


'''Двойной цикл Кабанова'''
s = open('файл.txt').readline()

m = 0 #максимум
for l in range(len(s)): #левый указатель
    for r in range(l + m, len(s)): #правый указатель
        c = s[l:r + 1] #срез строки
        if #условие из задачи
            m = max(m,len(c)) #находим максимум
        else:
            break #чуть ускоряем работу
print(m) #вывод максимума


'''Текстовый файл состоит из символов, обозначающих заглавные буквы латинского алфавита и десятичные цифры.Определите в
прилагаемом файле максимальное количество идущих подряд символов, которые могут представлять запись чётного числа в
двенадцатеричной системе счисления. В этой записи отсутствуют незначащие нули(ведущие нули)'''

from re import finditer

s = open('24_9791.txt').readline()

p = r'[1-B][0-B]*[02468A]'  # max символ в 12-ричной системе B. начинаем с 1, тк с нуля начать не можем,
                            # дальше выбираем любые симсволы в любом кол-ве, в конце проверяем на чётность

print(max(len(x.group()) for x in finditer(p, s)))

'''Текстовый файл состоит из символов, обозначающих заглавные буквы латинского алфавита и цифры от 1 до 9 включительно.
Определите в прилагаемом файле максимальное ЧИСЛО в двенадцатеричной системе счисления кратное 6. В этой записи отсутствуют незначащие нули(ведущие нули)'''

from re import finditer

s = open('24_9791.txt').readline()

p = r'[1-B][0-B]*[06]'  # в конце проверям на кратность 6, тк 12ричная СС, то число должно оканчиваться на 0/6

print(max([x.group() for x in finditer(p, s)], key=lambda k: int(k, 12)))

'''Текстовый файл состоит из десятичных цифр, «+» и «*». Определите максимальное кол-во символов в непрерывной последовательности,
являющейся корректным арифметическим выражением с целыми неотрицательными числами (без знака), значение которого равно нулю. 
В этом выражении никакие два знака арифметических операций не стоят рядом, порядок действий определяется по правилам математики. 
В записи чисел отсутствуют незначащие (ведущие) нули.'''

from re import *

s = open('24_17641 (1).txt').readline()
num = r'(([1-9][0-9]*)|0)'  # число от 1-9, затем цифры 0-9 в любом кол-ве ИЛИ 0 тк число должно быть неотр, а не натуральным
pr = rf'(({num}\*)*0(\*{num})*)'  # (num*num*num*num*)(ЛЮБОЕ КОЛ-ВО РАЗ) 0 (*num*num*num*num)(ЛЮБОЕ КОЛ-ВО РАЗ)
p = rf'{pr}(\+{pr})*'  # pr +pr+pr+pr+pr(любое кол-во раз)

m = max([x.group() for x in finditer(p, s)], key=len)
print(len(m))
print(m)


'''Текстовый файл состоит из символов T, U, V, W, X, Y и Z.Определите в прилагаемом файле максимальное количество
идущих подряд символов (длину непрерывной подпоследовательности), среди которых символ Y встречается не более 150 раз.'''

s = open('24_9753.txt').readline()
m = 0
for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l:r + 1]
        if c.count('Y') <= 150:
            m = max(m, len(c))
        else:
            break
print(m)

'''Текстовый файл состоит из символов, обозначающих заглавные буквы латинского алфавита и цифры от 1 до 9 включительно.
Определите в прилагаемом файле максимальное количество идущих подряд символов, которые могут представлять запись числа
в шестнадцатеричной системе счисления.'''

from string import printable

s = open('24_9791.txt').readline()

for c in printable[16:36].upper():
    s = s.replace(c, '*')  # находим символы, которые не могут быть в шестнадцатеричной системе счисления и заменям их

m = 0
for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l:r + 1]
        if '*' not in c and c[0] != '0':
            m = max(m, len(c))
        else:
            break
print(m)

'''Текстовый файл состоит из символов, обозначающих буквы латинского алфавита А, В, С и цифры 8 и 9.Определите в прилагаемом 
файле максимальное количество идущих подряд символов, среди которых ни одна буква не стоит рядом с буквой, а цифра — с цифрой.'''

s = open('24_9845.txt').readline()
s = s.replace('B', 'A').replace('C', 'A').replace('9','8')  # заменим все буквы на одну, как и с цифрами, чтобы упростить условие
m = 0
for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l:r + 1]
        if '88' not in c and 'AA' not in c:
            m = max(m, len(c))
        else:
            break
print(m)


'''Текстовый файл состоит из символов A, B, C, D, E и F. Определите максимальное количество идущих подряд символов в
прилагаемом файле, среди которых пара символов CD (в указанном порядке) встречается ровно 160 раз..'''
# ОЧЕНЬ ДОЛГО СЧИТАЕТ, НА ЭКЗЕ ЗАЙМЕТ МИНУТ 5-10 ДУМАЮ

s = open('24_17535.txt').readline()
m = 0
for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l:r + 1]
        if c.count('CD') <= 160:  # ПРОСЯТ РОВНО 160 РАЗ, НО СТАВИМ ЗНАК <=
            m = max(m, len(c))
        else:
            break
print(m)
