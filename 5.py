def f(n):
    s = ''
    while n > 0:
        s = str(n%3) + s
        n = n//3
    return s
m = []
for n in range(200, 1000):
    a = f(n)
    if a.count('2')%2 == 0:
        a += f(int(min(list(a))) + int(max(list(a))))
    else:
        a += f(int(list(a)[0]) + int(list(a)[-1]))
    r = int(a, 3)
    if r > 650 and r % 2 == 0:
        m.append(r)
print(min(m))
