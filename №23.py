def f(x, end):
    if x > end or x == 27: return 0
    if x == end: return 1
    return f(x + 1, end) + f(x * 2, end) + f(3 * x, end)


print(f(5, 9) * f(9, 43))
