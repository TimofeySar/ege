def dist(a):
    mas = []
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            mas.append(i)
            mas.append(a // i)
    return sorted(mas)


for i in range(106732567, 152673837):
    a = dist(i)
    if len(a) == 3:
        print(a[-1])
