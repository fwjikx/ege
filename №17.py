a = [int(x) for x in open('17_Demo22.txt')]

mn = min(i for i in a if i % 100 == 15)
sp = []
for i in range(len(a) - 2):
    usl1 = abs(a[i]) % 10 == 3
    usl2 = abs(a[i + 1]) % 10 == 3
    usl3 = abs(a[i + 2]) % 10 == 3
    if usl1 + usl2 + usl3 <= 2:
        if a[i] + a[i + 1] + a[i + 2] >= mn:
            sp.append(a[i] + a[i + 1] + a[i + 2])

print(len(sp), max(sp))