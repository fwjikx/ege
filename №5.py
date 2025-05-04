a = []
for N in range(1, 200):
    chisl = bin(N)[2:]
    chisl += chisl[-1]
    chisl += str(chisl.count('1') % 2)
    r = int(chisl, 2)
    if r > 97:
        a.append(r)
print(min(a))

for n in range(100, 1000):
    s = str(n)
    r = int(s[0])+int(s[1])
    f = int(s[1])+int(s[2])
    first = str(min(r,f))
    second = str(max(r,f))
    d = first + second
    if d == '1115':
        print (n)
        break

for n in range(100,1,-1): #чтобы найти наибольшее начинаем отсчет от 100 с шагом -1
    R = bin(n)[2:]
    R = R[::-1] # отзеркаливаем число
    R = R[R.find('1'):] #срез до первой 1
    if int(R,2)==13:
        print(n)
        break
