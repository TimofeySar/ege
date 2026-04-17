# f = [0]* 60123
#
# for i in range( 60000):
#     if i == 1:
#         f[i] =1
#     else:
#         f[i] = 2 * i + f[i - 1]
# w = str(f[57693])
# print(w)
# q = list(map(int,(w)))
# print(q)
# print(sum(q)**2)


import turtle

# Настройка экрана
screen = turtle.Screen()
screen.title("Алгоритм из задачи")
screen.bgcolor("white")
screen.setup(width=800, height=800)

# Создание черепашки
t = turtle.Turtle()
t.speed(0)  # максимальная скорость
t.pensize(2)

# Начинаем рисовать
# Повтори 5 [Вперёд 42 Направо 270 Вперёд 55 Налево 90]
for _ in range(5):
    t.forward(42)
    t.right(270)  # то же, что t.left(90)
    t.forward(55)
    t.left(90)

# Поднять хвост
t.penup()

# Вперёд 17 Направо 90 Вперёд 12 Налево 90
t.forward(17)
t.right(90)
t.forward(12)
t.left(90)

# Опустить хвост
t.pendown()

# Повтори 14 [Вперёд 14 Налево 90 Вперёд 200 Налево 90]
for _ in range(2):
    t.forward(14)
    t.left(90)
    t.forward(200)
    t.left(90)

# Завершение
t.hideturtle()
turtle.done()