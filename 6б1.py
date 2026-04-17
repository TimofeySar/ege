from turtle import *

screensize(1000, 1000)
left(90)
m = 20
speed(0)
down()

for i in range(4):
    fd(6 * m)
    rt(90)
    fd(6*m)
    lt(90)
    fd(6 * m)
    rt(90)
tracer(0)
up()

for x in range(-50 * m, 50 * m, m):
    for y in range(-50 * m, 50 * m, m):
        goto(x, y)
        dot(5)

done()