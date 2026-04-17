# def f(n ,m):
#     if n > m or n == 10:
#         return 0
#     elif n == m: return 1
#     return f(n + 1, m )+ f(n+2, m)+ f(n * 2, m)
#
# print(f(3, 7) * f(7, 20))

def f(x, y):
    if x < y or x == 12: return 0
    if x == y: return 1
    return f(x - 3, y) + f(x // 2 if x % 2 == 0 else x - 5, y)

print(f(36, 3))