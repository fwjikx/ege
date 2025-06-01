from turtle import *

m = 10
tracer(0)
pendown()

# ниже переписываем алгоритм из задачи
for i in range(4):
    fd(3 * m)
    lt(270)
    fd(5 * m)
    rt(90)
lt(270)
for i in range(3):
    fd(5 * m)
    rt(90)
    fd(3 * m)
    lt(270)

penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, "red")
update()
exitonclick()  # выход по нажатию
done()  # если exit не работает


#это мне
from turtle import *

tracer(0)
left(90)
m = 20
speed(200)
for i in range(5):
    forward(7*m)
    rt(120)

up()
for x in range(-1,10):
    for y in range(-10,15):
        goto(x*m,y*m)
        dot(5)
done()
