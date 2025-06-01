f = open('txt.txt')

c = 0
for i in f:
    a = sorted(list(map(int, i.split())))
    mx = max(a)
    mn = min(a)
    sm = sum(a) - mx
    sr = sum(a) - mn - mx
    if mx < sm and sr != mx + mn:
        c += 1
print(c)

#открываем файл и записываем кажду строку в список
f = open('9.txt')
for s in f:
    a = [int(x) for x in s.split()] #сплитуем по пробелу (или ';' если файл csv с разделителями ;)
    
    povt = [x for x in a if a.count(x) == 2] #элементы встречаются ровно 2 раза (соответственно ставим значение исходя из условия)
    razl = [x for x in a if a.count(x) == 1] #уникальные (различные) элементы
    kr5 = [x for x in a if x % 5 == 0] #элементы кратные 5
    dv = [x for x in a if len(str(x)) == 2] #двухзначные элементы
    
    
    a = sorted(a) #когда нужно найти мин,макс и другие элементы (сортировка от меньшего к больш)
