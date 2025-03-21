a = []
for i in range(14014, 49836):
    if (i % 13 == 5) and (i % 5 != 0) and (i % 11 != 0):
     a.append(i)

print(len(a), max(a))