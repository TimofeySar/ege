def f(x):
    if x == 0:
        return "0"

    ternary_digits = []
    while x > 0:
        remainder = x % 3  # Получаем остаток от деления на 3
        ternary_digits.append(str(remainder))
        x //= 3  # Целочисленное деление на 3

    # Объединяем остатки в обратном порядке, чтобы получить троичную запись
    return "".join(ternary_digits[::-1])

for n in range(1000, 1, -1):
    w = f(n)
    if n % 5 == 0:
        w += w[-2:]


    else:
        w += f((n%5)*7)
    e = int(w, 3)
    if e <= 273:
        print(n)
        break

w = f(32)
if n % 5 == 0:
    w += w[-2:]


else:
    w += f((n%5)*7)
e = int(w, 3)
print(e)