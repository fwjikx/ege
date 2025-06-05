# print('w x y z')
# for w in 0, 1:
#    for x in 0, 1:
#        for y in 0, 1:
#            for z in 0, 1:
#                if ((not x) and y and z and (not w)) or ((not x) and y and (not z) and (not w)) or (
#                        x and y and z and (not w)) == 1:
#                    print(w, x, y, z)


from itertools import product, permutations


def f(x, y, w, z):
    return w and ((not x) or y) and ((not y) and z or y and (not z))  # w ∧ (¬x ∨ y) ∧ (¬y ∧ z ∨ y∧ ¬ z)


for x1, x2, x3, x4 in product([0, 1], repeat=4):
    t = (
        (0, 0, x3, x4, 1),
        (x1, 0, 0, 1, 1),
        (1, x2, 0, 1, 1)
    )
    if len(t) == len(set(t)):
        for p in permutations('xywz', r=4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p)

# несколько функций
from itertools import *


def f1(a, b, c, d):
    return ((not a) and (not b)) or (b == c) or d

def f2(a,b,c,d)
    return 

for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
    t = [(1, x1, 1, 1), (x2, 1, 0, 0,), (x3, 0, 0, x4)]
    if len(t) == len(set(t)):
        for p in permutations('abcd', r=4):
            if [f1(**dict(zip(p, m))) for m in t] == [1, 1, 0] and \
                    [f2(**dict(zip(p, m))) for m in t] == [0, x5, 0]:
                print(*p)
