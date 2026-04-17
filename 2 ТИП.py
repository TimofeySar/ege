print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (z or (x == (y <= w))) == 0:
                    print(x, y, z, w)

# print(1024 * 768 / (2 ** 30) )

# def Perevod(n, c):
#     st = ''
#     while n > 0:
#         st += str(n % c)
#         n //= c
#     return st[::-1]
#
#
# for n in range(1, 1000):
#     d = Perevod(n, 2)
#     d += str(sum(list(map(int, list(d)))) % 2)
#     d = Perevod(int(d), 2)
#     d += str(sum(list(map(int, list(d)))) % 2)
#     # for i in range(2):
#     # d += str(sum(list(map(int, list(d)))) % 2)
#     # d = Perevod(int(d), 2)
#     if int(d, 2) > 77:
#         print(int(d, 2))
#         break

#
# '''8 '''
# for i in '':
#     for u in '':
#         for y in '':
#             for o in '':
#                 st = i + u + y + o
#
#
