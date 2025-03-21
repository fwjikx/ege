# нечет - ход пети, чет - ход вани

# type1(№19-21) ОДНА КУЧА

def f(s, m):
    if s >= 30: return m % 2 == 0
    if m == 0: return 0
    h = [f(s + 1, m - 1), f(s * 2, m - 1)]
    return any(h) if m % 2 != 0 else all(h) #  ДЛЯ 19) any, а не all, когда в условии сказано, что после неудачного 1-ого хода Пети


print('19)', [s for s in range(1, 30) if f(s, 2)])
print('20)', [s for s in range(1, 30) if not f(s, 1) and f(s, 3)])
print('21)', [s for s in range(1, 30) if not f(s, 2) and f(s, 4)])
'''


# type2(№19-21) ДВЕ КУЧИ
def f(a, b, m):
    if a + b <= 20: return m % 2 == 0
    if m == 0: return 0
    h = [f(a - 1, b, m - 1), f(a, b - 1, m - 1), f(a // 2, b, m - 1), f(a, b // 2, m - 1)]
    return any(h) if m % 2 != 0 else all(h)  # 19) any, а не all, т.к. в условии сказано, что после неудачного 1-ого хода Пети



print('19)', [s for s in range(10, 100) if f(10, s, 2)])
print('20)', [s for s in range(10, 100) if not f(10, s, 1) and f(10, s, 3)])
print('21)', [s for s in range(10, 100) if not f(10, s, 2) and f(10, s, 4)])

'''

