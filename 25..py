def dell(n):
    m = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            m.append(i)
            m.append(n//i)

    return sorted(list(set(m)))

mas = []
for i in range(1125000, 400000000000):
    if len(mas) < 5:
        m = dell(i)
        f = 0
        for j in range(len(m)):
            if m[j] %10 == 7 and m[j] != 7 and m[j] != i:
                mas.append([i, m[j]])
                break

    else:
        break
print(mas)
