# f = open('17.txt').readlines()
# a = list(map(int, f))
# su = 0
# sh =  0
# for i in range(0, len(a) - 1):
#     if a[i] % 3 == 0 or + a[i+1] % 3 == 0:
#         sh += 1
#         su = max(su, a[i] + a[i+1])
# print(sh, su)


# f = open('17.txt').readlines()
# a = list(map(int, f))
# mmm = min([x for x in a if abs(x) % 10 == 3])
#
# mmax = 0
# sh =0
# for i in range(len(a) - 1):
#     mm = min(a[i], a[i + 1])
#     if abs(mm) % 10 == 3:
#         if a[i]**2 + a[i + 1]**2 < mmm**2:
#             sh += 1
#             mmax = max(mmax, a[i]**2 + a[i + 1]**2)
# print(sh, mmax)
#
#
# f = open('17.txt').readlines()
# a = list(map(int, f))
#
# # Находим минимальное число, оканчивающееся на 3
# ends_with_3 = [x for x in a if abs(x) % 10 == 3]
# if not ends_with_3:
#     min3 = 0
# else:
#     min3 = min(ends_with_3)
#
# count = 0
# max_sum_sq = 0
#
# for i in range(len(a) - 1):
#     m = min(a[i], a[i+1])
#     if abs(m) % 10 == 3:  # оканчивается на 3
#         sum_sq = a[i]**2 + a[i+1]**2
#         if sum_sq < min3**2:
#             count += 1
#             if sum_sq > max_sum_sq:
#                 max_sum_sq = sum_sq
#
# print(count, max_sum_sq)


