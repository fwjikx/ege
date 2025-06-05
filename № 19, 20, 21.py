# нечет - ход пети, чет - ход вани

#1 куча
def f(s,m): #s - кол-во камней в куче, m - кол-во ходов
    if s >= 132: return m % 2 == 0
    if m == 0: return 0
    h = [f(s + 3,m - 1), f(s + 6, m - 1), f(s * 3, m - 1)]
    return any(h) if m % 2 != 0 else all(h) #для 19 номера all может поменяться на any если в вопросе звучит "НЕУДАЧНЫЙ ХОД"

print('#19', min([s for s in range(1,132) if f(s,2)])) #игра заканчивается за 2 хода (победа вани)
print('#20', [s for s in range(1,132) if not(f(s,1)) and f(s,3)]) #игра не заканчивается за 1 ход, но заканчивается на 3 ходу (победа пети)
print('#21', min([s for s in range(1,132) if not(f(s,2)) and f(s,4)])) #игра не заканчивается за 2 хода, но заканчивается на 4 ходу (победа вани)

#2 кучи
def f(x,y,m): #x = 1 куча , y = 2 куча , m - кол-во ходов
    if (x + y) >= 77: return m % 2 == 0
    if m == 0: return 0
    h = [f(x + 3, y, m - 1), f(x * 3, y , m - 1), f(x , y + 3, m - 1), f(x , y * 3, m - 1)]
    return any(h) if m % 2 != 0 else all(h) #вот тут второе all меняем на any только в 19 номере если вопрос при "неудачном ходе"

print('#19', min([s for s in range(1,65) if f(12,s,2)]))
print('#20', [s for s in range(1,65) if not(f(12,s,1)) and f(12,s,3)])
print('#21', [s for s in range(1,65) if not(f(12,s,2)) and f(12,s,4)])

#отрезки в играх
def f(x, m):
    if 105 >= x >= 97: return m % 2 == 0
    if x > 105: return m % 2 != 0
    if m == 0: return 0
    h = [f(x + 3, m - 1), f(x + 5, m - 1), f(x * 3, m - 1)]
    return any(h) if m % 2 != 0 else all(h)


print('#19', [s for s in range(1, 97) if f(s, 2)])
print('#20', [s for s in range(1, 97) if not (f(s, 1)) and f(s, 3)])
print('#21', [s for s in range(1, 97) if not (f(s, 2)) and f(s, 4)])


#одна куча 
from functools import lru_cache


def step(p):
    res = []
    if p > 0:
        res += p + 1, p * 3
    return res


#print(step(11))


@lru_cache()
def game(p):
    if p >= 268: return 0
    if any(game(p1) == 0 for p1 in step(p)): return 1
    if all(game(p1) == 1 for p1 in step(p)): return 2 # в 19 при неудачном ходе пети меняется на any 
    if any(game(p1) == 2 for p1 in step(p)): return 3
    if all(game(p1) in (1, 3) for p1 in step(p)): return 4


for p in range(1, 268):
    if game(p) == 2: # зависит от того за сколько ходов должна закончиться игра 
        print(p)

#две кучи
from functools import lru_cache


def step(p):
    (a, b) = p
    return (a + 1, b), (a, b + 1), (a * 3, b), (a, b * 3)


@lru_cache(None)
def game(p):
    if sum(p) >= 175: return 0
    if any(game(p1) == 0 for p1 in step(p)): return 1
    if all(game(p1) == 1 for p1 in step(p)): return 2 # в 19 при неудачном ходе пети меняется на any 
    if any(game(p1) == 2 for p1 in step(p)): return 3
    if all(game(p1) in (1, 3) for p1 in step(p)): return 4


for s in range(1, 155):
    p = (19, s)
    if game(p) == 4: # зависит от того за сколько ходов должна закончиться игра (обычно в 19=2, в 20=3, в 21=4)
        print(s)
