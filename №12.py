a = '1' + '9' * 100
while '19' in a or '299' in a or '3999' in a:
    if '19' in a:
        a = a.replace('19', '2', 1)
    if '299' in a:
        a = a.replace('299', '3', 1)
    if '3999' in a:
        a = a.replace('3999', '1', 1)

print(a)