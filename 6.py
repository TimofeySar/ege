from turtle import *

m = 20
lt(90)
speed(0)
for i in range(4):
    fd(5*m)
    rt(90)
up()
tracer(0)
for x in range(10):
    for y in range(10):
        goto(x*m, y*m)
        dot(5)
done()