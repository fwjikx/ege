from itertools import product, permutations

words = list(product('МАНГУСТ', repeat=6))
words.sort()
n = 0
a = []
for word in words:
    n += 1
    if word[0] != 'У' and word.count('М') == 2 and word.count('Г') <= 1:
        a.append(n)

print(max(a))
