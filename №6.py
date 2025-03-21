from turtle import *

m = 10

speed(100000)
right(90)
pen()


for i in range(2):
    forward(10 * m)
    right(90)
    forward(18 * m)
    right(90)
penup()
forward(5 * m)
right(90)
forward(7 * m)
left(90)
pendown()
for i in range(2):
    forward(10 * m)
    right(90)
    forward(7 * m)
    right(90)

penup()
speed(2000)
for x in range(0, 50):
    for y in range(0, 25):
        setpos(-x * m, -y * m)
        dot(5, 'red')
done()
