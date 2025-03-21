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