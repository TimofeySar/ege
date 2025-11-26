# def f(x):
#     s = ''
#     if f == '0':
#         return '0'
#     while x != 0:
#         x, r = divmod(x, 29)
#         s = str(r) + s
#     return s
#
#
# a = 7 ** 91 + 7 ** 160
# for i in range(2030, 0, -1):
#     q = a - i
#     m = f(q)
#     if m.count('0') == 70:
#         print(i)
#         break
# a = 29**293 + 29 ** 271
# m = 0
# for i in range(1, 8411):
#     q = a - i
#     w = f(q)
#     m = max(m, w.count('0'))
# print(m)


a = '0123456789ABCDEFGHJKL'
for x in a:
    if (int('90'+x+'5F42', 23) + int(x+'4C82G1', 23))%22 == 0:
        print((int('90'+x+'5F42', 23) + int(x+'4C82G1', 23))/22)