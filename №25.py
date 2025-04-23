# МАСКА
# from fnmatch import fnmatch
#
# for x in range(0, 10 ** 8 + 1, 2321): № менять шаг и диапозон по условию
#    if fnmatch(str(x), '1*2??76'): # менять маску по условию
#        print(x, x // 2321)


# ДЕЛИТЕЛИ (Пусть М - сумма минимального и максимального натуральных делителей целого числа)
i = 700001
k = 0
while k != 5:
    divs = set()
    for d in range(2, round(i ** 0.5) + 1):
        if i % d == 0:
            divs.add(d)
            divs.add(i // d)
    if len(divs) > 0:
        m = min(divs) + max(divs)
        if m % 10 == 4:
            print(i, m)
            k += 1
    i += 1
