def deveterich(n):
    stroka = ''
    while n > 0:
        stroka += str(n % 27)
        n //= 27
    return stroka[::-1]


for x in range(5760, 5770):
    a = 2 * 729 ** 73 + 2 * 243 ** 78 + 81 ** 81 + 2 * 27 ** 84 + 2 * 9 ** 97 + 58
    n9 = deveterich(a)
print(n9.count('0'))
