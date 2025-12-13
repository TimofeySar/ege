def f(n ,m):
    if n > m or n == 10:
        return 0
    elif n == m: return 1
    return f(n + 1, m )+ f(n+2, m)+ f(n * 2, m)

print(f(3, 7) * f(7, 20))