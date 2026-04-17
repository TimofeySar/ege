# from turtle import *
#
# screensize(1000, 1000)
# left(90)
# m = 20
# speed(0)
# down()
#
# for i in range(4):
#     fd(6 * m)
#     rt(90)
#     fd(6*m)
#     lt(90)
#     fd(6 * m)
#     rt(90)
# tracer(0)
# up()
#
# for x in range(-50 * m, 50 * m, m):
#     for y in range(-50 * m, 50 * m, m):
#         goto(x, y)
#         dot(5)
#
# done()
#
#
#
import turtle as t

t.screensize(1000, 1000)
m = 20
t.speed(0)
t.begin_fill()
t.lt(90)
t.down()
for i in range(4):
    t.fd(6 * m)
    t.rt(90)
    t.fd(6*m)
    t.lt(90)
    t.fd(6 * m)
    t.rt(90)
t.up()
t.tracer(0)
t.end_fill()
count = 0
canvas = t.getcanvas()
for x in range(-50 * m , 50 * m,m):
    for y in range(-50 * m, 50 * m, m):
        s = canvas.find_overlapping(x, y, x, y)
        if len(s) == 1 and s[0] == 5:
            count +=1
t.done()
print(count)