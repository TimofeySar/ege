# f = open('17_23757.txt').readlines()
# a = list(map(int, f))
# amin = 9999999
# for i in range(len(a)):
#     if len(str(a[i])) == 2:
#         amin = min(a[i], amin)
#
# sh = 0
# mm = 0
# for i in range(0, len(a)-1):
#     if len(str(a[i])) == 2 and len(str(a[i+1])) != 2:
#         if (a[i] + a[i+1]) % amin == 0:
#             sh += 1
#             mm = max(mm, a[i] + a[i+1])
#     if len(str(a[i])) != 2 and len(str(a[i+1])) == 2:
#         if (a[i] + a[i+1]) % amin == 0:
#             sh += 1
#             mm = max(mm, a[i] + a[i + 1])
#
# print(sh, mm)

f = open('17.txt').readlines()
a = list(map(int, f))
mina = -123213123123
for i in range(len(a)):
    if a[i] < 0 and a[i] % 6 == 0:
        mina = max(mina, a[i])
maxa = 0
sh =0
for i in range(len(a) - 1):
    if ((a[i] < 0 and a[i + 1] >= 0) or (a[i] > 0 and a[i + 1] < 0)) and (a[i] + a[i + 1] > mina):
        sh += 1
        maxa = max(maxa, a[i] ** 2 + a[i + 1] ** 2)
print(sh, maxa)