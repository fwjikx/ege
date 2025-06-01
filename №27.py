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

####
#дистанция от точки А до точки В
def d(a,b):
    x1,y1 = a
    x2,y2 = b
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


#поиск центров кластеров
def center(cl):
    m = []
    for p in cl:
        sm = sum(d(p, p1) for p1 in cl)
        m.append([sm,p])
    return min(m)[1]

#пример поиска центров
centerA = [center(cl) for cl in clA]
centerB = [center(cl) for cl in clB]

#среднее арифм. абсцисс и ординат центров кластеров
px = int(sum(x for x,y in centerA) / 2 * 10000)
py = int(sum(y for x,y in centerA) / 2 * 10000)
px2 = int(sum(x for x,y in centerB) / 3 * 10000)
py2 = int(sum(y for x,y in centerB) / 3 * 10000)

#МЕТОД DBSCAN (Шастин)
data = []
clusters = []
while data:
    clusters.append([data.pop(0)])
    for p1 in clusters[-1]:
        neighbors = [p for p in data if d(p1,p) < 1] #d - дистанция из функции выше
        clusters[-1] += neighbors
        for p in neighbors: data.remove(p)

#DBCAN (Родя)

from math import *

f = open('файл тут')

data = []
for s in f:
    data.append([float(k) for k in s.split()])


def dbscan(p0):
    cluster = [p for p in data if dist(p0, p) < 1]
    if cluster:
        for p in cluster: data.remove(p)
        next_clusters = [dbscan(p) for p in cluster]
        cluster += sum(next_clusters, [])
    return cluster


clusters = []
while len(data) != 0:
    cluster = dbscan(data[0])
    clusters.append(cluster)

#DBSCAN (Столбов)

def dbscan(c,r):
    cl = []
    while c:
        cl.append([c.pop(0)])
        for j in cl[-1]:
            for i in c[:]:
                if dist(i,j) < r:
                    cl[-1].append(i)
                    c.remove(i)
    return cl
