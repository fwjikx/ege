s = open('24_17641.txt').readline()
while '+*' in s: s = s.replace('+*', '+ *')
while '++' in s: s = s.replace('++', '+ +')
while '**' in s: s = s.replace('**', '* *')
while '*+' in s: s = s.replace('*+', '* +')

m = -float('inf')
for kusochek in s.split(' '):
    if len(kusochek) > m:
        for i in range(len(kusochek) - 1):
            podstroka = kusochek[i]
            if podstroka[0] not in '+*' and kusochek[i] + kusochek[i + 1] not in ['01', '02', '03', '04', '05', '06',
                                                                                  '07',
                                                                                  '08', '09', '00']:
                for j in range(i + 1, len(kusochek)):
                    podstroka += kusochek[j]
                    if podstroka[-1] not in '+*':
                        if eval(podstroka) == 0:
                            m = max(m, len(podstroka))

print(m)

# хуйня какая то
# from re import findall
# s = open('24_17641.txt').readline()
# a = findall(r'(?:0|[123456789][0123456789]*)(?:[*+](?:0|[123456789][0123456789]*))*', s)
# res = max(a, key=len)
# print(len(res))