a = []
for N in range(1, 200):
    chisl = bin(N)[2:]
    chisl += chisl[-1]
    chisl += str(chisl.count('1') % 2)
    r = int(chisl, 2)
    if r > 97:
        a.append(r)
print(min(a))
