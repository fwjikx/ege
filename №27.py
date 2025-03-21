clasterA = [[], []]
clasterB = [[], [], []]

for line in open('27A_18623.txt'):
    x, y = [float(k) for k in line.split()]
    if y < 3:
        clasterA[0].append([x, y])
    else:
        clasterA[1].append([x, y])
for line in open('27B_18623.txt'):
    x, y = [float(k) for k in line.split()]
    if y < -x + 8:
        clasterB[0].append([x, y])
    elif y > 1.5 * x - 6.5:
        clasterB[1].append([x, y])
    else:
        clasterB[2].append([x, y])


def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def center(cl):
    m = []
    for p in cl:
        sm = sum(d(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


centersA = [center(cl) for cl in clasterA]
centersB = [center(cl) for cl in clasterB]

pxA = sum(x for x, y in centersA) / 2 * 100000
pyA = sum(y for x, y in centersA) / 2 * 100000
pxB = sum(x for x, y in centersB) / 3 * 100000
pyB = sum(y for x, y in centersB) / 3 * 100000
print(int(pxA), int(pyA))
print(int(pxB), int(pyB))
